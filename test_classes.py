from typing import Self


class Person:
    name: str
    age: int
    is_active: bool = True

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.is_active = True

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

    def say_goodbye(self):
        print("Goodbye!")

    def __str__(self) -> str:
        return f"I'm {self.name}, {self.age} years old"

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age}, is_active={self.is_active})"

    def __len__(self) -> int:
        return self.age

    def __bool__(self) -> bool:
        return self.is_active

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return False

        return (
            self.name == other.name
            and self.age == other.age
            and self.is_active == other.is_active
        )

    def __add__(self, other: Self) -> "Person":
        return Person(f"{self.name} {other.name}", self.age + other.age)

    def active_status(self) -> bool:
        self.is_active = True
        return True

    def deactivate(self) -> bool:
        self.is_active = False
        return True


class Developer(Person):
    def __init__(self, name: str, age: int, programming_language: str):
        super().__init__(name, age)
        self.programming_language = programming_language

    def say_hello(self):
        print(
            f"Hello, my name is {self.name} and I am {self.age} years old and I code in {self.programming_language}"
        )

    def __str__(self) -> str:
        return f"I'm {self.name}, {self.age} years old and I code in {self.programming_language}"

    def __repr__(self) -> str:
        return f"Developer(name={self.name}, age={self.age}, is_active={self.is_active}, programming_language={self.programming_language})"


p = Person("Angelo", 26)
p2 = Person("Ana", 25)
p3 = p + p2
p.say_hello()
p.say_goodbye()
print(p)
print(len(p))
print(repr(p))
print(bool(p))
print(p == p2)
p.active_status()
print(p3)


d = Developer(name="Angelo", age=26, programming_language="Python")
print(d)
