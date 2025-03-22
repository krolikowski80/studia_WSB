import unittest
from app import (
    is_valid_email,
    is_palindrome,
    rectangle_area,
    filter_even_numbers,
    convert_date_format
)


class TestAppFunctions(unittest.TestCase):

    # Testy funkcji sprawdzającej adres e-mail
    def test_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertTrue(is_valid_email("user.name@domain.co"))
        self.assertFalse(is_valid_email("invalidemail"))
        self.assertFalse(is_valid_email("test@.com"))

    # Testy funkcji sprawdzającej palindrom
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("kajak"))
        self.assertTrue(is_palindrome("Kobyla ma maly bok"))
        self.assertFalse(is_palindrome("Python"))

    # Testy funkcji liczenia pola prostokąta
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(5, 10), 50)
        self.assertEqual(rectangle_area(0, 5), 0)
        with self.assertRaises(ValueError):
            rectangle_area(-2, 4)

    # Testy funkcji filtrowania liczb parzystych
    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(filter_even_numbers([2, 4, 6]), [2, 4, 6])
        self.assertEqual(filter_even_numbers([]), [])

    # Testy funkcji konwersji daty
    def test_convert_date_format(self):
        self.assertEqual(convert_date_format("2024-03-15"), "15.03.2024")
        self.assertEqual(convert_date_format("1999-12-01"), "01.12.1999")
        with self.assertRaises(ValueError):
            convert_date_format("15-03-2024")


if __name__ == '__main__':
    unittest.main()
