from typing import Callable


def test_append():
    a: list[int] = [1, 2, 3]
    a.append(4)
    assert a == [1, 2, 3, 4]


def test_extend():
    a: list[int] = [1, 2, 3]
    a.extend([4, 5])
    assert a == [1, 2, 3, 4, 5]


def test_insert():
    a: list[int] = [1, 2, 3]
    a.insert(1, 4)
    assert a == [1, 4, 2, 3]


def test_remove():
    a: list[int] = [1, 2, 3, 4, 5]
    a.remove(
        2
    )  # .remove() removes the first occurrence of the element and modifies the list in place
    assert a == [1, 3, 4, 5]


def test_pop():
    a: list[int] = [1, 2, 3]
    assert (
        a.pop() == 3
    )  # .pop() returns the last element and modifies the list in place
    assert a == [1, 2]


def test_index():
    a: list[int] = [1, 2, 3]
    assert a.index(2) == 1


def test_count():
    a: list[int] = [1, 2, 2, 3, 2]
    assert a.count(2) == 3


def test_sort():
    a: list[int] = [3, 2, 1]
    a.sort()  # .sort modifies the list in place
    assert a == [1, 2, 3]


def test_sort_reverse():
    a: list[int] = [1, 2, 3]
    a.sort(reverse=True)  # .sort(reverse=True) modifies the list in place
    assert a == [3, 2, 1]


def test_reverse():
    a: list[int] = [1, 2, 3]
    a.reverse()  # .reverse() modifies the list in place
    assert a == [3, 2, 1]


def test_copy():
    a: list[int] = [1, 2, 3]
    b: list[int] = a.copy()
    assert a == b
    assert a is not b


def test_clear():
    a: list[int] = [1, 2, 3]
    a.clear()  # .clear() modifies the list in place
    assert a == []


def test_list_comprehension():
    a: list[int] = [i**2 for i in range(1, 4)]
    assert a == [1, 4, 9]


def test_sorted():
    a: list[int] = [3, 2, 1]
    b: list[int] = sorted(a)  # sorted() returns a new list
    assert a == [3, 2, 1]
    assert b == [1, 2, 3]
    assert a is not b


def test_reversed():
    a: list[int] = [1, 2, 3]
    b: list[int] = list(reversed(a))  # reversed() returns an iterator
    assert a == [1, 2, 3]
    assert b == [3, 2, 1]
    assert a is not b


def test_slicing():
    a: list[int] = [1, 2, 3, 4, 5]
    assert a[1:4] == [2, 3, 4]
    assert a[:2] == [1, 2]
    assert a[2:] == [3, 4, 5]
    assert a[::2] == [1, 3, 5]
    assert a[::-1] == [5, 4, 3, 2, 1]


def test_map():
    a: list[int] = [1, 2, 3]
    b: list[int] = list(map(lambda x: x**2, a))
    assert b == [1, 4, 9]


def test_filter():
    a: list[int] = [1, 2, 3]
    filter_by_even: Callable[[int], bool] = lambda x: x % 2 == 0
    b: list[int] = list(filter(filter_by_even, a))
    assert b == [2]
