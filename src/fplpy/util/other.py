from typing import Literal, Callable, Iterable, Union, Any


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


def set_dict_values_tuple(constraints: dict[str, Union[Any, tuple[Any, ...]]]) -> dict[str, tuple[Any, ...]]:
    """Formats query so each constraint value is in a tuple, even if it's just on constraint value.
    
    {"foo": 1, "bar": [2, 3]} -> {"foo": (1,), "bar": (2, 3)}

    Used by `ElementGroup.filter()`

    Parameters
    ----------
    constraints : dict[str, Union[Any, tuple[Any]]]
        Original query

    Returns
    -------
    dict[str, tuple[Any]]
        Formatted query where values are stored in tuples by default.
    """
    constraints_tuple: dict[str, tuple[Any, ...]] = dict()

    for attr, values in constraints.items():
        # If tuple is already passed
        if isinstance(values, Iterable):
            constraints_tuple[attr] = tuple(values)
        else:
            constraints_tuple[attr] = (values,)

    return constraints_tuple
