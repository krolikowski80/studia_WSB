# Zad 1.
# Napisz funkcję, sprawdzającą czy wszystkie otwarte nawiasy w napisie zostały zamknięte prawidłowo.
# Funkcjama wykorzystywać do tego celu stos i obsługiwać dwa typy nawiasów: okrągłe i kwadratowe.

from collections import deque  # Importujemy kolejkę deque z modułu collections


def is_valid(s):
    stack = deque()  # Tworzymy pustą kolejkę deque do przechowywania nawiasów
    # Mapujemy zamykające nawiasy do odpowiadających im otwierających
    mapping = {')': '(', ']': '['}

    # Iterujemy przez każdy znak w napisie
    for char in s:
        # Jeśli znak to otwarty nawias (okrągły lub kwadratowy), dodajemy go do stosu
        if char in ['(', '[']:
            stack.append(char)
        # Jeśli znak to zamykający nawias
        elif char in [')', ']']:
            # Sprawdzamy, czy stos nie jest pusty i czy zamykający nawias pasuje do otwierającego
            if not stack or mapping[char] != stack.pop():
                return False  # Jeśli nawiasy się nie zgadzają, zwracamy False

    # Sprawdzamy, czy stos jest pusty - jeśli tak, to nawiasy są poprawnie zamknięte
    return not stack


# Testujemy funkcję na różnych przypadkach
print(is_valid('(())'))  # Powinno zwrócić True
print(is_valid('([])'))  # Powinno zwrócić True
print(is_valid('((2 + 5) * (2 + 3)) / 2'))  # Powinno zwrócić True
print(is_valid('a = [(3, 5), (2, 5), (2, 9)]'))  # Powinno zwrócić True
print(is_valid('(]()[]'))  # Powinno zwrócić False
print(is_valid('[[((]]))'))  # Powinno zwrócić False

# ----------------------------------------------------------------
# zad 2.
# Zaimplementować algorytm sortowania przez wstawianie używający dwa stosy.
# Algorytm jest opisany na stronie https://eduinf.waw.pl/inf/alg/001_search/0103.php.

from collections import deque


def insertion_sort_with_stacks(arr):
    input_stack = deque(arr)  # Stos wejściowy
    output_stack = deque()  # Pusty stos wyjściowy

    while input_stack:
        value = input_stack.pop()  # Pobieramy wartość z góry stosu wejściowego

        # Szukamy odpowiedniego miejsca dla wartości na stosie wyjściowym
        while output_stack and output_stack[-1] > value:
            # Przesuwamy większe wartości z wyjściowego na wejściowy
            input_stack.append(output_stack.pop())

        # Wstawiamy wartość na odpowiednie miejsce na stosie wyjściowym
        output_stack.append(value)

    # Konwertujemy stos wyjściowy na listę posortowanych wartości
    return list(output_stack)


# Testowanie sortowania przez wstawianie z wykorzystaniem dwóch stosów
data = [12, 5, 7, 3, 10, 2]
sorted_data = insertion_sort_with_stacks(data)
print("Posortowane dane:", sorted_data)

# ----------------------------------------------------------------
# Zad 3
# Napisać funkcje, symulującą działanie placówki „Poczta Polska”. Funkcja ta ma otrzymać na wejściu listę
# krotek, zawierających po kolei imię klienta oraz czy po spędzeniu tego czasu będzie musiał wrócić do okienka
# (by np. wypełnić potwierdzenie nadania i wrócić wysłać list). Funkcja powinna używać kolejki.
# Kolejka powinna być obsługiwana następująco:
# (a) Pobierz osobę na początku kolejki.
# (b) Sprawdź czy osoba musi coś wysłać.
# (c) Jeżeli tak to dopisz na koniec kolejki.
# (d) Jeżeli nie to dopisz do listy osób wychodzących z poczty.

from collections import deque


def obsluga_poczty(klienci):
    kolejka = deque()
    wychodzacy = []

    for klient in klienci:
        kolejka.append(klient)  # Dodajemy klienta na koniec kolejki

    while kolejka:
        obecny_klient = kolejka.popleft()  # Pobieramy klienta z początku kolejki

        imie, wysylka = obecny_klient

        if wysylka:
            # Jeśli klient musi coś wysłać, dodajemy go z powrotem na koniec kolejki
            kolejka.append(obecny_klient)
        else:
            # Dodajemy do listy osób wychodzących z poczty
            wychodzacy.append(imie)

    return wychodzacy


# Przykładowa lista krotek: (imię klienta, czy musi wysłać coś?)
klienci_na_poczcie = [
    ('Adam', True),
    ('Barbara', False),
    ('Czesław', True),
    ('Dorota', True),
    ('Ewa', False)
]

# Wywołanie funkcji symulującej obsługę poczty
osoby_wychodzace = obsluga_poczty(klienci_na_poczcie)
print("Osoby wychodzące z poczty:", osoby_wychodzace)
