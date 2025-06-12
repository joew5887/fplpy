from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Iterable, Optional, Type, TypeVar, Generic, Union, Literal
from dataclasses import fields
from functools import cache
from ...external.template import ExternalFPLData
from ...external.api import FPLAPI
from ...external.github import VaastavGitHub
from ...err.types import IDMatchesZeroElements, IDNotUnique
from ...util.typed_ordered_set import TypedOrderedSet
from ...util.dataclass import all_attributes_present
from ...util.other import method_choice, set_dict_values_tuple


element = TypeVar("element", bound="Element[Any]")  # generic type of `Element`


class Element(ABC, Generic[element]):
    """Template class for an FPL element.

    E.g. Players, Teams, Fixtures
    """

    UNIQUE_ID_ATTR: str = "id"
    _data_source = None
    STR_ATTR: str = "name"
    
    @classmethod
    @abstractmethod
    def get_latest_external_data(cls, source: FPLAPI) -> list[dict[str, Any]]: ...
    
    @classmethod
    @abstractmethod
    def from_dict_api(cls, element_args: dict[str, Any]) -> dict[str, Any]:
        return element_args
    
    @classmethod
    @abstractmethod
    def from_dict_vaastav(cls, element_args: dict[str, Any]) -> dict[str, Any]:
        return element_args

    def __str__(self) -> str:
        """Gets attribute called `cls.STR_ATTR`.

        Returns
        -------
        str
            Text name of element.
        """
        return str(getattr(self, type(self).STR_ATTR))

    @property
    def unique_id(self) -> int:
        """Returns unique ID for an object.

        Returns
        -------
        int
            Unique ID.

        Raises
        ------
        AttributeError
            If the ID cannot be found from the `UNIQUE_ID_ATTR`.
        """
        id_col: str = type(self).UNIQUE_ID_ATTR
        id_: int = getattr(self, id_col)

        return id_

    @classmethod
    def from_dict(cls: Type[element], new_instance: dict[str, Any], source: ExternalFPLData) -> element:
        class_fields = fields(cls)  # `cls` must be a dataclass.
        field_names = {f.name for f in class_fields}

        # Check if all attributes in dictionary present as dataclass attributes
        if all_attributes_present(cls, new_instance):
            required_attrs = {attr: new_instance[attr]
                              for attr in field_names}
        else:
            raise KeyError(
            f"Missing: {field_names.difference(set(new_instance.keys()))}")

        # Alter attributes based on external source. e.g. formatting time
        if isinstance(source, FPLAPI):
            edited_attrs = cls.from_dict_api(required_attrs)
        elif isinstance(source, VaastavGitHub):
            edited_attrs = cls.from_dict_vaastav(required_attrs)
        else:
            raise TypeError()

        return cls(**edited_attrs)
    
    @classmethod
    @cache
    def get(cls, *, source: FPLAPI, method_: Literal["all", "or"] = "all", **attr_to_value: Union[Any, Iterable[Any]]) -> ElementGroup[element]:
        """Gets a group of elements based on filters and conditions passed.

        Conditions passed by `attr_to_value`. E.g. `web_name="Spurs"`

        Parameters
        ----------
        method_ : str, optional
            "all" if all conditions must be met, "or" for any condition to be met, by default "all"

        Returns
        -------
        ElementGroup[element]
            All elements that satisfy the filters passed, may also be empty.
        """
        all_elems = cls.get_all(source)

        return all_elems.filter(method_=method_, **attr_to_value)

    @classmethod
    @cache
    def get_all(cls, source: FPLAPI) -> ElementGroup[element]:
        """Gets all elements as objects of parent class `Element`.

        Returns
        -------
        ElementGroup[element]
            All elements.
        """
        elements = cls.get_latest_external_data(source)
        elements_as_objs: list[element] = [cls.from_dict(elem, source) for elem in elements]
        elements_sorted = sorted(elements_as_objs, key=lambda p: p.unique_id)

        return ElementGroup[element](elements_sorted)

    @classmethod
    @cache
    def get_by_id(cls, source: FPLAPI, id_: Any) -> Optional[element]:
        """Get an element by their unique id.

        Parameters
        ----------
        id_ : Any
            ID of element to find.

        Returns
        -------
        Optional[element]
            The found element. May return None if no element has been found.
        """
        filter_ = {cls.UNIQUE_ID_ATTR: id_}
        element_group = cls.get(source, **filter_)

        if not element_group.is_length_1:
            raise Exception
        
        return element_group[0]
    
    
class ElementGroup(TypedOrderedSet[element], Generic[element]):
    def __init__(self, iterable: Iterable[element]) -> None:
        super().__init__(iterable)

    @property
    def is_length_1(self) -> bool:
        return len(self) == 1

    def filter(self, *, method_: Literal["all", "or"] = "all", **constraints: Union[Any, tuple[Any]]) -> ElementGroup[element]:
        # Method check
        func = method_choice(method_)
        constraints = set_dict_values_tuple(constraints)

        elements_found = []

        for elem in self:
            conditions_by_attr = []

            for attr, values in constraints.items():
                elem_attr = getattr(elem, attr)

                for value in values:
                    if elem_attr == value:
                        conditions_by_attr.append(True)
                        break
                else:
                    conditions_by_attr.append(False)

            if func(conditions_by_attr):
                elements_found.append(elem)

        return ElementGroup[element](elements_found)

    def get_top_n_elements(self, col_by: str, n: int, reverse: bool = True) -> ElementGroup[element]:
        """Gets top n elements of an attribute and returns them in a new ElementGroup.

        Parameters
        ----------
        col_by : str
            Attribute to rank elements by.
        n : int
            Number of elements to save.

        Returns
        -------
        ElementGroup[element]
            Group of top elements of size `n`.
        """
        elements_sorted = self.sort(col_by, reverse=reverse)
        best_elements = ElementGroup[element]([])
        
        for i in range(n):
            best_elements.append(elements_sorted[i])
        
        return best_elements
    
    def group_by(self, group_by_attr: str) -> dict[Any, ElementGroup[element]]:
        """Split an ElementGroup into multiple sub-groups by an attribute value.

        Parameters
        ----------
        group_by_attr : str
            Attribute to create groups by.

        Returns
        -------
        dict[Any, ElementGroup[element]]
            The key is the attribute value, the value is elements with a common attribute value.

        Raises
        ------
        AttributeError
            If `group_by_attr` does not exist for the elements.
        """
        groups: dict[Any, list[element]]
        groups = {}

        for elem in self:
            elem_attr = getattr(elem, group_by_attr, None)

            if elem_attr is None:
                raise AttributeError(
                    f"'{group_by_attr}' not in attributes.")

            if elem_attr not in groups:
                groups[elem_attr] = [elem]  # Creates new group
            else:
                groups[elem_attr].append(elem)

        return {attr: ElementGroup[element](elems) for attr, elems in groups.items()}
    
    def sort(self, sort_by: str, *, reverse: bool = True) -> ElementGroup[element]:
        """Sorts a list of like elements by an attribute.

        Parameters
        ----------
        sort_by : str
            Attribute name to sort `elements` by.
        reverse : bool, optional
            True if in descending order, by default True

        Returns
        -------
        list[element]
            `elements` sorted by `sort_by`.
        """

        def foo(elem: Element[Any]) -> Any:
            return getattr(elem, sort_by)

        if self.is_empty:
            return ElementGroup[element]([])

        elements_sorted = sorted(self.to_list(), key=foo, reverse=reverse)

        return ElementGroup[element](elements_sorted)
    
    def split(self, *, method_: Literal["all", "or"] = "all", **attr_to_value: Union[Any, Iterable[Any]]) -> tuple[ElementGroup[element], ElementGroup[element]]:
        """Splits an ElementGroup into two sub-groups, where one group satisfies the filters, the other does not.

        Parameters
        ----------
        method_ : bool, optional
            "all" if all conditions must be met, "or" for any condition to be met, by default "all"

        Returns
        -------
        tuple[ElementGroup[element], ElementGroup[element]]
            The first group satisfies the filter, the other does not.
        """
        filtered_elems = self.filter(method_=method_, **attr_to_value)

        not_filtered_elems = ElementGroup[element](
            [elem for elem in self if elem not in filtered_elems.to_list()])

        return filtered_elems, not_filtered_elems
