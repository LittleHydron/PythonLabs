from transport import *


class Car(Transport):
    def __init__(self, license_number: str, mark: str, wheels: int):
        super().__init__(license_number, mark, "car")
        self.wheels = wheels

    def __str__(self):
        return super().__str__() + f" wheels: {self.wheels}"


class Bus(Transport):
    def __init__(self, license_number: str, mark: str, number: int):
        super().__init__(license_number, mark, "bus")
        self.number = number

    def __str__(self):
        return super().__str__() + f" number: {self.number}"


class Airplane(Transport):
    def __init__(self, license_number: str, mark: str, length_of_wings: int):
        super().__init__(license_number, mark, "airplane")
        self.length_of_wings = length_of_wings

    def __str__(self):
        return super().__str__() + f" length_of_wings: {self.length_of_wings}"


class Trolley(Transport):
    def __init__(self, license_number: str, mark: str, voltage: int):
        super().__init__(license_number, mark, "trolley")
        self.voltage = voltage

    def __str__(self):
        return super().__str__() + f" voltage: {self.voltage}"


class Tramway(Transport):
    def __init__(self, license_number: str, mark: str, looks_like_donald: bool):
        super().__init__(license_number, mark, "tramway")
        self.looks_like_donald = looks_like_donald

    def __str__(self):
        return super().__str__() + f" Looks like Donald: {self.looks_like_donald}"
