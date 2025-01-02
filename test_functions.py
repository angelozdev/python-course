number = float | int


def add(a: int, b: int, /) -> int:
    return a + b


def multiply(a: float, b: float, /) -> float:
    return a * b


def divide(a: number, b: number, /) -> int:
    return int(a // b)


n = divide(9, 6)

print(len(str(n)))
