from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Iterable, Iterator, Optional, SupportsIndex, Type, TypeVar, Generic, Union, overload, Callable, Literal
from dataclasses import fields
from functools import cache
from random import choice, sample
import pandas as pd
from ...external.template import ExternalFPLData
from ...external.api import FPLAPI
from ...external.github import VaastavGitHub
from ...err.types import IDMatchesZeroElements, IDNotUnique


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

        try:
            id_uniqueness_check(element_group)
        except IDMatchesZeroElements:
            return None
        else:
            return element_group[0]


class ElementGroup(ABC, Generic[element]):
    """Way to store and edit a group of common FPL elements.
    """

    def __init__(self, objects: Iterable[element]):
        # Need to find a method of removing duplicates whilst preserving order.
        self.__objects = list(objects)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ElementGroup):
            raise NotImplementedError

        return other.to_list() == self.to_list()

    def __add__(self, other: ElementGroup[element]) -> ElementGroup[element]:
        if not isinstance(other, ElementGroup):
            raise NotImplementedError

        if not self.is_compatible(other):
            raise Exception("ElementGroups must have same type.")

        return ElementGroup[element](self.to_list() + other.to_list())

    @overload
    def __getitem__(self, idx: SupportsIndex) -> element: ...
    @overload
    def __getitem__(self, idx: slice) -> ElementGroup[element]: ...

    def __getitem__(self, idx: Any) -> Any:
        if isinstance(idx, slice):
            # slicing creates new ElementGroup
            return ElementGroup(self.__objects[idx])
        elif isinstance(idx, SupportsIndex):
            return self.__objects[idx]
        else:
            raise NotImplementedError

    def __iter__(self) -> Iterator[element]:
        return iter(self.__objects)

    def __len__(self) -> int:
        return len(self.__objects)

    def __str__(self) -> str:
        """Description of contents in the class.

        Returns
        -------
        str
            E.g. 'ElementGroup of 10 elements.'
        """
        return f"{self.__class__.__name__} of {len(self)} elements."

    def filter(self, *, method_: Literal["all", "or"] = "all", **attr_to_value: Union[Any, tuple[Any]]) -> ElementGroup[element]:
        """Filters an ElementGroup into a group that satisfies all the conditions passed.

        Parameters
        ----------
        method_ : bool, optional
            "all" if all conditions must be met, "or" for any condition to be met, by default "all"

        Returns
        -------
        ElementGroup[element]
            All elements that satisfy the filters.

        Raises
        ------
        AttributeError
            If the attribute does not exist for the elements.
        """
        # Method check
        func = method_choice(method_)
        attr_to_value = _format_attr_to_value(attr_to_value)

        elements_found = []

        for elem in self:
            conditions_by_attr = []

            for attr, values in attr_to_value.items():
                elem_attr = getattr(elem, attr)

                if isinstance(elem_attr, Element):
                    elem_attr = elem_attr.unique_id

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
        reverse : bool, optional
           For descending order, use True, by default True

        Returns
        -------
        ElementGroup[element]
            Group of top elements of size `n`.
        """
        return ElementGroup[element](self.sort(col_by, reverse=reverse)[:n])

    def get_random(self) -> element:
        """Gets random element from objects list.

        Returns
        -------
        element
            Random element selected.
        """
        return choice(self.__objects)

    def get_sample(self, n: int) -> ElementGroup[element]:
        """Gets `n` random elements from `self`.

        Parameters
        ----------
        n : int
            Length of new element group.

        Returns
        -------
        ElementGroup[element]
            `n` elements from random sample.
        """
        return ElementGroup[element](list(sample(self.__objects, n)))

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

    def is_compatible(self, other: ElementGroup[Any]) -> bool:
        """Checks if two ElementGroups store the same element.

        Parameters
        ----------
        other : ElementGroup
            Other group of elements to compare against.

        Returns
        -------
        bool
            True if they both store the same elements, False otherwise.
        """
        subtypes_found = []

        full_list = self.to_list() + other.to_list()

        for elem in full_list:
            if type(elem) not in subtypes_found:
                subtypes_found.append(type(elem))

                if len(subtypes_found) > 1:
                    return False

        return True

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

        if self.__objects == []:
            return ElementGroup[element](self.__objects)

        elements_sorted = sorted(self.__objects, key=foo, reverse=reverse)

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

    def to_df(self, *attributes: str) -> pd.DataFrame:
        """Gets a list of like elements and puts them into a dataframe.

        With the chosen attributes as columns.

        Returns
        -------
        pd.DataFrame
            `elements` data in a dataframe.
        """

        df_rows = [[getattr(element, attr) for attr in attributes]
                   for element in self]

        df = pd.DataFrame(df_rows, index=list(
            range(1, len(self) + 1)), columns=attributes)

        return df

    def to_list(self) -> list[element]:
        """All elements in instance within a list.

        Returns
        -------
        list[element]
            `self.__object`.
        """
        return self.__objects

    def to_string_list(self) -> list[str]:
        """All elements in instance as their string representation.

        Returns
        -------
        list[str]
            All elements in instance as their string representation.
        """
        output = [str(elem) for elem in self]

        return output
    
    
def id_uniqueness_check(query_result_from_id: ElementGroup[Any]) -> None:
    """Checks if result from ID search produces a valid result.

    Parameters
    ----------
    query_result_from_id : ElementGroup[Any]
        Result from searching for an item by its ID, usually using `cls.get_by_id()`.

    Raises
    ------
    IDNotUnique
        If the query result has more than 1 element.
    IDMatchesZeroElements
        If the query result has 0 elements.
    """
    if len(query_result_from_id) == 1:
        return None

    if len(query_result_from_id) > 1:
        raise IDNotUnique(
            f"Expected only one element, got {len(query_result_from_id)}.")
    if len(query_result_from_id) == 0:
        raise IDMatchesZeroElements("ID matches 0 elements.")
    
    
def method_choice(method_: Literal["all", "or"]) -> Callable[[Iterable[bool]], bool]:
    """Checks if method choice passed from `get` is acceptable.

    Parameters
    ----------
    method_ : str
        Choice of applying conditions. E.g. `all()`,  `any()`.

    Returns
    -------
    Callable[[Iterable[bool]], bool]
        Either `any()` or `all()`.

    Raises
    ------
    Exception
        If a method choice is not recognised.
    """
    METHOD_CHOICES = ["all", "or"]

    if method_ not in METHOD_CHOICES:
        raise Exception(f"method_ must be in {METHOD_CHOICES}")

    if method_ == "all":
        func = all
    else:
        func = any

    return func


def _format_attr_to_value(attr_to_value: dict[str, Union[Any, tuple[Any, ...]]]) -> dict[str, tuple[Any, ...]]:
    """Formats query so the values are all tuples.

    Used by `ElementGroup.filter()`

    Parameters
    ----------
    attr_to_value : dict[str, Union[Any, tuple[Any]]]
        Original query

    Returns
    -------
    dict[str, tuple[Any]]
        Formatted query where values are stored in tuples by default.
    """
    # Attr_to_value check
    for attr, values in attr_to_value.items():
        # If single value for attr is passed
        if isinstance(values, tuple):
            attr_to_value[attr] = list(values)
        else:
            attr_to_value[attr] = [values]

    no_elem_attr_to_value: dict[str, tuple[Any, ...]] = dict()

    for attr, values in attr_to_value.items():
        temp: list[Any] = []

        for value in values:
            if isinstance(value, Element):
                temp.append(value.unique_id)
            else:
                temp.append(value)

        no_elem_attr_to_value[attr] = tuple(temp)

    return no_elem_attr_to_value


def all_attributes_present(class_, new_instance: dict[str, Any]) -> bool:
    """Checks if `new_instance` contains all the attributes of `class_`.

    Parameters
    ----------
    class_ : _type_
        A class with the `@dataclass` decorator.
    new_instance : dict[str, Any]
        Attribute name to the value.

    Returns
    -------
    bool
        True if `new_instance` contains all the necessary attributes of `class_`.
    """
    actual_attr_names = set(all_field_names(class_))
    found_attr_names = set(new_instance.keys())

    if actual_attr_names == found_attr_names:
        return True
    elif actual_attr_names.issubset(found_attr_names):
        return True
    else:  # More values in actual_attr_names
        return False


def all_field_names(class_) -> list[str]:
    """Gets all field names for a given class.

    Parameters
    ----------
    class_ : _type_
        A class with the `@dataclass` decorator.

    Returns
    -------
    list[str]
        All field names for `class_`.
    """
    class_attrs = fields(class_)

    return [attr.name for attr in class_attrs]
