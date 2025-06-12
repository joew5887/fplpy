from typing import Any
from dataclasses import fields

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
