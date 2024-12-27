def test_dictionary():
    a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    assert a['a'] == 1
    assert a['b'] == 2
    assert a['c'] == 3

def test_get():
    a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    assert a.get('a') == 1
    assert a.get('b') == 2
    assert a.get('c') == 3
    assert a.get('d') == None
    assert a.get('d', 4) == 4

def test_keys():
    a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    assert list(a.keys()) == ['a', 'b', 'c']
    assert tuple(a.keys()) == ('a', 'b', 'c')

def test_values():
    a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    assert list(a.values()) == [1, 2, 3]
    assert tuple(a.values()) == (1, 2, 3)

def test_items():
    a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    assert list(a.items()) == [('a', 1), ('b', 2), ('c', 3)]
    assert tuple(a.items()) == (('a', 1), ('b', 2), ('c', 3))

def test_update():
    a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    a.update({'d': 4, 'e': 5})
    assert a == {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

def test_pop():
    a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    assert a.pop('a') == 1 # mutates a
    assert a == {'b': 2, 'c': 3}

def test_setdefault():
    a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    assert a.setdefault('a', 4) == 1
    assert a == {'a': 1, 'b': 2, 'c': 3}
    assert a.setdefault('d', 4) == 4
    assert a == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

def test_clear():
    a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    a.clear()
    assert a == {}

def test_copy():
    a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    b: dict[str, int] = a.copy()
    assert a == b
    assert a is not b

def test_fromkeys():
    a: dict[str, int] = dict.fromkeys(['a', 'b', 'c'], 1)
    assert a == {'a': 1, 'b': 1, 'c': 1}

def test_popitem():
    a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    assert a.popitem() == ('c', 3) # mutates a
    assert a == {'a': 1, 'b': 2}

def test_len():
    a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    assert len(a) == 3

def test_in_operator():
    a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    assert 'a' in a
    assert 'b' in a
    assert 'c' in a

def test_not_in_operator():
    a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    assert 'd' not in a
    assert 'e' not in a
    assert 'f' not in a

def test_del():
    a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    del a['a']
    assert a == {'b': 2, 'c': 3}
