import unittest
from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    #1st iteration fail (no production code yet)
    #2nd iteration pass
    def test_needs_service_true(self):
        tires_sensors = [0.7, 1, 0.9, 0.8]
        tires = OctoprimeTires(tires_sensors)
        self.assertTrue(tires.needs_service())

    #1st iteration fail (no production code yet)
    #2nd iteration pass
    def test_needs_service_false(self):
        tires_sensors = [0.2, 0.3, 0.6, 1]
        tires = OctoprimeTires(tires_sensors)
        self.assertFalse(tires.needs_service())
