import unittest
from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    #1st iteration fail (no production code yet)
    #2nd iteration pass
    def test_needs_service_true(self):
        tires_sensors = [0, 1, 0, 1]
        tires = CarriganTires(tires_sensors)
        self.assertTrue(tires.needs_service())

    #1st iteration fail (no production code yet)
    #2nd iteration pass
    def test_needs_service_false(self):
        tires_sensors = [0.2, 0.2, 0.5, 0.7]
        tires = CarriganTires(tires_sensors)
        self.assertFalse(tires.needs_service())

