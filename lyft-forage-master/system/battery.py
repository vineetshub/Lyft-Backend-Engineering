from .serviceable import Serviceable
from abc import ABC, abstractmethod

class Battery(Serviceable, ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class SpindlerBattery(Battery):
    SERVICE_INTERVAL_YEARS = 2

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        years_since_last_service = self.current_date.year - self.last_service_date.year
        return years_since_last_service >= self.SERVICE_INTERVAL_YEARS

class NubbinBattery(Battery):
    SERVICE_INTERVAL_YEARS = 4

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        years_since_last_service = self.current_date.year - self.last_service_date.year
        return years_since_last_service >= self.SERVICE_INTERVAL_YEARS
