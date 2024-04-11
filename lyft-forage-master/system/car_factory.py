from datetime import date
from car import Car
from engine import CapuletEngine, WilloughbyEngine
from battery import SpindlerBattery, NubbinBattery
from tire import CarriganTire, OctoprimeTire, TireType

class CarFactory:
    def create_calliope(self, current_date: date, last_service_date: date, tire_wear: list, tire_type: TireType) -> Car:
        engine = CapuletEngine(last_service_date, current_date)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = self.create_tire(tire_wear, tire_type)
        return Car(engine, battery, tire)

    def create_glissade(self, current_date: date, last_service_date: date, tire_wear: list, tire_type: TireType) -> Car:
        engine = CapuletEngine(last_service_date, current_date)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = self.create_tire(tire_wear, tire_type)
        return Car(engine, battery, tire)

    def create_palindrome(self, current_date: date, last_service_date: date, tire_wear: list, tire_type: TireType) -> Car:
        engine = CapuletEngine(last_service_date, current_date)
        battery = NubbinBattery(last_service_date, current_date)
        tire = self.create_tire(tire_wear, tire_type)
        return Car(engine, battery, tire)

    def create_rorschach(self, current_date: date, last_service_date: date, tire_wear: list, tire_type: TireType) -> Car:
        engine = WilloughbyEngine(last_service_date, current_date)
        battery = NubbinBattery(last_service_date, current_date)
        tire = self.create_tire(tire_wear, tire_type)
        return Car(engine, battery, tire)

    def create_thovex(self, current_date: date, last_service_date: date, tire_wear: list, tire_type: TireType) -> Car:
        engine = WilloughbyEngine(last_service_date, current_date)
        battery = NubbinBattery(last_service_date, current_date)
        tire = self.create_tire(tire_wear, tire_type)
        return Car(engine, battery, tire)

    def create_tire(self, tire_wear: list, tire_type: TireType):
        if tire_type == TireType.CARRIGAN:
            return CarriganTire(tire_wear)
        elif tire_type == TireType.OCTOPRIME:
            return OctoprimeTire(tire_wear)
        else:
            raise ValueError("Invalid tire type")
