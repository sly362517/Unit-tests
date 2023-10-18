import unittest

from Vehicle import *


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('BMW', 'M550D', 2021)
        self.motorcycle = Motorcycle('Yamaha', 'R1', 2018)

    def test_car_is_instance_of_vehicle(self):
        self.assertTrue(isinstance(self.car, Vehicle))  
    def test_four_wheel_car(self):
        self.assertEqual(self.car.num_wheels, 4)  

    def test_two_wheel_motorcycle(self):
        self.assertEqual(self.motorcycle.num_wheels, 2)

    def test_car_speed(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)

    def test_motorcycle_speed(self):
        self.motorcycle.test_drive()
        self.assertEqual(self.motorcycle.speed, 75)

    def test_car_park_mode_after_test_drive(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)

    def test_motorcycle_park_mode_after_test_drive(self):
        self.motorcycle.test_drive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2) 