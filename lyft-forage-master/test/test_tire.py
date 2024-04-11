import unittest
from datetime import date
from system.tire import CarriganTire, OctoprimeTire

class TestTireService(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        # Create a Carrigan tire with wear values indicating service is needed
        tire_wear = [0.8, 0.9, 0.95, 0.7]
        tire = CarriganTire(tire_wear)

    
        needs_service = tire.needs_service()

        
        self.assertTrue(needs_service)

    def test_tire_should_not_be_serviced(self):
        # Create an Octoprime tire with wear values indicating no service is needed
        tire_wear = [0.5, 0.3, 0.4, 0.6]
        tire = OctoprimeTire(tire_wear)

      
        needs_service = tire.needs_service()

       
        self.assertFalse(needs_service)

if __name__ == '__main__':
    unittest.main()
