# Importujemy bibliotekę unittest, służącą do pisania testów jednostkowych
import unittest
# Importujemy moduł text_processing z naszej biblioteki
from my_awesome_lib import text_processing

# Klasa testowa dla modułu text_processing
class TestTextProcessing(unittest.TestCase):

    # Testujemy funkcję count_words
    # Sprawdzamy, czy prawidłowo liczy słowa w zdaniu
    def test_count_words(self):
        self.assertEqual(text_processing.count_words("Ala ma kota"), 3)

    # Testujemy funkcję reverse_string
    # Sprawdzamy, czy odwraca tekst poprawnie
    def test_reverse_string(self):
        self.assertEqual(text_processing.reverse_string("abc"), "cba")

    # Testujemy funkcję is_palindrome
    # Sprawdzamy, czy poprawnie wykrywa palindromy
    def test_is_palindrome(self):
        self.assertTrue(text_processing.is_palindrome("kajak"))
        self.assertTrue(text_processing.is_palindrome("Kobyła ma mały bok"))
        self.assertFalse(text_processing.is_palindrome("python"))

# Uruchamiamy testy, jeśli ten plik został wywołany bezpośrednio
if __name__ == '__main__':
    unittest.main()