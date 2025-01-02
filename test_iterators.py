from typing import Generator, Iterator


def test_iter():
    l: list[int] = [1, 2, 3, 4, 5]
    li = iter(l)

    for i in range(len(l)):
        assert next(li) == l[i]

    t: tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)
    ti = iter(t)

    for i in range(len(t)):
        assert next(ti) == t[i]

    d: dict[str, int] = {"a": 1, "b": 2, "c": 3}
    di = iter(d)

    for i in range(len(d)):
        assert next(di) == list(d.keys())[i]

    s: str = "abcde"
    si = iter(s)

    for i in range(len(s)):
        assert next(si) == s[i]

    r: range = range(1, 6)
    ri = iter(r)

    for i in range(len(r)):
        assert next(ri) == r[i]

    se: set[int] = {1, 2, 3, 4, 5}
    sei = iter(se)

    for i in range(len(se)):
        assert next(sei) == list(se)[i]

    b: bytes = b"abcde"
    bi = iter(b)

    for i in range(len(b)):
        assert next(bi) == b[i]


def test_next():
    numbers = [1, 2, 3, 4, 5]
    it = iter(numbers)

    assert next(it) == 1
    assert next(it) == 2
    assert next(it) == 3
    assert next(it) == 4
    assert next(it) == 5


def test_convert_object_to_iterator():
    class Fibonacci:
        def __init__(self):
            self.a = 0
            self.b = 1

        def __iter__(self):
            return self

        def __next__(self):
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            return result

    fib = Fibonacci()
    fib_iter = iter(fib)

    assert next(fib_iter) == 0
    assert next(fib_iter) == 1
    assert next(fib_iter) == 1
    assert next(fib_iter) == 2
    assert next(fib_iter) == 3
    assert next(fib_iter) == 5
    assert next(fib_iter) == 8
    assert next(fib_iter) == 13
    assert next(fib_iter) == 21


def test_zip():
    numbers: list[int] = [1, 2, 3, 4, 5]
    letters: list[str] = ["a", "b", "c", "d", "e"]
    zipped: zip[tuple[int, str]] = zip(numbers, letters)
    expected: list[tuple[int, str]] = [(1, "a"), (2, "b"), (3, "c"), (4, "d"), (5, "e")]

    assert list(zipped) == expected


def test_enumerate():
    numbers: list[int] = [1, 2, 3, 4, 5]
    enumerated: enumerate[int] = enumerate(numbers)
    expected: list[tuple[int, int]] = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

    assert list(enumerated) == expected


def test_filter():
    numbers: list[int] = [1, 2, 3, 4, 5]
    filtered: filter[int] = filter(lambda x: x % 2 == 0, numbers)
    expected: list[int] = [2, 4]

    for i, j in zip(filtered, expected):
        assert i == j


def test_map():
    numbers: list[int] = [1, 2, 3, 4, 5]
    mapped: map[int] = map(lambda x: x**2, numbers)
    expected: list[int] = [1, 4, 9, 16, 25]

    for i, j in zip(mapped, expected):
        assert i == j


def test_count():
    from itertools import count

    c: count = count(start=1, step=2)
    assert next(c) == 1
    assert next(c) == 3
    assert next(c) == 5
    assert next(c) == 7
    assert next(c) == 9
    assert next(c) == 11


def test_cycle():
    from itertools import cycle

    c: cycle = cycle("abc")
    assert next(c) == "a"
    assert next(c) == "b"
    assert next(c) == "c"
    assert next(c) == "a"
    assert next(c) == "b"
    assert next(c) == "c"


def test_repeat():
    from itertools import repeat

    r: repeat = repeat(5, times=3)
    assert next(r) == 5
    assert next(r) == 5
    assert next(r) == 5


def test_accumulate():
    from itertools import accumulate

    numbers: list[int] = [1, 2, 3, 4, 5]
    acc: Iterator[int] = accumulate(numbers)
    expected: list[int] = [1, 3, 6, 10, 15]

    for i, j in zip(acc, expected):
        assert i == j


def test_chain():
    from itertools import chain

    numbers: list[int] = [1, 2, 3]
    letters: list[str] = ["a", "b", "c"]
    chained: Iterator[int | str] = chain(numbers, letters)
    expected: list[int | str] = [1, 2, 3, "a", "b", "c"]

    for i, j in zip(chained, expected):
        assert i == j


def test_permutations():
    from itertools import permutations

    numbers: list[int] = [1, 2, 3]
    perms: Iterator[tuple[int, ...]] = permutations(numbers)
    expected: list[tuple[int, int, int]] = [
        (1, 2, 3),
        (1, 3, 2),
        (2, 1, 3),
        (2, 3, 1),
        (3, 1, 2),
        (3, 2, 1),
    ]

    for i, j in zip(perms, expected):
        assert i == j


def test_reversed():
    numbers: list[int] = [1, 2, 3, 4, 5]
    rev: Iterator[int] = reversed(numbers)
    expected: list[int] = [5, 4, 3, 2, 1]

    for i, j in zip(rev, expected):
        assert i == j


def test_generators():
    def fibonacci() -> Generator[int, None, None]:
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    fib: Iterator[int] = fibonacci()
    expected: list[int] = [0, 1, 1, 2, 3, 5, 8, 13, 21]

    for i, j in zip(fib, expected):
        assert i == j
