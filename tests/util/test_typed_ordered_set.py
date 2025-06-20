import pytest
from collections.abc import MutableSequence
from typing import TypeVar
from random import choice
from fplpy.util.typed_ordered_set import TypedOrderedSet  # Update this with the actual module

E = TypeVar("E")

@pytest.fixture
def sample_data() -> list[int]:
    return [1, 2, 3]

@pytest.fixture
def set_instance(sample_data: list[int]) -> TypedOrderedSet:
    return TypedOrderedSet(sample_data)

def test_creation(set_instance: TypedOrderedSet) -> None:
    assert isinstance(set_instance, MutableSequence)
    assert len(set_instance) == 3

def test_type_enforcement() -> None:
    with pytest.raises(TypeError):
        TypedOrderedSet(["a", 1])  # Mixed types should fail

def test_uniqueness_enforced() -> None:
    with pytest.raises(ValueError):
        s = TypedOrderedSet([1, 2, 3])
        s.insert(1, 2)  # Inserting duplicate should fail

def test_order_preserved(sample_data: list[int]) -> None:
    s = TypedOrderedSet(sample_data)
    assert s.to_list() == sample_data  # Ensure same order

def test_equality_check() -> None:
    s1 = TypedOrderedSet([1, 2, 3])
    s2 = TypedOrderedSet([1, 2, 3])
    s3 = TypedOrderedSet([3, 2, 1])

    assert s1 == s2  # Exact match
    assert s1 != s3  # Order matters

def test_get_random(set_instance: TypedOrderedSet) -> None:
    assert set_instance.get_random() in set_instance.to_list()  # Should always be a valid element

def test_empty_detection() -> None:
    s = TypedOrderedSet([])
    assert s.is_empty

def test_deletion(set_instance: TypedOrderedSet) -> None:
    del set_instance[1]  # Remove second item
    assert len(set_instance) == 2
    assert set_instance.to_list() == [1, 3]  # Item 2 should be gone

def test_insert() -> None:
    s = TypedOrderedSet([1, 2])
    s.insert(1, 3)
    assert s.to_list() == [1, 3, 2]  # Insert at index 1