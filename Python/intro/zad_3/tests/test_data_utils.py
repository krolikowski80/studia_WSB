# Importujemy bibliotekę unittest, która pozwala pisać testy jednostkowe
import unittest

# Importujemy nasz moduł data_utils z biblioteki my_awesome_lib
from my_awesome_lib import data_utils

# Tworzymy klasę testową dziedziczącą po unittest.TestCase
# Każda metoda w tej klasie będzie osobnym testem
class TestDataUtils(unittest.TestCase):

    # Testujemy funkcję filter_data z biblioteki
    # Sprawdzamy, czy filtr poprawnie zwraca liczby większe od 3
    def test_filter_data(self):
        data = [1, 2, 3, 4, 5]  # przykładowe dane wejściowe
        result = data_utils.filter_data(data, lambda x: x > 3)  # filtrujemy dane
        self.assertEqual(result, [4, 5])  # sprawdzamy czy wynik jest zgodny z oczekiwanym

# Jeśli uruchamiamy ten plik bezpośrednio, wykonaj wszystkie testy
if __name__ == '__main__':
    unittest.main()