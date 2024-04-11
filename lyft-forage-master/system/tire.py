from abc import ABC, abstractmethod

class Tire(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class CarriganTire(Tire):
    def __init__(self, tire_wear: list):
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        return any(wear >= 0.9 for wear in self.tire_wear)

class OctoprimeTire(Tire):
    def __init__(self, tire_wear: list):
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        return sum(self.tire_wear) >= 3
