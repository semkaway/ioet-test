import unittest
import sys
sys.path.insert(0, '.')
import functions

class TestSchedule(unittest.TestCase):

    def setUp(self):
        self.hours = [{"start": functions.getDateTime('00:01'), "end": functions.getDateTime('09:00'), "wage":"25"},
                {"start": functions.getDateTime('09:01'), "end": functions.getDateTime('18:00'), "wage":"15"},
                {"start": functions.getDateTime('18:01'), "end": functions.getDateTime('23:59'), "wage":"20"}]

    def tearDown(self):
        pass

    def test_countWageForEmployee(self):
        self.assertEqual(functions.countWageForEmployee("", self.hours), "THERE WAS A FORMATTING ERROR IN THE FILE ON THIS LINE")
        self.assertEqual(functions.countWageForEmployee("RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00", self.hours), "The amount to pay RENE is: 215 USD")
        self.assertEqual(functions.countWageForEmployee("ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00", self.hours), "The amount to pay ASTRID is: 85 USD")
        self.assertEqual(functions.countWageForEmployee("NAME=MO08:00-12:00", self.hours), "The amount to pay NAME is: 70 USD")
        self.assertEqual(functions.countWageForEmployee("NAME=FR23:00-01:00", self.hours), "The amount to pay NAME is: 50 USD")
        self.assertEqual(functions.countWageForEmployee("NAME=SU23:00-02:00", self.hours), "The amount to pay NAME is: 75 USD")
        self.assertEqual(functions.countWageForEmployee("LAURA=some text that is incorrect", self.hours), "THERE WAS A FORMATTING ERROR IN THE FILE ON THIS LINE")
        self.assertEqual(functions.countWageForEmployee("ASTRID=MO10:00-12:00ASTRID=MO10:00-12:00", self.hours), "THERE WAS A FORMATTING ERROR IN THE FILE ON THIS LINE")
        self.assertEqual(functions.countWageForEmployee("MICHAEL=SU14-21:00", self.hours), "THERE WAS A FORMATTING ERROR IN THE FILE ON THIS LINE")

if __name__ == '__main__':
    unittest.main()
