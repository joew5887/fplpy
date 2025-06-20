from dataclasses import dataclass
from typing import TypeVar


T_model = TypeVar("T_model", bound="Model")


@dataclass(frozen=True, order=True, kw_only=True)
class Model:
    pass
