# Tomasz Królikowski
# Numer albumu: 153790
# -------------------------------------------------------------------------------

# Zad 1.
# Napisz program, który pobierze od użytkownika liczbę całkowitą. Jeżeli pobrana liczba jest nie-parzysta, należy podnieść ją do potęgi trzeciej i wyświetlić wynik tej operacji.
# Jeżeli liczba jest parzysta, należy podzielić ją przez 2 i wyświetlić wynik tej operacji.

import random
n = int(input('napisz jakąkolwiek liczbę, byle całkowitą: '))
if n % 2 != 0:
    print(f'Liczba jest nieparzysta więc sześcian tej liczby to: {n**3}')
else:
    print(f'Liczba jest parzysta więc połowa tej liczby to: {n/2}')

# -------------------------------------------------------------------------------

# zad 2.
# Napisz program, który używając tylko pętli for i range() wypisze na ekran:
# (a) Liczby naturalne od 0 do 5 (bez 5),
# (b) Liczby naturalne od 5 do 10 (z 10),
# (c) Liczby naturalne od 0 do 10 z krokiem 3,
# (d) Liczby naturalne od 0 do -10 z krokiem -2.
# Przydatne: for, range(), print()

print("Liczby naturalne od 0 do 5 (bez 5):")
for i in range(5):
    print(i, end=" ")
print("\n")

print("Liczby naturalne od 5 do 10 (z 10):")
for i in range(5, 11):
    print(i, end=" ")
print("\n")

print("Liczby naturalne od 0 do 10 z krokiem 3:")
for i in range(0, 11, 3):
    print(i, end=" ")
print("\n")

print("Liczby naturalne od 0 do -10 z krokiem -2:")
for i in range(0, -11, -2):
    print(i, end=" ")
print("\n")

# -------------------------------------------------------------------------------

# zad 3.
# Napisz program który będzie pobierał od użytkownika słowa do momentu wprowadzenia słowa "koniec",
# a następnie wyświetli wszystkie wprowadzone słowa razem (w jednej linii (w postaci listy)).
# Przydatne: while, if, elif, else, [], append(), input()

slowa = []
while True:
    slowo = input("Napisz jakieś wyrazy - wpisz 'koniec' aby zakończyć: ")
    if slowo.lower() == 'koniec':
        break
    else:
        slowa.append(slowo)
print(f"Twoje napisane słowa w jednej linii wyglądają tak: {slowa}")

# -------------------------------------------------------------------------------

# zad 4.
# Napisz program który znajdzie pozycje (indeks) i wartości największej i najmniejszej liczb w liście. Wartości do listy mogą być wpisane na sztywno lub pobierane od użytkownika.
# Proszę nie używać funkcji wbudowanych, a wykonać program używając operatorów for i if.
# Przydatne: for, range(), if, elif, else, [], append(), int()
# Zabronione w tym zadaniu: max(), min(), index()
# ----------------------------------------------------------------------------------
# UWAGA!! - PROSZĘ O FEEDBACK Z TEGO ZADANIA BO MYŚLĘ, ŻE SKOMPLIKOWAŁEM RZECZY PROSTE
# POZA TYM, ZMIENNA "LISTA" POWINNA BYĆ W CIELE FUNKCJI - TAK MI SIĘ WYDAJE.
# MYŚLĘ, ŻE ARGYMENTEM FUNKCI CZYTANIE LISTY POWINNO BYĆ "DODAWANIE DO LISTY"
# RETURN MI JEDNAK NIE ZWRACA TEGO, CO BYM CHCIAŁ ;/
# WPROWADZANE ZMIANY WYSYPUJĄ PROGRAM
# -----------------------------------------------------------------------------------


def dodawanie_do_listy(lista):
    """Dodaje elementy do listy.
    Wczytuje je od uzyszkodnika
    """
    while True:
        try:
            x = int(input(
                "Podaj liczbę. Jeżeli wpiszesz inny znak, zakończysz dodawanie liczb: "))
            lista.append(x)
        except ValueError:
            print("Zakończono dodawanie liczb.")
            print(f"Twoja lista liczb to: {LISTA}")
            break


def czytanie_listy(lista):
    """Printuje elementy listy wraz z ich indeksami"""
    min_licz = None
    max_licz = None
    for index, liczba in enumerate(lista):
        if min_licz is None or min_licz > liczba:
            min_licz = liczba
            niski_ind = index
        if max_licz is None or max_licz < liczba:
            max_licz = liczba
            wysoki_ind = index
    print(f"Najmniejsza liczba to: {min_licz}, a jej index to: {niski_ind}")
    print(f"Największa liczba to: {max_licz}, a jej index to: {wysoki_ind}")


LISTA = []
dodawanie_do_listy(LISTA)
czytanie_listy(LISTA)

# -------------------------------------------------------------------------------

# Zad 5.
# Napisz program, który sprawdzi czy z trzech podanych przez użytkownika długości odcinków
# można utworzyć trójkąt prostokątny. Zakładamy że użytkownik będzie wprowadzać tylko liczby dodatnie.
#  Boki trójkąta prostokątnego spełniają twierdzenie Pitagorasa (a2 + b2 = c2).
# Przydatne: if, elif, else, int(), float()

bok_a = float(input("Podaj długość odcinka A: "))
bok_b = float(input("Podaj długość odcinka B: "))
bok_c = float(input("Podaj długość odcinka C: "))

if bok_a**2 + bok_b**2 == bok_c**2 or bok_a**2+bok_c**2 == bok_b**2 or bok_b**2+bok_c**2 == bok_a**2:
    print(f"Z boków o wymiarach {bok_a}, {bok_b} i {
          bok_c} - można utworzyć trójkąt prostokątny")
else:
    print(f"Z boków o wymiarach {bok_a}, {bok_b} i {
          bok_c} - niemożna utworzyć trójkąta prostokątnego")

# -------------------------------------------------------------------------------

# zad 6
# Napisz program który pobierze od użytkownika liczbę całkowitą,
# a następnie obliczy sumę cyfr z których składa się ta liczba.
# Przykładowo, dla liczby 1234 mamy otrzymać wynik 1 + 2 + 3 + 4 = 10.
# Przydatne: while, //, %


def suma_cyfr(liczba):
    """ZLicza sumę cyfr z podanej liczby"""
    suma = 0
    while liczba != 0:
        suma += liczba % 10
        liczba //= 10
    return suma


liczba = int(input("Podaj liczbę: "))
print(f"Suma cyfr liczby {liczba} wynosi", suma_cyfr(liczba))

# -------------------------------------------------------------------------------

# zad 7.
# Napisz program, który pobierze od użytkownika napis i w kolejnych linijkach wypisze:
# (a) długość napisu,
# (b) czwarty znak napisu,
# (c) przedostatni znak,
# (d) pierwsze 10 znaków napisu,
# (e) wszystkie znaki napisu oprócz ostatnich 5,
# (f) wszystkie znaki od 5 do 5 od końca znaku (włącznie),
# (g) znaki o indeksach parzystych w odwrotnej kolejności,
# Zakładamy że zawsze będzie podany napis wystarczającej długości. Do zadania należy użyć notacje "slice".
# Przydatne: len(), print(), [start:stop:step]

napis = input("Napisz coś: ")

# (a) Długość napisu
print("(a) Długość napisu:", len(napis))

# (b) Czwarty znak napisu
print("(b) Czwarty znak napisu:", napis[3])

# (c) Przedostatni znak
print("(c) Przedostatni znak napisu:", napis[-2])

# (d) Pierwsze 10 znaków napisu
print("(d) Pierwsze 10 znaków napisu:", napis[:10])

# (e) Wszystkie znaki napisu oprócz ostatnich 5
print("(e) Wszystkie znaki napisu oprócz ostatnich 5:", napis[:-5])

# (f) Wszystkie znaki od 5 do 5 od końca (włącznie)
print("(f) Wszystkie znaki od 5 do 5 od końca (włącznie):", napis[4:-4])

# (g) Znaki o indeksach parzystych w odwrotnej kolejności
print("(g) Znaki o indeksach parzystych w odwrotnej kolejności:", napis[::-2])

# -------------------------------------------------------------------------------

# Zad 8.
# Napisz program, który sprawdzi czy napis jest palindromem.
# Napis może być pobierany przez użytkownika, lub wpisany na sztywno.
# Zadanie należy wykonać bez użycia funkcji reversedi slice’sów, a posługując się pętlą i indeksowaniem.
# Do usunięcia spacji można posłużyć się funkcjami split() i join(). P
# alindrom to napis, który czyta się jednakowo z obu stron.
# Przydatne: for, range(), split(), join(), if, elif, else
# Zabronione w tym zadaniu: reversed(), [start:stop:step]


def czy_palindrom(wyraz):
    """Sprawdza czy podany nbapis jest palindromem"""
    wyraz = ''.join(wyraz.split()).lower()
    dlugosc = len(wyraz)
    for i in range(dlugosc // 2):
        if wyraz[i] != wyraz[dlugosc - i - 1]:
            return False
    return True


wpisany = input("Podaj napis do sprawdzenia: ")

if czy_palindrom(wpisany):
    print("To jest palindrom!")
else:
    print("To nie jest palindrom.")

# -------------------------------------------------------------------------------

# zad 9.
# Napisz program, który pobierze od użytkownika napis (ewentualnie może być wpisany na sztywno),
# a następnie w każdym drugim słowie zamieni literę ”a” na dużą literę ”A”. Pozostałe słowa należy
# zmienić tak, żeby zaczynały się z dużej litery. Zakładamy że zawsze będą wprowadzone minimum
# 2 słowa, oddzielone spacjami.
# Przydatne: split(), join(), replace(), capitalize(), title()


def zmien_litery(tekst):
    """Modyfikacja wpisanego tekstu"""
    slowa = tekst.split()
    for i in range(len(slowa)):
        if i % 2 == 1:
            slowa[i] = slowa[i].replace('a', 'A')
        else:
            slowa[i] = slowa[i].capitalize()
    nowy_tekst = ' '.join(slowa)
    return nowy_tekst


wynik = zmien_litery(input("Podaj napis: "))
print("Zmodyfikowany napis:", wynik)

# -------------------------------------------------------------------------------

# zad 10
# Napisz program, który obliczy i wyświetli listę, składającą się z N wyrazów ciągu Fibonacciego, zdefiniowanego poniższym wzorem:
# a_1 = 0
# a_2 = 2
# a_n = a_n-a + a_n-2


def ciag_fibo(n):
    """Oblicza kolejne wyrazy ciągu fibo"""
    wartosci = [0, 2]
    if n == 1:
        return wartosci[0]
    elif n == 2:
        return wartosci[0:1]
    else:
        for i in range(3, n + 1):
            wartosci.append(wartosci[-1] + wartosci[-2])
        return wartosci


# Jakby komuś zachciało się pisać litery albo liczby ujemne alb nierzeczywiste
try:
    ile = int(input("Ile kolejnych wyrazów ciągu chcesz zobaczyć?: "))
    if ile <= 0:
        print("Ej, no nie żartuj ;)")
    else:
        wynik = ciag_fibo(ile)
        print("Oto pierwsze", ile, "wyrazów:", wynik)
except ValueError:
    print("Nie wpisałeś dodatniej liczby całkowitej .")

# -------------------------------------------------------------------------------

# zad 11.
# Dane są dwie listy, zawierające liczby.
# Należy napisać program, który przeiteruje po obu listach jednocześnie
# i wyświetli w oddzielnych wierszach elementy z obu list, stojące na tej samej pozycji
# i ich sumę, jeżeli te elementy są różne. W przypadku gdy te elementy są jednakowe, należy wyświetlić ich iloczyn.
# Wyjście programu należy sformatować tak jak to jest pokazane w przykładzie.
# Należy użyć funkcji zip() i formatowania napisów.
# Przydatne: for, zip(), if, else
# Zabronione w tym zadaniu: range()

list1 = [1, 4, 7, 8, 25, 33]
list2 = [5, 2, 7, 6, 25, 99]

for a, b in zip(list1, list2):
    if a != b:
        print(f"{a} + {b} = {a + b}")
    else:
        print(f"{a} * {b} = {a * b}")

# -------------------------------------------------------------------------------

# zad 12. Podana jest lista zawierająca słowa.
# Napisz program, który wypisze w kolejnych wierszach indeks elementu listy
# wraz ze słowem znajdującym się pod tym indeksem, a dodatkowo wskaże na słowa
# (dopisać strzałkę jak przy przykładzie), w których liczba liter ”a” jest równa indeksu słowa w liście.
# Proszę użyć funkcji enumerate() i count()
# Przydatne: for, if, else, enumerate()
# Zabronione w tym zadaniu: range()


def sprawdzanie_wyrazow(lista_wyrazow):
    """SPrawdza indeks i liczy litery a w tekscie"""
    for index, wyraz in enumerate(lista_wyrazow):
        if wyraz.count('a') == index:
            znak = "<--"
        else:
            znak = ""
        print(f"{index}: {wyraz} {znak}")


lista_wyrazow = ["Jabłko", "Towar", "Python", "aaa", "Cośtam"]
sprawdzanie_wyrazow(lista_wyrazow)

# zad 13. Przyjmij listę składającą się z 10 liczb losowych z przedziału od 0 do 10 (10 nie włączamy), a następnie oblicz wystąpienia poszczególnych liczb w tym napisie.
# Do wykonania tego zadanianależy posłużyć się słownikiem.
# Przydatne: for, in, [], , if, else, randrange()
# Zabronione w tym zadaniu: count()

lista_liczb = [random.randrange(0, 10) for _ in range(10)]
policzone = {}

for number in lista_liczb:
    if number in policzone:
        policzone[number] += 1
    else:
        policzone[number] = 1

for number, count in policzone.items():
    print(f"Liczba {number} występuje {count} razy.")

# -------------------------------------------------------------------------------

# zad 14. Napisz prosty program do manipulacji napisami.
# Program w pętli ma pobierać od użytkownika dane w formacie polecenie jakieś słowa,
# gdzie polecenie będzie jednym z czterech napisów: lower (zamień wszystkie litery na małe),
# upper (zamień wszystkie litery na duże), title (zrób pierwszą literę każdego słowa dużą),
# reverse (odwróć znaki w napisie). W zależności od tego które polecenie będzie podane, należy wyświetlić odpowiednio zmodyfikowaną resztę napisu pobranego od użytkownika.
# Należy zakończyć działanie programu, jeżeli nie zostanie wprowadzone nic (po prostu wciśnięcie Enter). W przypadku podania nieznanego polecenia należy poinformować użytkownika o tym.
# Należy użyć funkcji lower(), upper(), title(), reversed() lub slice’ów.
# Przydatne: split(), upper(), lower(), title(), reversed(), join(), [start:stop:step]


def modyfikator(polecenie, text):
    """Sprawdza wartość 'polecenie' i stosuje odpowiednie modyfikacje do textu w zależności od polecenia."""
    if polecenie == "lower":
        return text.lower()
    elif polecenie == "upper":
        return text.upper()
    elif polecenie == "title":
        return text.title()
    elif polecenie == "reverse":
        return ''.join(reversed(text))
    else:
        print("Nieznane polecenie:", polecenie)
        return text


while True:
    wpisane_slowo = input(
        "Podaj polecenie (lower, upper, title, reverse) i napis (lub Enter, aby zakończyć): ")

    if not wpisane_slowo:
        break

    # Dzięki (maxsplit=1)dzieli wejście na dwie części:
    # pierwszą dla polecenia i drugą dla reszty tekstu.
    pociete = wpisane_slowo.split(maxsplit=1)

    if len(pociete) != 2:
        print("Błędne dane. Podaj polecenie i napis.")
        continue

    polecenie, text = pociete
    zmodyfikowany = modyfikator(polecenie, text)
    print("Zmodyfikowany napis:", zmodyfikowany)

# -------------------------------------------------------------------------------

# zad 15
# Napisz funkcję która przyjmuje liczbę x jako jedyny argument i zwraca wartość funkcji f(x) =x^3 − 3x^2 + 8x − 2 dla podanego argumentu x.
# Przydatne: def, return


def funkcja(x):
    return x**3 - 3*x**2 + 8*x - 2


argument = float(input("Podaj wartość x: "))
wynik = funkcja(argument)
print(f"Wartość funkcji dla x = {argument} to: {wynik}")


# -------------------------------------------------------------------------------

# zad 16.
# Napisz funkcję, która przyjmuje jako argument listę liczb całkowitych, tworzy kopie tej listy i modyfikuje jej kopie w następujący sposób:
# • Usuwa wszystkie podzielne przez 4 liczby,
# • Wkleja wartość -1 przed każdą liczbą nieparzystą.
# Po dokonaniu modyfikacji zmodyfikowana wersja listy ma być zwrócona z funkcji.
# Przy tym funkcję należy napisać tak, żeby lista, podana jako argument została niezmieniona.
# Zademonstruj działanie funkcji na liście liczb losowych z zakresu od 0 do 10.
# Przydatne: def, return, copy(), del, pop(), insert()


def modyfikuj_liste(lista):
    lista_kopia = lista.copy()
    lista_kopia = [x for x in lista_kopia if x % 4 != 0]
    i = 0
    while i < len(lista_kopia):
        if lista_kopia[i] % 2 == 1:
            lista_kopia.insert(i, -1)
            i += 2
        else:
            i += 1
    return lista_kopia


lista_liczb = [random.randint(0, 10) for _ in range(10)]
print("Oryginalna lista:", lista_liczb)

zmodyfikowana_lista = modyfikuj_liste(lista_liczb)
print("Zmodyfikowana lista:", zmodyfikowana_lista)

# -------------------------------------------------------------------------------

# zad 17.
# Napisz funkcję, która przyjmuje napis o dowolnej długości jako jedyny argument
# i zwraca listę napisów będących kombinacjami par symboli,
# z których składa się podany jako argument napis.
# Przydatne: for in, def, return, range(), enumerate()


def kombinator(napis):
    """Funkcja przyjmuje napis jako argument i zwraca listę napisów będących kombinacjami par symboli z tego napisu."""
    kombinacje = []

    for i, znak in enumerate(napis):
        for znak2 in napis[i+1:]:
            kombinacje.append(znak + znak2)

    return kombinacje


tekst = input("WPisz jaki tekst: ")
print(kombinator(tekst))

# -------------------------------------------------------------------------------

# zad 18
# Zaznajom się ze składnią list składanych (list comprehension), następnie napisz program,
# który utworzy używając tej składni trzy listy:
# • Lista składająca się z sześcianów liczb naturalnych od 0 do 10.
# • Lista składająca się z sześcianów liczb naturalnych od 0 do 10 pod warunkiem że sześcian tej liczby jest podzielny przez 3.
# • Lista składająca się z na przemian kwadratów i sześcianów liczb naturalnych od 0 do 10.
# Jeżeli liczba jest podzielna na 3, to zapisujemy jej sześcian, inaczej kwadrat. Początek listy: [0, 1, 4, 27, 16, ...
# Przydatne: List comprehension
# Zabronione w tym zadaniu: append(), insert()

# • Lista składająca się z sześcianów liczb naturalnych od 0 do 10.
szesciany = [x ** 3 for x in range(10)]

# • Lista składająca się z sześcianów liczb naturalnych od 0 do 10 pod warunkiem że sześcian tej liczby jest podzielny przez 3.
szesciany_podzielne = [x ** 3 for x in range(10) if x ** 3 % 3 == 0]

# • Lista składająca się z na przemian kwadratów i sześcianów liczb naturalnych od 0 do 10.
kwadraty_szesciany = [x ** 3 if x % 2 == 1 else x ** 2 for x in range(10)]

# Jeżeli liczba jest podzielna na 3, to zapisujemy jej sześcian, inaczej kwadrat.
podzielne = [x ** 3 if x % 3 == 0 else x ** 2 for x in range(10)]

print(szesciany)
print(szesciany_podzielne)
print(kwadraty_szesciany)
print(podzielne)


# ------ KONIEC -----
