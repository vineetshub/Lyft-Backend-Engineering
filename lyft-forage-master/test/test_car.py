import unittest
from datetime import date
from car import Car, CarType
from system.engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from system.battery import SpindlerBattery, NubbinBattery
from system.tire import CarriganTire, OctoprimeTire, TireType

class TestCar(unittest.TestCase):
    def setUp(self):
        self.current_date = date.today()
        self.last_service_date = self.current_date
        self.current_mileage = 50000
        self.last_service_mileage = 45000

    def test_calliope_needs_service(self):
      
        engine = CapuletEngine(self.last_service_date, self.current_date, self.last_service_mileage, self.current_mileage)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        tire_wear = [0.8, 0.9, 0.95, 0.7]
        tire = CarriganTire(tire_wear)
        calliope = Car(CarType.CALLIOPE, engine, battery, tire)

        
        needs_service = calliope.needs_service()

        
        self.assertTrue(needs_service)

    def test_glissade_needs_service(self):
        
        engine = WilloughbyEngine(self.last_service_date, self.current_date, self.last_service_mileage, self.current_mileage)
        battery = NubbinBattery(self.last_service_date, self.current_date)
        tire_wear = [0.7, 0.6, 0.8, 0.9]
        tire = OctoprimeTire(tire_wear)
        glissade = Car(CarType.GLISSADE, engine, battery, tire)

        
        needs_service = glissade.needs_service()

       
        self.assertTrue(needs_service)

    def test_palindrome_needs_service(self):
        
        engine = CapuletEngine(self.last_service_date, self.current_date, self.last_service_mileage, self.current_mileage)
        battery = NubbinBattery(self.last_service_date, self.current_date)
        tire_wear = [0.6, 0.7, 0.8, 0.6]
        tire = CarriganTire(tire_wear)
        palindrome = Car(CarType.PALINDROME, engine, battery, tire)

        
        needs_service = palindrome.needs_service()

        
        self.assertTrue(needs_service)

    def test_rorschach_needs_no_service(self):

        engine = WilloughbyEngine(self.last_service_date, self.current_date, self.last_service_mileage, self.current_mileage)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        tire_wear = [0.3, 0.2, 0.4, 0.5]
        tire = OctoprimeTire(tire_wear)
        rorschach = Car(CarType.RORSCHACH, engine, battery, tire)

       
        needs_service = rorschach.needs_service()

       
        self.assertFalse(needs_service)

    def test_thovex_needs_no_service(self):
       
        engine = SternmanEngine(self.last_service_date, self.current_date, self.last_service_mileage, self.current_mileage)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        tire_wear = [0.3, 0.3, 0.3, 0.3]
        tire = OctoprimeTire(tire_wear)
        thovex = Car(CarType.THOVEX, engine, battery, tire)

      
        needs_service = thovex.needs_service()

       
        self.assertFalse(needs_service)

if __name__ == '__main__':
    unittest.main()
