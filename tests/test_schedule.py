import unittest
import sys
sys.path.insert(0, '..')
import schedule

class TestSchedule(unittest.TestCase):

    def test_workWithFile(self):
        self.assertEqual(schedule.workWithFile("employees.txt"), "OK")
        self.assertEqual(schedule.workWithFile("employees.doc"), "Incorrect file extention")
        self.assertEqual(schedule.workWithFile("no-such-file.txt"), "Incorrect filename")

if __name__ == '__main__':
    unittest.main()
