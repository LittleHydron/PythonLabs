from transport import *


class Car(Transport):
    def __init__(self, license_number: str, mark: str, wheels: int):
        super().__init__(license_number, mark, "car")
        self.wheels = wheels


class Bus(Transport):
    def __init__(self, license_number: str, mark: str, number: int):
        super().__init__(license_number, mark, "bus")
        self.number = number


class Airplane(Transport):
    def __init__(self, license_number: str, mark: str, length_of_wings: int):
        super().__init__(license_number, mark, "airplane")
        self.length_of_wings = length_of_wings


class Trolley(Transport):
    def __init__(self, license_number: str, mark: str, voltage: int):
        super().__init__(license_number, mark, "trolley")
        self.voltage = voltage


class Tramway(Transport):
    def __init__(self, license_number: str, mark: str, looks_like_donald: bool):
        super().__init__(license_number, mark, "tramway")
        self.looks_like_donald = looks_like_donald
