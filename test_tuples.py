def test_tuple():
    a: tuple[int, int, int] = (1, 2, 3)
    assert a[0] == 1

def test_count():
    a: tuple[int, int, int] = (1, 2, 3)
    assert a.count(1) == 1

    b: tuple[int, int, int, int] = (1, 2, 3, 1)
    assert b.count(1) == 2

def test_index():
    a: tuple[int, int, int] = (1, 2, 3)
    assert a.index(1) == 0

    b: tuple[int, int, int, int] = (1, 2, 3, 1)
    assert b.index(1) == 0

    c: tuple[int, int, int, int] = (1, 2, 3, 1)
    assert c.index(1, 1) == 3

    e: tuple[int, int, int, int] = (1, 2, 3, 1)
    assert e.index(1, 1, 4) == 3

    f: tuple[int, int, int, int] = (1, 2, 3, 1)
    assert f.index(1, 1, 5) == 3

def test_len():
    a: tuple[int, int, int] = (1, 2, 3)
    assert len(a) == 3

    b: tuple[int, int, int, int] = (1, 2, 3, 1)
    assert len(b) == 4

def test_in_operator():
    a: tuple[int, int, int] = (1, 2, 3)
    assert 1 in a

    b: tuple[int, int, int, int] = (1, 2, 3, 1)
    assert 1 in b

def test_not_in_operator():
    a: tuple[int, int, int] = (1, 2, 3)
    assert 4 not in a

    b: tuple[int, int, int, int] = (1, 2, 3, 1)
    assert 4 not in b

def test_concatenation():
    a: tuple[int, int, int] = (1, 2, 3)
    b: tuple[int, int, int] = (4, 5, 6)
    assert a + b == (1, 2, 3, 4, 5, 6)

def test_repetition():
    a: tuple[int, int, int] = (1, 2, 3)
    assert a * 2 == (1, 2, 3, 1, 2, 3)

def test_slicing():
    a: tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)
    assert a[1:3] == (2, 3)

    b: tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)
    assert b[1:4] == (2, 3, 4)

    c: tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)
    assert c[1:] == (2, 3, 4, 5)

    d: tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)
    assert d[:3] == (1, 2, 3)

    e: tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)
    assert e[:] == (1, 2, 3, 4, 5)

    f: tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)
    assert f[1:4:2] == (2, 4)

    g: tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)
    assert g[::2] == (1, 3, 5)

    h: tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)
    assert h[::-1] == (5, 4, 3, 2, 1)

def test_unpacking():
    a: tuple[int, int, int] = (1, 2, 3)
    x, y, z = a
    assert x == 1
    assert y == 2
    assert z == 3

def test_unpacking_with_star():
    a: tuple[int, int, int, int] = 1, 2, 3, 4
    x, *y, z = a
    assert x == 1
    assert y == [2, 3]
    assert z == 4

def test_tuple_constructor():
    a = tuple([1,2,3])
    assert a == (1, 2, 3)

    b = tuple()
    assert b == ()

    c = tuple("hello")
    assert c == ('h', 'e', 'l', 'l', 'o')

    d = tuple(range(5))
    assert d == (0, 1, 2, 3, 4)
