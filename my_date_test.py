import unittest
import my_date

class MyDateTest(unittest.TestCase):

    def test_is_leap_year1(self):
        self.assertTrue(my_date.is_leap_year(1984))

    def test_is_leap_year2(self):
        self.assertFalse(my_date.is_leap_year(1985))

    # test for ordinal date

    def ordinal_date(self):
        self.assertEqual(172, my_date.ordinal_date(2000, 6, 21))

    
    # test for days elapsed

    def days_elapsed(self):
        self.assertEqual(31, my_date.days_elapsed(1997, 1, 1, 1997, 2, 1))

    def days_elapsed(self):
        self.assertEqual(8408, my_date.days_elapsed(2023, 5, 23, 2000, 5, 10)) 

    def days_elapsed(self):
        self.assertEqual(2201, my_date.days_elapsed(2000, 6, 1, 1994, 5, 21))   

     


    # days of week

    def test_days_week(self):
        self.assertEqual('Friday', my_date.day_of_week(2023,9,29))


    def test_to_str(self):
        self.assertEqual('Friday, 29 September 2023', my_date.to_str(2023,9,29))

    
if __name__ == '__main__':
    unittest.main()