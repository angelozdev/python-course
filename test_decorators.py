from typing import Callable, Type


def log(function: Callable) -> Callable:
    def wrapper(self, *args, **kwargs):
        print(
            f"Function {function.__name__} called with args {args} and kwargs {kwargs}"
        )
        return function(self, *args, **kwargs)

    return wrapper


def add_attribute(attr: str, value: str):
    def decorator(cls: Type):
        setattr(cls, attr, value)
        return cls

    return decorator


@add_attribute("custom_attr", "Angelo")
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @log
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"

    @log
    def say_goodbye(self):
        return "Goodbye!"


p = Person("Angelo", 27)
print(p.greet())
print(p.say_goodbye())


def fn(a, b):
    return a + b
