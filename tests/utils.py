from typing import Any, Callable, Iterable, TypeVar

import pytest

T = TypeVar("T")


def tst_compare(
    obj: T,
    other: T,
    compare: Callable[[Any, Any], bool],
    match_itself: bool,
    illegal: Iterable[tuple[Any, Any]] = (),
) -> None:
    """Test that the object compares correctly to other objects.

    Args:
        obj: The object to test.
        other: Another object to compare the first object to.
        compare: The comparison function to use. `compare(obj, other)` should return True and `compare(other, obj)` should return False.
        match_itself: Whether `compare(obj, obj)` should return True or False.
        illegal: A list of tuples of objects that should raise a TypeError when compared to each other.
    """
    assert compare(obj, other)
    assert not compare(other, obj)
    assert compare(obj, obj) == match_itself
    for a, b in illegal:
        with pytest.raises(TypeError):
            compare(a, b)
