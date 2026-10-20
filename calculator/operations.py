
def validate_inputs(a, b):
    for value in (a, b):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError("Inputs must be positive integers")


def add(a: int, b: int) -> int:
    validate_inputs(a, b)
    return a + b


def subtract(a: int, b: int) -> int:
    validate_inputs(a, b)
    return a - b


def multiply(a: int, b: int) -> int:
    validate_inputs(a, b)
    return a * b
