# zadanie_1.py - Korzystanie z dokumentacji Python

# Tworzę dwie listy z liczbami i literami
# Listy te zostaną połączone w pary za pomocą funkcji zip()
# Dokumentacja zip(): https://docs.python.org/3/library/functions.html#zip
import math
list_a = [1, 2, 3]  # Lista liczb
list_b = ['a', 'b', 'c']  # Lista liter
combined = list(zip(list_a, list_b))  # Łączenie list w pary
print("Połączone listy:", combined)  # Wyświetlenie wyniku

# Importuję moduł math do wykonywania operacji matematycznych
# Dokumentacja math: https://docs.python.org/3/library/math.html

# Obliczam pierwiastek kwadratowy z liczby 16
# Funkcja sqrt() zwraca pierwiastek kwadratowy z podanej liczby
print("Pierwiastek kwadratowy z 16:", math.sqrt(16))

# Obsługa błędu za pomocą bloku try-except
# Dokumentacja ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
try:
    # Próbuję przekonwertować napis na liczbę całkowitą
    # To spowoduje błąd ValueError, ponieważ "abc" nie jest liczbą
    num = int("abc")
except ValueError as e:
    # Obsługa wyjątku - wyświetlenie komunikatu o błędzie
    print("Błąd ValueError złapany:", e)

# Program kończy działanie poprawnie, pomimo wystąpienia wyjątku.
# Wyjątek został obsłużony za pomocą bloku try-except