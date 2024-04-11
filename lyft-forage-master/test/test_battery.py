import unittest
from datetime import date
from system import SpindlerBattery, NubbinBattery

class BatteryTest(unittest.TestCase):
    def test_spindler_battery_should_be_serviced(self):
        last_service_date = date(2021, 1, 1)
        current_date = date(2023, 1, 1)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_should_not_be_serviced(self):
        last_service_date = date(2022, 1, 1)
        current_date = date(2023, 1, 1)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    def test_nubbin_battery_should_be_serviced(self):
        last_service_date = date(2019, 1, 1)
        current_date = date(2023, 1, 1)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        last_service_date = date(2022, 1, 1)
        current_date = date(2023, 1, 1)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
