# # Zad 1.
# # Utwórz funkcję, która przyjmuje trzy argumenty n, a, b i zwraca listę o długości n, wypełnioną
# # losowymi liczbami całkowitymi z zakresu od a do b. Argument n ma mieć wartość domyślną 10,
# # argument a wartość domyślną 0 i argument b wartość domyślną 10.
# # Przydatne: def, return, random.randrange()

# import itertools
# import collections
# import math
# import random


# def generate_numbers(n=10, a=0, b=10):
#     """Generator"""
#     return [random.randrange(a, b) for _ in range(n)]


# print(generate_numbers())

# # ----------------------------------------------------------------

# # Zad 2.
# # Napisz funkcję, która przyjmuję jeden argument n, i wykonuje następujące rzeczy:
# # • Utworzy listę liczb losowych z zakresu od 0 do 10 o długości n (można użyć funkcje
# #   z poprzedniego zadania).
# # • Wypisze na ekran wylosowaną listę.
# # • Wypisze na ekran największą liczbę z listy.
# # • Wypisze indeks pod którym znajduje się najmniejsza liczba w liście.
# # • Wypisze sumę liczb w liście.
# # • Wypisze ile razy w liście występuje wartość 5.
# # • Wypisze zbiór liczb unikalnych występujących w tej liście.
# # Przydatne: print(), max(), min(), index(), sum(), count(), set()


# def generate_numbers(n):
#     """Generator i kilka funkcji"""
#     nums = [random.randrange(0, 10) for _ in range(n)]
#     print(nums)
#     print(f"Największa liczba z listy to: {max(nums)}")
#     print(f"Indeks pod którym znajduje się najmniejsza liczba w liście to: {
#           nums.index(min(nums))}")
#     print(f"Suma liczb w liście to: {sum(nums)}")
#     print(f"Wartość 5 występuje: {nums.count(5)} razy")
#     print(f"Zbiór liczb unikalnych w tej liie: {set(nums)}")


# generate_numbers(10)

# # ----------------------------------------------------------------

# # Zad 3.
# # Napisz program, który wygeneruje listę składającą się z 20 całkowitych liczb losowych od -100 do
# # 100, a następnie obliczy sumę liczb dodatnich z tej listy, korzystając się ze składni list składanych
# # (list comprehension).
# # Przydatne: List comprehension, random.randrange()


# def generate_numbers(n):
#     """Losowe liczbys"""
#     nums = [random.randrange(-100, 100) for _ in range(n)]
#     positiv_nums = [x for x in nums if x >= 0]
#     print(nums)
#     print(f"Suma liczb w liście to: {sum(positiv_nums)}")


# generate_numbers(20)

# # ----------------------------------------------------------------

# # Zad 4.
# # Napisz funkcję, która przyjmuje jeden argument który może być liczbą albo listą liczb. Jeżeli jako
# # argument została podana liczba, należy zwrócić tą liczbę pomnożoną razy 2. Jeżeli jako argument
# # została podana lista należy utworzyć nową listę, która będzie zawierała elementy pierwotnej listy,
# # pomnożone razy 2. Zademonstruj działanie tej funkcji dla liczby i listy losowej.
# # Przydatne: List comprehension, random.randrange(), isinstance()


# def generate_numbers(n):
#     """Sprawdza czy lista czy liczba"""
#     if isinstance(n, int):
#         return n*2
#     elif isinstance(n, list):
#         return [x*2 for x in n]


# print(generate_numbers(random.randrange(-100, 100)))
# random_nums = [random.randrange(-100, 100) for _ in range(10)]
# print(f"Wylosowane liczby: {random_nums}")
# print(f"Podwojone wartości z tej listy: {generate_numbers(random_nums)}")

# # ----------------------------------------------------------------

# # Zad 5.
# # Napisz program, który wygeneruje listę składającą się z 50 losowych liczb całkowitych z zakresu
# # od 0 do 10,a następnie wyświetli 5 najczęściej spotykanych liczb. Do wykonania zadania należy
# # użyć funkcji Counter(), z modułu collections.
# # Przydatne: collections.Counter(), most_common(), random.randrange()


# def generate_numbers(n):
#     """5 Najczęściej spotykanych liczb"""
#     nums = [random.randrange(0, 10) for _ in range(n)]
#     counter = collections.Counter(nums)
#     print(f"Wylosowane liczby: {nums}")
#     for key, value in counter.most_common(5):
#         print(f"Liczba {key} wystąpilas: {value} razy")


# generate_numbers(50)

# # # ----------------------------------------------------------------

# # Zad 6.
# # Zastosuj funkcję z modułu itertools, żeby wypisać na ekran permutacje i kombinacje dwusymbolowe,
# # które można złożyć z liter napisu podanego przez użytkownika.
# # Przydatne: itertools.permutations(), itertools.combinations(), input()
# # import itertools


# def perm_com(word):
#     """Permutacj i kombinacje"""
#     per = list(itertools.permutations(word, 2))
#     print("Permutacje :", end=" ")
#     for val in per:
#         print("".join(val), end=" ")
#     comb = list(itertools.combinations(word, 2))
#     print("\nKombinacje :", end=" ")

#     for val in comb:
#         print("".join(val), end=" ")


# word = input("Wpisz jakieś wyraz: ")
# perm_com(word)

# # ----------------------------------------------------------------

# # Zad 7.
# # Utwórz strukturę składającą się z list zagnieżdżonych, która będzie reprezentować macierz
# # (w rozumieniu matematycznym). Następnie, zaimplementuj funkcję, która będzie wykonywała mnożenie
# # macierzy przez wektor pionowy (reprezentowany przez zwykłą listę). W przypadku gdy
# # do funkcji jako drugi argument jest podana macierz (lista zagnieżdżona) zamiast listy, należy
# # wyrzucić wyjątek ValueError w którym będą umieszczone stosowne informacje. Zademonstruj
# # działanie zaimplementowanej funkcji.
# # Przydatne: def, return, for, range(), ValueError()

# def matrix(mtx, vector):
#     """Mnożenie macieży prez wektor"""
#     if isinstance(vector, list) and not any(isinstance(row, list) for row in vector):
#         for row in mtx:
#             result = []
#             row_sum = sum(row[i]*b[i] for i in range(len(vector)))
#             result.append(row_sum)
#             print(result)
#     else:
#         raise ValueError("Podałeś zły wektor")


# # Przykładowa macierz:
# a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # Przykładowy wektor:
# b = [6, 4, 2]

# matrix(a, b)

# # ----------------------------------------------------------------
# # Zad 8.
# # Wczytaj plik points.txt, który zawiera współrzędne 100 punktów położonych w przestrzeni
# # dwuwymiarowej (jeden wiersz - jeden punkt, współrzędne x i y są oddzielone od siebie spacjami).
# # Następnie, wypisz na ekran dwa punkty które są położone najbliżej siebie.
# # Przydatne: with, open(), read(), splitlines(), math.dist(), itertools.combinations()
# import math
# import itertools


# def point_counter(file):
#     with open(file, "r", encoding='utf-8') as f:
#         table = f.read().splitlines()
#         points = [tuple(map(float, line.split())) for line in table]
#         # print(points) #sprawdzam co wyszło

#     distance_min = float('inf')  # Znalezienie float('inf') zajęło mi 2 godziny :/
#     closest = ()
#     for pair in itertools.combinations(points, 2):
#         # print(pair)  # mam wszystkie kombinacje punktów
#         distance = math.dist(pair[0], pair[1])
#         # print(distance)  # mam wszystkie odległości w kombinacjach
#         if distance < distance_min:
#             distance_min = distance
#             closest = pair
#     # print(closest)
#     print(f"Najbliżej siebie są punkty: ")
#     print(f"Punkt 1: {closest[0]}")
#     print(f"Punkt 2: {closest[1]}")
#     print(f"Odległość między nimi: {distance_min}")


# file = 'Python\zajecia\lab3_pliki\points.txt'
# point_counter(file)

# # ----------------------------------------------------------------
# # Zad 9. Napisz funkcję, która służy do rozwiązywania równań kwadratowych przyjmującą trzy argumenty,
# # będące współczynnikami równania. Do obliczenia pierwiastka z delty należy użyć funkcji
# # math.sqrt(). Proszę nie używać warunków dla sprawdzenia czy delta jest ujemna,
# # a wyjątek wyrzucany przez funkcje math.sqrt() przechwycić poza funkcją.
# # ----------------------------------------------------------------
# # Następnie, napisz program który będzie w pętli odpytywać użytkownika o kolejne równania które
# # trzeba rozwiązać (użytkownik ma podawać trzy współczynniki w jednym wierszu, lub podawać
# # kolejne współczynniki w kolejnych wierszach, dane pobierać do momentu wprowadzenia przez
# # użytkownika pustego wierszu). Znalezione pierwiastki należy wypisać na ekran, jeżeli równanie
# # nie ma pierwiastków rzeczywistych, odpowiednio poinformować użytkownika o tym. Proszę również
# # pamiętać, że jeżeli funkcja została zaimplementowana zgodnie z wymaganiami będzie ona
# # wyrzucać wyjątek, który należy odpowiednio obsłużyć.
# # Przydatne: input(), math.sqrt(), try, expect
# import math
# import itertools


# def qudratic(a, b, c):
#     """Quadratic"""

#     delta = b**2 - 4*a*c
#     if delta == 0:
#         x1 = -b/(2*a)
#         return x1, "brak"
#     if delta < 0:
#         raise ValueError(
#             "Delta jest mniejsza od zera, brak pierwiastków rzeczywistych")
#     sqrt_delta = math.sqrt(delta)
#     x1 = (-b - sqrt_delta)/(2*a)
#     x2 = (-b + sqrt_delta)/(2*a)
#     return x1, x2


# def count():
#     while True:
#         print("Podaj wartości a,b,c oddzielone od siebie spacją.")
#         abc = input()
#         if not abc:
#             break
#         try:
#             a, b, c = map(float, abc.split())
#             output = qudratic(a, b, c)
#             print(f"Pierwiastki równania: x1 = {output[0]}, x2 = {output[1]}")
#         except ValueError as e:
#             print(f"Błąd: {e}. Spróbuj ponownie.")


# count()

# # ----------------------------------------------------------------
# Zad 10.
# Zaimplementuj funkcję, która utworzy listę liczb pierwszych do n (n jest argumentem funkcji)
# korzystając z algorytmu sita Eratostenesa. Następnie, napisz program, który wygeneruje za pomocą
# tej funkcji listę liczb pierwszych do 100 i zapisze ją do pliku prime_numbers.txt, zapisując
# po 5 kolejnych liczb pierwszych w każdym wierszu pliku wynikowego/
# Przydatne: with, open(), write()

########################################################################
# Oto kroki algorytmu sito Eratostenesa:
# 1. Tworzenie listy wszystkich liczb naturalnych od 2 do ustalonego limitu.
# 2. Rozpoczęcie od pierwszej liczby z listy (2) i zaznaczenie wszystkich jej wielokrotności
#     (4, 6, 8, ...) jako skreślonych (nie będących liczbami pierwszymi).
# 3. Przejście do kolejnej nieoznaczonej liczby na liście (następnego nie skreślonego),
#     a następnie zaznaczenie wszystkich jej wielokrotności jako skreślonych.
# 4. Powtarzanie kroku 3, aż do momentu osiągnięcia końca listy.
# 5. Pozostawienie na liście jedynie nieoznaczonych liczb, które są liczbami pierwszymi.
#
# Na końcu algorytmu pozostają tylko liczby pierwsze mniejsze od ustalonego limitu.
# Jest to prosty i efektywny sposób znajdowania liczb pierwszych.
# Jego złożoność obliczeniowa zależy od wielkości badanego zakresu, ale w praktyce jest to
# jedna z najszybszych metod znajdowania liczb pierwszych dla niewielkich liczb.
#
########################################################################
