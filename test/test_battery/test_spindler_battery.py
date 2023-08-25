import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    #1st iteration pass
    #2nd iteration pass
    def test_needs_service_3years_true_1(self):
        current_date = date.fromisoformat("2023-05-15")
        last_service_date = date.fromisoformat("2020-01-25")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    #1st iteration fail
    #2nd iteration pass
    def test_needs_service_3years_false_1(self):
        current_date = date.fromisoformat("2023-05-15")
        last_service_date = date.fromisoformat("2021-01-10")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())



