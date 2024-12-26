import math

def test_addition():
    assert 2 + 2 == 4

def test_subtraction():
    assert 4 - 2 == 2

def test_multiplication():
    assert 2 * 2 == 4

def test_division():
    assert 4 / 2 == 2

def test_modulus():
    assert 4 % 2 == 0

def test_exponentiation():
    assert 2 ** 2 == 4

def test_floor_division():
    assert 5 // 2 == 2

def test_float_division():
    assert 5 / 2 == 2.5

def test_round():
    assert round(2.6) == 3
    assert round(3.4) == 3

def test_abs():
    assert abs(-2) == 2
    assert abs(2) == 2

def test_int():
    assert int(2.5) == 2
    assert int(2.9) == 2

def test_float():
    assert float(2) == 2.0
    assert float(2.5) == 2.5

def test_complex():
    assert complex(real=2, imag=3) == 2 + 3j
    assert complex(real=2) == 2 + 0j

def test_pow():
    assert pow(2, 2) == 4
    assert pow(2, 2, 3) == 1

def test_divmod():
    assert divmod(5, 2) == (2, 1)
    assert divmod(5.5, 2) == (2.0, 1.5)
    assert divmod(5, 2.5) == (2.0, 0.0)

def test_min():
    assert min(1, 2, 3) == 1

def test_max():
    assert max(1, 2, 3) == 3

def test_sqrt():
    assert math.sqrt(4) == 2
    assert math.sqrt(9) == 3

def test_log():
    assert math.log(2, 2) == 1
    assert math.log(4, 2) == 2
    assert math.log(8, 2) == 3
