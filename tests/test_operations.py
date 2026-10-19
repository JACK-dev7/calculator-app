
from calculator import add, subtract, multiply


def test_add():
    assert add(1, 3) == 4


def test_subtract():
    assert subtract(3, 3) == 0


def test_multiply():
    assert multiply(6, 3) == 18
