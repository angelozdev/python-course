from typing import Union


FactorType = Union[int, float]


class MultiplierFactory:
    factor: FactorType

    def __new__(cls, factor: FactorType) -> "MultiplierFactory":
        print("Creating new instance")
        return super().__new__(cls)

    def __init__(self, factor: FactorType):
        print("Initializing instance")
        self.factor = factor

    def __call__(self, n: FactorType) -> FactorType:
        return n * self.factor


if __name__ == "__main__":
    multiplier = MultiplierFactory(2)
    print(multiplier(10))
