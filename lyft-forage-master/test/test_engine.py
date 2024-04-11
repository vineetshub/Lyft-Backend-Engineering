import unittest
from system import CapuletEngine, SternmanEngine, WilloughbyEngine

class EngineTest(unittest.TestCase):
    def test_capulet_engine_should_be_serviced(self):
        last_service_mileage = 20000
        current_mileage = 40000

        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_capulet_engine_should_not_be_serviced(self):
        last_service_mileage = 30000
        current_mileage = 35000

        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

    def test_sternman_engine_should_be_serviced(self):
        warning_light_on = True

        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_should_not_be_serviced(self):
        warning_light_on = False

        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())

    def test_willoughby_engine_should_be_serviced(self):
        last_service_mileage = 50000
        current_mileage = 80000

        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_should_not_be_serviced(self):
        last_service_mileage = 50000
        current_mileage = 55000

        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
