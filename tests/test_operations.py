
import pytest
from calculator import add, subtract, multiply


def test_add():
    assert add(5, 3) == 8


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(5, 3) == 15


@pytest.mark.parametrize("value", [0, -1, 2.5, "5", True, False, None])
def test_invalid_inputs(value):
    with pytest.raises(ValueError):
        add(value, 3)

    with pytest.raises(ValueError):
        subtract(5, value)

    with pytest.raises(ValueError):
        multiply(value, 3)
