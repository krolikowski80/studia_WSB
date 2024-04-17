# 1.Zadania do wykonania na zajęciach
# Uzupełnij brakujące elementy - Wypełnij ____ poniżej, aby uzyskać prawidłowe wartości zmiennych small_cased,
# stripped i stripped_lower_case
# Przydatne metody: .lower(), .strip()
original = " Python strings are COOL! "
lower_cased = original.lower()
stripped = original.strip()
stripped_lower_cased = original.strip().lower()

# Sprawdźmy czy otrzymaliśmy poprawny wynik
assert lower_cased == " python strings are cool! "
assert stripped == "Python strings are COOL!"
assert stripped_lower_cased == "python strings are cool!"


# 2. Prettify - zmodyfikuj podane ciągi wyrazów, aby wyglądały lepiej i zarazem zgadzały się
# z oczekiwanym wynikiem
# Przydatne metody: .title(), .strip()

ugly = " tiTle of MY new Book\n\n"
# Twoja implementacja:
pretty = ugly.strip().title()

# Sprawdźmy czy otrzymaliśmy poprawny wynik
# print(pretty)
assert pretty == "Title Of My New Book"


# 3. Sformatuj ciąg znaków w oparciu o istniejące zmienne Przydatne formatowanie: f""
verb = "is"
language = "Python"
punctuation = "!"

# Twoja implementacja
sentence = f"Learning {language} {verb} fun{punctuation}"

# Sprawdźmy czy otrzymaliśmy poprawny wynik
assert sentence == "Learning Python is fun!"

# 4. Tworzenie formuł
# Napisz następującą formułę matematyczną w Pythonie:
# result =6a^3 - ( (8b^2)/(4c) + 11

a = 2
b = 3
c = 2
# Twoja implementacja:
result = 6*a**3-(8*b**2)/(4*c)+11

# Sprawdźmy czy otrzymaliśmy poprawny wynik
assert result == 50

# 5. Pobieranie danych od użytkownika - wykonaj obliczenia na wprowadzonej przez użytkownika liczbie,
# dla przedstawionego przykładu zakładamy że użytkownik zawsze wprowadza liczbę 20
# Przydatne funkcje: input(), int()

# Twoja implementacja
x = int(input("Podaj liczbę: "))
result = x / 2 + 4
# Sprawdźmy czy otrzymaliśmy poprawny wynik
assert result == 14
