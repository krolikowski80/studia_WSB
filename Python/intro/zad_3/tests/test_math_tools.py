# Importujemy bibliotekę unittest - służy do tworzenia testów jednostkowych w Pythonie
import unittest
# Importujemy moduł math_tools z naszej biblioteki
from my_awesome_lib import math_tools

# Tworzymy klasę testową dziedziczącą po unittest.TestCase
# W tej klasie będziemy umieszczać testy dla funkcji z modułu math_tools
class TestMathTools(unittest.TestCase):

    # Test funkcji factorial - sprawdzamy, czy silnia z 5 to 120
    def test_factorial(self):
        self.assertEqual(math_tools.factorial(5), 120)

    # Test funkcji mean - sprawdzamy, czy średnia z listy [1, 2, 3, 4] to 2.5
    def test_mean(self):
        self.assertAlmostEqual(math_tools.mean([1, 2, 3, 4]), 2.5)

    # Test funkcji is_prime - sprawdzamy czy liczba 7 jest pierwsza, a 8 nie
    def test_is_prime(self):
        self.assertTrue(math_tools.is_prime(7))
        self.assertFalse(math_tools.is_prime(8))

# Uruchomienie testów, jeśli plik wykonywany bezpośrednio
if __name__ == '__main__':
    unittest.main()