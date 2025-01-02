from test.test_ctypes.test_repr import subclasses
import random
from unittest.mock import MagicMock

def test_divide_by_zero():
    try:
        a = 9
        b = 0
        n = a // b
        print(n)
    except ZeroDivisionError as e:
        assert str(e) == "integer division or modulo by zero"
    else:
        raise AssertionError("Exception not raised")

def test_capture_multiple_errors():
    try:
        random_number = random.choice([True, False])
        if random_number:
            n = int("hola")
            print(n)
        else:
            n = 9 // 0
            print(n)
    except (ValueError, ZeroDivisionError) as e:
        assert (
            str(e) == "invalid literal for int() with base 10: 'hola'" or
            str(e) == "integer division or modulo by zero"
        )
    else:
        raise AssertionError("Exception not raised")

def test_execute_finally():
    fn = MagicMock()
    fn.side_effect = ZeroDivisionError("integer division or modulo by zero")
    try:
        n = fn("arg")
        print(n)
    except Exception as e:
        print(e)
    finally:
        fn.assert_called()
        fn.assert_called_once()
        fn.assert_called_with("arg")


for error in Exception.__subclasses__():
    print(error.__name__)
