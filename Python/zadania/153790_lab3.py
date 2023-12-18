# Tomasz Królikowski
# Numer albumu: 153790
# -------------------------------------------------------------------------------

# Zad 1.
# Utwórz funkcję, która przyjmuje trzy argumenty n, a, b i zwraca listę o długości n, wypełnioną
# losowymi liczbami całkowitymi z zakresu od a do b. Argument n ma mieć wartość domyślną 10,
# argument a wartość domyślną 0 i argument b wartość domyślną 10.
# Przydatne: def, return, random.randrange()

import random


def generate_numbers(n=10, a=0, b=10):
    """generator liczb"""
    return [random.randrange(a, b) for _ in range(n)]


print(generate_numbers())


# -------------------------------------------------------------------------------
# Zad 2.
# Napisz funkcję, która przyjmuje jeden argument n, i wykonuje następujące rzeczy:
# •Utworzy listę liczb losowych z zakresu od 0 do 10 o długości n (można użyć funkcję z poprzedniego zadania).
# •Wypisze na ekran wylosowaną listę.
# •Wypisze na ekran najmniejszą liczbę z listy.
# •Wypisze indeks pod którym znajduje się największa liczba w liście.
# •Wypisze sumę liczb w liście.
# •Wypisze posortowaną listę liczb (przy tym zachowując też wersje nieposortowaną).
# •Wypisze ile razy w liście występuje wartość 3.
# •Wypisze zbiór liczb unikalnych występujących w tej liście.
# Przydatne: print(), max(), min(), index(), sum(), count(), set(), sorted()

from operator import index
import random


def generate_numbers(n, a=0, b=10):
    """generator liczb"""
    nums = [random.randrange(a, b) for _ in range(n)]
    print(f"Oryginalna lista: {nums}")
    print(f"Najmniejsza liczba z listy to: {min(nums)}")
    print(f"Indeks pod którym znajduje się największa liczba w liście {
          nums.index(max(nums))}")
    print(f"Suma liczb w liście to: {sum(nums)}")
    print(f"posortowana lista: {sorted(nums)}")
    print(f"W licie liczba 3 występuje {nums.count(3)} razy")
    print(f"Zbiór liczb unikalnych występujących w tej liście: {set(nums)}")


generate_numbers(5)

# ----------------------------------------------------------------------------
# Zad 3.
# Napisz program, który wygeneruje listę składającą się z 20 całkowitych liczb losowych od -100 do
# 100, a następnie obliczy sumę liczb dodatnich z tej listy,
# korzystając się ze składni list składanych (list comprehension).
# Przydatne: List comprehension, random.randrange()

import random


def randoml_numbers(n):
    """Program generuje listę składającą się z 20 całkowitych liczb losowych od -100 do 100, a następnie obliczy sumę liczb dodatnich z tej listy"""
    nums = [random.randrange(-100, 100) for _ in range(n)]
    print(nums)
    positiv_nums = [x for x in nums if x >= 0]
    print(positiv_nums)
    print(f"Suma liczb dodatnich to: {sum(positiv_nums)}")


randoml_numbers(10)

# ----------------------------------------------------------------
# Zad 4.
# Napisz funkcję, która przyjmuje jeden argument który może być liczbą albo listą liczb. Jeżeli jako
# argument została podana liczba, należy zwrócić tą liczbę pomnożoną razy 2. Jeżeli jako argument
# została podana lista należy utworzyć nową listę, która będzie zawierała elementy pierwotnej listy,
# pomnożone razy 2. Zademonstruj działanie tej funkcji dla liczby i listy losowej
# Przydatne: List comprehension, random.randrange(), isinstance()

def mlt_list(n):
    """Sprawdza czy argumet to lista czy liczba. Mnoży wartości razy dwa"""
    if isinstance(n, int):
        return n*2
    elif isinstance(n, list):
        return [x*2 for x in n]


print(mlt_list([1, 3, 5, 67, 54, 3]))
print(mlt_list(54))

# ----------------------------------------------------------------

# Zad 5.
# Napisz program, który wygeneruje listę składającą się z 50 losowych liczb całkowitych z zakresu
# od 0 do 10, a następnie wyświetli 5 najczęściej spotykanych liczb.
# Do wykonania zadania należy użyć funkcji Counter(), z modułu collections.
# Przydatne: collections.Counter(), most_common(), random.randrange()

from collections import Counter
import random


def nums_generator(n):
    """5 Najczęściej spotykanych liczb"""
    nums = [random.randint(0, 10) for _ in range(n)]
    counter = Counter(nums)
    # print(nums)
    # print(counter)
    for k, v in counter.most_common(5):
        print(f"Liczba {k} wystąpiła {v} razy")


nums_generator(50)

# ----------------------------------------------------------------

# zad 6.
# Zastosuj funkcje z modułu itertools, żeby wypisać na ekran permutacje i kombinacje trzysymbolowe,
# które można złożyć z liter napisu podanego przez użytkownika.
# Przydatne: itertools.permutations(), itertools.combinations(), input()

from itertools import permutations, combinations


def perm_com(word):
    """permutacje i kombinacje trzysybolowe z podanego przez użytkownika wyrazu"""
    perm = list(permutations(word, 2))
    print("Permutacje :", end=" ")
    for val in perm:
        print("".join(val), end=" ")
    comb = list(combinations(word, 2))
    print("\nKombinacje :", end=" ")

    for val in comb:
        print("".join(val), end=" ")


word = input("Wpisz jakieś wyraz: ")
print(perm_com(word))

----------------------------------------------------------------

# zad 7
#Zaimplementuj funkcję służąca do obliczenia wyznacznika macierzy kwadratowych o rozmiarze
# Macierz powinna być jedynym argumentem tej funkcji. W razie podania macierzy o złych
# wymiarach należy wyrzucić wyjątek ValueError z odpowiednią informacją.
# Przydatne: def, return, if, else, raise, ValueError()
# Macierz:
# a = [[1, 2], [3, 4]]
# Wyznacznik: -2


def det(matrix):
    # Sprawdzenie, czy macierz jest kwadratowa
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        raise ValueError("Macierz nie jest kwadratowa")

    # Obsługa macierzy 2x2
    if rows == 2 and cols == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Obliczanie wyznacznika dla macierzy większych niż 2x2
    determinant = 0
    for c in range(cols):
        determinant += ((-1) ** c) * matrix[0][c] * det(minor(matrix, 0, c))

    return determinant


def minor(matrix, row, col):
    # Tworzenie macierzy minor dla danego wiersza i kolumny
    return [row[:col] + row[col + 1 :] for row in (matrix[:row] + matrix[row + 1 :])]


# Przykładowe macierze
a = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]

b = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [6, 3, 4, 5, 6],
    [3, 7, 9, 7, 6],
    [9, 8, 5, 6, 7],
]

# Obliczenie wyznacznika
result = det(a)
print("Wyznacznik:", result)

result_2 = det(b)
print("Wyznacznik:", result_2)

# --------------------------------------------------------------

# zad. 8
# Wczytaj plik points.txt, który zawiera współrzędne 100 punktów położonych w przestrzeni
# dwuwymiarowej (jeden wiersz - jeden punkt, współrzędne x i y są oddzielone od siebie spa-
# cjami). Pobierz od użytkownika dwie liczby będącymi współrzędnymi x, y kolejnego punktu.
# Następnie, wypisz na ekran współrzędne 10 punktów które są położone najbliżej tego wczyta-
# nego od użytkownika punktu.
# Przydatne: with, open(), read(), write(), math.dist()

import math

# Wczytanie współrzędnych punktów z pliku points.txt
with open("Python/zadania/points.txt", "r") as file:
    lines = file.readlines()

# Konwersja wczytanych danych na listę punktów (x, y)
points = []
for line in lines:
    coordinates = line.split()  # Podział linii na współrzędne
    x = float(coordinates[0])  # Konwersja współrzędnej x na float
    y = float(coordinates[1])  # Konwersja współrzędnej y na float
    points.append((x, y))  # Dodanie punktu do listy

# Pobranie współrzędnych punktu od użytkownika
user_x, user_y = map(float, input("Podaj współrzędne punktu (x y): ").split())

# Obliczenie odległości między punktem użytkownika a każdym punktem z pliku
distances = []
for point in points:
    distance = math.dist((user_x, user_y), point)  # Obliczenie odległości
    distances.append(distance)  # Dodanie odległości do listy

# Znalezienie 10 najbliższych punktów
closest_points = sorted(zip(distances, points))[
    :10
]  # Posortowanie i wybranie 10 najbliższych

# Wyświetlenie współrzędnych 10 najbliższych punktów
print("10 punktów najbliżej podanego przez uzyszkodnika punktu:")
for distance, point in closest_points:
    print(f"Współrzędne: {point}, Odległość: {distance}")

# -----------------------------------------------------------------------

# Zad. 9
# Napisz funkcję, która służy do rozwiązywania równań kwadratowych przyjmującą trzy argu-
# menty, będące współczynnikami równania. Do obliczenia pierwiastka z delty należy użyć funkcji
# math.sqrt(). Proszę nie używać warunków dla sprawdzenia czy delta jest ujemna, a
# wyjątek wyrzucany przez funkcje math.sqrt() przechwycić poza funkcją.
# Następnie, napisz program który wczytuje zawartość pliku equations.txt (jeden wiersz - jedno
# równanie, trzy współczynniki oddzielone spacjami). Użyj wcześniej zaimplementowanej funkcji
# do rozwiązywania 50 równań znajdujących się we wczytanym pliku. Znalezione pierwiastki na-
# leży zapisać w nowym pliku pod nazwą equations_results.txt w formacie: jeden wiersz - dwa
# pierwiastki jednego równania, oddzielone spacjami, jeżeli równanie nie ma pierwiastków rzeczy-
# wistych należy zostawić w pliku wiersz pusty. Proszę również pamiętać, że jeżeli funkcja została
# zaimplementowana zgodnie z wymaganiami będzie ona wyrzucać wyjątek, który należy odpo-
# wiednio obsłużyć.
# Przydatne: with, open(), read(), splitlines(), write(), math.sqrt(), try, expect
import math


# Funkcja do rozwiązywania równań kwadratowych
def solve_quadratic_equation(a, b, c):
    delta = b**2 - 4 * a * c  # Obliczenie delty
    if delta < 0:
        raise ValueError(
            "Delta jest mniejsza od zera"
        )  # Wyrzucenie wyjątku dla delty ujemnej

    sqrt_delta = math.sqrt(delta)  # Obliczenie pierwiastka z delty
    x1 = (-b + sqrt_delta) / (2 * a)  # Pierwszy pierwiastek
    x2 = (-b - sqrt_delta) / (2 * a)  # Drugi pierwiastek
    return x1, x2  # Zwrócenie obliczonych pierwiastków


# Wczytanie równań z pliku i rozwiązanie ich
with open(
    "/Users/tomasz/local_repo/studia_WSB/Python/zajecia/lab3_pliki/equations.txt", "r"
) as file:
    equations = file.read().splitlines()  # Wczytanie równań z pliku

results = []
for equation in equations:
    try:
        a, b, c = map(float, equation.split())  # Rozdzielenie współczynników równania
        x1, x2 = solve_quadratic_equation(a, b, c)  # Rozwiązanie równania
        results.append(f"{x1} {x2}")  # Dodanie znalezionych pierwiastków do wyników
    except ValueError as e:
        results.append(
            ""
        )  # Dodanie pustego wiersza, jeśli równanie nie ma pierwiastków rzeczywistych

# Zapisanie wyników do pliku equations_results.txt
with open(
    "/Users/tomasz/local_repo/studia_WSB/Python/zajecia/lab3_pliki/equations_results.txt",
    "w",
) as file:
    file.write("\n".join(results))  # Zapisanie wyników do pliku


# ----------------------------------------------------------------------

# Zad 10
# Zaimplementuj funkcję, sprawdzającą czy liczba n podana jako argument jest liczbą pierwszą.
# Funkcja ma sprawdzać, czy liczba podana jako argument jest podzielna na potencjalne dzielniki
# tej liczby. Implementacja ma wykorzystywać następujące usprawnienia:
# •liczba 1 i wszystkie liczby ujemne nie są pierwsze,
# •liczby parzyste większe od 2 mogą być wyeliminowane od razu,
# •dla pozostałych liczb wystarczy sprawdzić ich podzielność na liczby nieparzyste od 3 do √n
# (włącznie!).
# Następnie, napisz program, który znajdzie które z pierwszych 30 liczb ciągu Fibonacciego są też
# liczbami pierwszymi. Liczby z ciągu Fibonacciego mogą być generowane w dowolny sposób.
# Przydatne: math.sqrt(), range()

import math

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2):
        return False  # 1, liczby ujemne oraz parzyste większe od 2 nie są liczbami pierwszymi

    # Sprawdzenie podzielności na liczby nieparzyste od 3 do pierwiastka z n
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False  # Jeśli n jest podzielne przez i, nie jest liczbą pierwszą

    return True  # Jeśli nie znaleziono dzielników, n jest liczbą pierwszą

# Znalezienie liczb pierwszych w pierwszych 30 liczbach ciągu Fibonacciego
def generate_fibonacci_primes(limit):
    fibonacci = [0, 1]  # Pierwsze dwie liczby ciągu
    primes = []

    for i in range(2, limit):
        next_num = fibonacci[-1] + fibonacci[-2]  # Wygenerowanie kolejnej liczby ciągu
        fibonacci.append(next_num)

        if is_prime(next_num):  # Sprawdzenie czy liczba jest pierwsza
            primes.append(next_num)

    return primes

# Znalezienie pierwszych 30 liczb pierwszych z ciągu Fibonacciego
fibonacci_primes = generate_fibonacci_primes(30)
print("Pierwsze 30 liczb pierwszych z ciągu Fibonacciego:", fibonacci_primes)


# --------------------------------------------------------

# Zad 11
# Zaimplementuj generator, używającą słowo kluczowe yield która będzie służyć do generowania
# kolejnych wyrazów ciągu Collatz’a zaczynając od podanej jako argument funkcji liczby n do 1.
# Przy implementacji nie używamy rekurencji! Ciąg Collatz’a jest zdefiniowany następują-
# cym wzorem:

# C_n+1 = 1/2C_n -> gdy cnjest parzysta; 3C_n + 1

# Przydatne: yield
# Przykładowe wywołanie funkcji-generatora:
# 1 >>> for i in collatz(13):
# 2 ... print(i, end=" -> " if i != 1 else "\n")
# 3 ...
# 4 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

def collatz(n):
    while n != 1:  # Wykonuj, dopóki n nie jest równy 1
        yield n  # Zwróć aktualną wartość n
        if n % 2 == 0:
            n = n // 2  # Jeśli n jest parzyste, n = n / 2
        else:
            n = 3 * n + 1  # Jeśli n jest nieparzyste, n = 3n + 1

    yield n  # Zwróć 1, końcową wartość ciągu

# Przykładowe wywołanie funkcji-generatora
for i in collatz(13):
    print(i, end=" -> " if i != 1 else "\n")

# ------------------------------------------------------------
# Zad 12.
# Wczytaj plik cars.csv, który zawiera w kolejnych wierszach dane o samochodach w postaci produ-
# cent, model, rok, cena, oddzielone przycinkami. Należy wczytać te dane do struktury listy krotek
# (list of tuples). Następnie, należy użyć funkcji wbudowanych sorted(), min() z argumentem
# key i wyświetlić:
# •Dane o samochodach, posortowane od najtańszego do najdroższego,
# •Dane o samochodach, posortowane od najnowszego do najstarszego,
# •Dane o najtańszym samochodzie.
# Przydatne: sorted(), min(), lambda, with, open(), read(), splitlines(), split()

# Wczytanie danych z pliku cars.csv do listy krotek
with open(
    "/Users/tomasz/local_repo/studia_WSB/Python/zajecia/lab3_pliki/cars.csv", "r"
) as file:
    lines = file.read().splitlines()  # Odczyt linii z pliku
    data = [
        tuple(line.split(",")) for line in lines
    ]  # Konwersja danych do listy krotek

# Posortowanie danych od najtańszego do najdroższego
sorted_by_price = sorted(data, key=lambda x: float(x[3]))

# Posortowanie danych od najnowszego do najstarszego
sorted_by_year = sorted(data, key=lambda x: int(x[2]), reverse=True)

# Znalezienie najtańszego samochodu
cheapest_car = min(data, key=lambda x: float(x[3]))

# Wyświetlenie posortowanych danych oraz informacji o najtańszym samochodzie
print("Posortowane od najtańszego do najdroższego:")
for car in sorted_by_price:
    print(car)

print("\nPosortowane od najnowszego do najstarszego:")
for car in sorted_by_year:
    print(car)

print("\nNajtańszy samochód:")
print(cheapest_car)
