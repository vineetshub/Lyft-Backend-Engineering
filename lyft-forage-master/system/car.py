from engine import Engine
from battery import Battery
from tire import Tire

class Car:
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self) -> bool:
        return any(part.needs_service() for part in [self.engine, self.battery, self.tire])
