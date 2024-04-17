# Tomasz Królikowski
# Numer albumu: 153790

# zad 1
# Stwórzmy pustą listę
# my_list = []
# #Dodajmy wartości
# my_list.append("Python")
# my_list.append("is ok")
# my_list.append("sometimes")
#
# # Usuńmy 'sometimes'
# my_list.remove("sometimes")
# # Zmieńmy drugi element listy
# my_list[1] = "is neat"
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert my_list == ["Python", "is neat"]
# print(my_list)

# zad 2
# original = ["I", "am", "learning", "hacking", "in"]
# # Twoja implementacja
# modified = original[:3]
# modified.extend(["lists", "in", "Python"])
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert original == ["I", "am", "learning", "hacking", "in"]
# assert modified == ["I", "am", "learning", "lists", "in", "Python"]

# zad 3
# list1 = [6, 12, 5]
# list2 = [6.2, 0, 14, 1]
# list3 = [0.9]
# # Twoja implementacja
# my_list = sorted(list1 + list2 + list3, reverse=True)
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert my_list == [14, 12, 6.2, 6, 5, 1, 0.9, 0]

# słowniki
# zad 1

# first_name = "John"
# last_name = "Doe"
# favorite_hobby = "Python"
# sports_hobby = "gym"
# age = 82
# # Twoja implementacja
# my_dict = {"name": first_name+' '+last_name,
#            "age": age,
#            "hobbies": [favorite_hobby, sports_hobby]
#            }
#
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert my_dict == {"name": "John Doe", "age": 82, "hobbies": ["Python", "gym"]}


# zad 2
# dict1 = dict(key1="This is not that hard", key2="Python is still cool")
# dict2 = {"key1": 123, "special_key": "secret"}
# #
# # # Można również zainicjalizować słownik przez wykorzystanie listy krotek
# dict3 = dict([("key2", 456), ("keyX", "X")])
# #
# # # Twoja implementacja
# my_dict = dict1 | dict2 | dict3
# special_value = my_dict['special_key']
# del my_dict['special_key']
#
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert my_dict == {"key1": 123, "key2": 456, "keyX": "X"}
# assert special_value == "secret"
#
# # Sprawdźmy czy słowniki początkowe nie zostały zmienione
# assert dict1 == {"key1": "This is not that hard", "key2": "Python is still cool"}
# assert dict2 == {"key1": 123, "special_key": "secret"}
# assert dict3 == {"key2": 456, "keyX": "X"}

# Sterowanie przepływem

# zad1
# name = "John Doe"
# if len(name) > 20:
#     print(f'Name "{name}" is more than 20 chars long')
#     length_description = "long"
# elif len(name) > 15:
#     print(f'Name "{name}" is more than 15 chars long')
#     length_description = "semi long"
# elif len(name) > 10:
#     print(f'Name "{name}" is more than 10 chars long')
#     length_description = "semi long"
# elif len(name) in range(8, 10):
#     print(f'Name "{name}" is 8, 9 or 10 chars long')
#     length_description = "semi short"
# else:
#     print(f'Name "{name}" is a short name')
#     length_description = "short"
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert length_description == "semi short"

#
# #zad2
# words = ["PYTHON", "JOHN", "chEEse", "hAm", "DOE", "123"]
# upper_case_words = []
# for i in words:
#     if i.isupper():
#         upper_case_words.append(i)
#
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert upper_case_words == ["PYTHON", "JOHN", "DOE"]


# zad 3
# magic_dict = dict(val1=44, val2="secret value", val3=55.0, val4=1)
# Twoja implementacja
# sum_of_values = 0
# for i in magic_dict.values():
#     if isinstance(i, (float, int)):
#         sum_of_values +=i
#
# #Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert sum_of_values == 100

# zad 4
# numbers = [1, 3, 4, 6, 81, 80, 100, 95]
# # Twoja implementacja
# my_list = []
# for i in numbers:
#     if i % 5 == 0 and i % 2 == 1:
#         my_list.append('five odd')
#     elif i % 5 == 0 and i % 2 == 0:
#         my_list.append('five even')
#     elif i % 2 == 1:
#         my_list.append('odd')
#     elif i  % 2 == 0:
#         my_list.append('even')

# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert my_list == [
#     "odd",
#     "odd",
#     "even",
#     "even",
#     "odd",
#     "five even",
#     "five even",
#     "five odd",
#     ]

# # zad 5
# def count_even_numbers(numbers):
#     count = 0
#     for num in numbers:
#         if num % 2 == 0:
#             count += 1
#     return count
#
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert count_even_numbers([1, 2, 3, 4, 5, 6]) == 3
# assert count_even_numbers([1, 3, 5, 7]) == 0
# assert count_even_numbers([-2, 2, -10, 8]) == 4


# # 2. Znalezienie poszukiwanych osób
# WANTED_PEOPLE = ["John Doe", "Clint Eastwood", "Chuck Norris"]
# # Twoja implementacja
# def find_wanted_people(people_to_check):
#     found = []
#     for name in people_to_check:
#         if name in WANTED_PEOPLE:
#             found.append(name)
#     return found
#
#
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
#
# people_to_check1 = ["Donald Duck", "Clint Eastwood", "John Doe", "Barack Obama"]
# wanted1 = find_wanted_people(people_to_check1)
# assert len(wanted1) == 2
# assert "John Doe" in wanted1
# assert "Clint Eastwood" in wanted1
# people_to_check2 = ["Donald Duck", "Mickey Mouse", "Zorro", "Superman", "Robin Hood"]
# wanted2 = find_wanted_people(people_to_check2)
# assert wanted2 == []


# 3 Liczenie średniej długości słów w zdaniu
# Twoja implementacja
# def average_length_of_words(words):
#     words = words.split(" ")
#     return round(sum(len(w) for w in words) / len(words), 1)
#
#
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert average_length_of_words("only four lett erwo rdss") == 4
# assert average_length_of_words("one two three") == 3.7
# assert average_length_of_words("one two three four") == 3.8
# assert average_length_of_words("") == 0
# print(average_length_of_words("one two three"))


# 4.5 Ogólne
# 1. Napisz program, który pobierze od użytkownika liczbę całkowitą. Jeżeli pobrana liczba jest parzysta,
# należy podnieść ją do kwadratu i wyświetlić wynik tej operacji. Jeżeli liczba jest nieparzysta,
# należy podnieść ją do trzeciej potęgi i wyświetlić wynik tej operacji.

# x = int(input("Podaj liczbę: "))
# def counter (digit):
#     if digit % 2 == 0:
#         return digit ** 2
#     if digit % 2 == 1:
#         return digit ** 3
#
# print(counter(x))

# 2. Napisz program, który używając tylko pętli for i range() wypisze na ekran:
# • Liczby naturalne od 0 do 10 (bez 10),
# • Liczby naturalne od 10 do 20 (z 20),
# • Liczby naturalne od 0 do 20 z krokiem 2,
# • Liczby całkowite od 0 do -10 z krokiem -1.

# for i in range(1,10):
#     print(i)
#
# for i in range(10, 21):
#     print(i)
#
# for i in range(0, 21, 2):
#     print(i)
#
# for i in range(0, -11, -1):
#     print(i)

# 3. Napisz program który będzie pobierał od użytkownika liczby do momentu wprowadzenia liczby
# ujemnej, a następnie wyświetli wszystkie wprowadzone liczby razem (w jednej linii (w postaci
# listy)).

# lista =[]
# while True:
#     x = int(input("Podaj liczbę: "))
#     if x >= 0:
#         lista.append(x)
#     else:
#         print("Podałeś złą liczbę")
#         break
# print(f"Twoja lista liczb to: {lista}")


# 4. Napisz program który znajdzie pozycje (indeks) i wartość największej liczby w liście. Wartości do
# listy mogą być wpisane na sztywno lub pobierane od użytkownika. Proszę nie używać funkcji
# wbudowanych, a wykonać program używając operatorów for i if.
# Przydatne: for, range(), if, elif, else, [], append(), int()
# Zabronione w tym zadaniu: max(), index()

# UWAGA!! - PROSZĘ O FEEDBACK Z TEGO ZADANIA BO MYŚLĘ, ŻE SKOMPLIKOWAŁEM RZECZY PROSTE
# ZMIENNA "LISTA" POWINNA BYĆ W CIELE FUNKCJI - TAK MI SIĘ WYDAJE

# def dodawanie_do_listy(lista):
#     """Dodaje elementy do listy.
#     Wczytuje je od uzyszkodnika
#     """
#     while True:
#         try:
#             x = int(input(
#                 "Podaj liczbę. Jeżeli wpiszesz inny znak, zakończysz dodawanie liczb: "))
#             lista.append(x)
#         except ValueError:
#             print("Zakończono dodawanie liczb.")
#             print(f"Twoja lista liczb to: {LISTA}")
#             break


# def czytanie_listy(lista):
#     """Printuje elementy listy wraz z ich indeksami"""
#     min_licz = None
#     max_licz = None
#     for index, liczba in enumerate(lista):
#         if min_licz is None or min_licz > liczba:
#             min_licz = liczba
#             niski_ind = index
#         if max_licz is None or max_licz < liczba:
#             max_licz = liczba
#             wysoki_ind = index
#     print(f"Najmniejsza liczba to: {min_licz}, a jej index to: {niski_ind}")
#     print(f"Największa liczba to: {max_licz}, a jej index to: {wysoki_ind}")


# LISTA = []
# dodawanie_do_listy(LISTA)
# czytanie_listy(LISTA)

# 5. Napisz program, który sprawdzi czy z trzech podanych przez użytkownika długości odcinków
# można utworzyć trójkąt. Zakładamy że użytkownik będzie wprowadzać tylko liczby dodatnie. (Z
# trzech odcinków można utworzyć trójkąt wtedy i tylko wtedy gdy suma każdych dwóch odcinków
# jest większa trzeciemu odcinkowi).

# # Funkcja do sprawdzania trójkąta prostokątnego
# def czy_trojkat_prostokatny(a, b, c):
#     # Sprawdzamy warunek Pitagorasa
#     if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
#         return True
#     else:
#         return False

# # Pobieranie długości boków od użytkownika
# a = float(input("Podaj długość boku a: "))
# b = float(input("Podaj długość boku b: "))
# c = float(input("Podaj długość boku c: "))

# # Sprawdzenie czy można utworzyć trójkąt prostokątny
# if a > 0 and b > 0 and c > 0:
#     if czy_trojkat_prostokatny(a, b, c):
#         print("Podane długości boków tworzą trójkąt prostokątny.")
#     else:
#         print("Podane długości boków nie tworzą trójkąta prostokątnego.")
# else:
#     print("Podane długości boków muszą być liczbami dodatnimi.")


# 6. Napisz program który pobierze od użytkownika liczbę całkowitą, a następnie obliczy sumę cyfr z których składa się ta liczba. Przykładowo, dla liczby 1234 mamy otrzymać wynik 1 + 2 + 3 + 4 = 10.

# def suma_cyfr(liczba):
#     suma = 0
#     while liczba != 0:
#         suma += liczba % 10
#         liczba //= 10
#     return suma


# liczba = int(input("Podaj liczbę: "))  # zmienna liczba jest typu int
# print(f"Suma cyfr liczby {liczba} wynosi", suma_cyfr(liczba))


# 7. Napisz program, który pobierze od użytkownika napis i w kolejnych linijkach wypisze:
# • długość napisu,
# • trzeci znak napisu,
# • ostatni znak,
# • pierwsze 5 znaków napisu,
# • ostatnie 5 znaków napisu,
# • wszystkie znaki od 3 do 3 od końca znaku (włącznie),
# • znaki o indeksach parzystych,
# • wszystkie znaki napisu w odwrotnej kolejności.
# Zakładamy że zawsze będzie podany napis wystarczającej długości. Do zadania należy użyć
# notacje "slice".
# Przydatne: len(), print(), [start:stop:step]

# wyraz = input("Napisz jakiś wyraz: ")
# # długość napisu
# i = len(wyraz)
# print(i)

# # trzeci znak napisu,
# print(f"trzeci znak napisu to: {wyraz[2]}")

# # ostatni znak
# print(f"Ostatni znak napisu to: {wyraz[-1]}")

# # pierwsze 5 znaków napisu
# print(f"pierwsze 5 znaków napisu to: {wyraz[:5]}")

# # ostatnie 5 znaków napisu
# print(f"ostatnie 5 znaków napisu to: {wyraz[-5:]}")

# # wszystkie znaki od 3 do 3 od końca znaku (włącznie),
# print(f"wszystkie znaki od 3 do 3 od końca znaku (włącznie) to: {wyraz[3:-2]}")

# # znaki o indeksach parzystych
# print(f"znaki o indeksach parzystych to: {wyraz[::2]}")

# # wszystkie znaki napisu w odwrotnej kolejności
# print(f"wszystkie znaki napisu w odwrotnej kolejności to: {wyraz[::-1]}")


# 8. Napisz program, który odwróci elementy w napisie. Napis może być pobierany przez użytkownika, lub wpisany na sztywno. Zadanie należy wykonać bez użycia funkcji reversed i slice’sów, a posługując się pętlą i indeksowaniem. Do zamiany napisu na listę i z powrotem należy użyć funkcji list() i join().
# Przydatne: for, range(), list(), join().
# Zabronione w tym zadaniu: reversed(), [start:stop:step]
# Dane wejściowe: "ala ma kota"
# Wynik: "atok am ala"

# wyraz = input("Jaki wyraz mam przekształcić: ")
# odwrotny = ""

# while wyraz != "":
#     odwrotny += wyraz[-1]
#     wyraz = wyraz[:-1]

# print(odwrotny)


# 9. Napisz program, który pobierze od użytkownika napis (ewentualnie może być wpisany na sztywno), a następnie zamieni litery każdego drugiego słowa na duże litery. Pozostałe słowa mają być napisane małymi literami. Zakładamy że zawsze będą wprowadzone minimum 2 słowa, oddzielone spacjami.
# Przydatne: split(), join(), upper(), lower()
# Przykład
# Dane wejściowe: "Ala ma kota, a Jan psa"
# Wynik: "ala MA kota, A jan PSA"

# zdanie = input("jakie ZDANIE mam NAPISAĆ tak DZIWNIE? : ").split(" ")
# for i, wyraz in enumerate(zdanie):
#     # print(i, wyraz)
#     if i % 2 == 1:
#         zdanie[i] = wyraz.upper()
# print(" ".join(zdanie))


# 10 Napisz program, który obliczy i wyświetli listę, składającą się z N wyrazów ciągu Fibonacciego, zdefiniowanego poniższym wzorem:

# nty = int(input('Ile wyrazów ciągu Fibonacciego chcesz zobaczyć? '))
# dane = [1, 2]

# if nty == 0 or nty == 1:
#     print(f'{dane[nty]}')

# for i in range(2, nty):
#     dane.append(dane[i-1] + dane[i-2])
# print(dane)

# 10.1
# 10. Napisz program, który obliczy i wyświetli listę, składającą się z N wyrazów ciągu rekurencyjnego, zdefiniowanego poniższym wzorem:
# 3, n = 1
# a^2 n−1 − an−1, n > 1
# nty = int(input('Ile wyrazów ciągu rekurencyjnego chcesz zobaczyć? '))
# dane = [3]
# if nty == 0:
#     print("no to nic ;)")
# elif nty == 1:
#     print(dane[nty-1])
# else:
#     for i in range(2, nty+1):
#         dane.append((dane[i-2]**2)-dane[i-2])
#     print(dane)


# 11. Dane są dwie listy, zawierające liczby.
# Należy napisać program, który przeiteruje po obu listach jednocześnie i wyświetli
# w oddzielnych wierszach elementy z obu list, stojące na tej samej pozycji i ich sumę,
# jeżeli te elementy są różne. W przypadku gdy te elementy są jednakowe, należy
# wyświetlić ich iloczyn. Wyjście programu należy sformatować tak jak to jest pokazane
# w przykładzie. Należy użyć funkcji zip() i formatowania napisów. Przydatne: for, zip(),
# if, else  Zabronione w tym zadaniu: range()

# lista_1 = [1, 4, 3, 5, 2]
# lista_2 = [4, 2, 1, 5, 3]
# for i, o in zip(lista_1, lista_2):
#     if i != o:
#         sum = i + o
#         print(f'{i} + {o} = {sum}')
#     else:
#         il = i * o
#         print(f'{i} x {o} = {il}')

# 12. Podana jest lista zawierająca liczby całkowite. Napisz program, który wypisze w kolejnych wierszach
# indeks elementu listy wraz z elementem listy pod tym indeksem, a dodatkowo wypisze
# słowo "kwadrat", jeżeli element pod indeksem i jest równy i2. Proszę użyć funkcji enumerate().
# Przydatne: for, if, else, enumerate()
# Zabronione w tym zadaniu: range()

# list = [1, 9, 4, 49, 16, 36]
# for i, num in enumerate(list):
#     if i**2 == num:
#         print(f"{i} {num} Kwadrat!")
#     else:
#         print(i, num)


# 13. Napisz program, który pobierze od użytkownika napis, a następnie obliczy
# wystąpienia poszczególnych liter w tym napisie, pomijając pozostałe symboli
# (nie uwzględniamy cyfr, spacji, przycinków itd.).
# Do wykonania tego zadania należy posłużyć się słownikiem.
# Przydatne: for, in, , if, else, isalpha()
# Zabronione w tym zadaniu: count()


# def ile_liczb(napis):
#     litery = {}

#     for litera in napis:
#         if litera.isalpha():
#             litera = litera.lower()  # Zamień na małą literę, aby nie rozróżniać wielkości liter
#             if litera in litery:
#                 litery[litera] += 1
#             else:
#                 litery[litera] = 1

#     return litery


# napis = input(
#     "Podaj napis a ja policzę ile razy pojawiła się w nim każda z liter : ")
# wynik = ile_liczb(napis)

# print(f"Wystąpienia poszczególnych liter: {wynik}")
# for litera, ilosc in wynik.items():
#     print(f"{litera}: {ilosc}")


# zad 14 Napisz program, który będzie działał jako prosty kalkulator. Program w pętli ma pobierać od użytkownika wyrażania formatu ab, gdzie a i b są liczbami całkowitymi,
# a znakiem oznaczającym dodawanie, odejmowanie, mnożenie lub dzielenie (+, -, *, /) i wyświetlać wynik tego wyrażenia
# Należy zakończyć działanie programu, jeżeli nie zostanie wprowadzone nic (po prostu wciśnięcieEnter).
# Zakładamy, że zawsze mamy podane 2 liczby i działanie pomiędzy nimi, liczby i działanie są oddzielone spacjami.
# Należy jednak obsłużyć przypadek dzielenia przez zero.
# Przydatne: while, split(), int(), if, elif, else

# def kalkulator(operacja, liczba1, liczba2):
#     if operacja == "+":
#         return liczba1 + liczba2
#     elif operacja == "-":
#         return liczba1 - liczba2
#     elif operacja == "*":
#         return liczba1 * liczba2
#     elif operacja == "/":
#         if liczba2 != 0:
#             return liczba1 / liczba2
#         else:
#             return "Nie można dzielić przez zero"
#     else:
#         return "Nieprawidłowe działanie"


# while True:
#     wyrazenie = input("podaj liczby w formacie 'liczba znak liczba': ")

#     # Sprawdź, czy użytkownik nacisnął Enter, aby zakończyć program
#     if not wyrazenie:
#         print("Koniec programu.")
#         break

#     # Rozdziel wyrażenie na operację, liczby1 i liczby2
#     try:
#         czesc = wyrazenie.split(" ")
#         operacja = czesc[1]
#         liczba1 = int(czesc[0])
#         liczba2 = int(czesc[2])
#     except (ValueError, IndexError):
#         print("Coś tu namieszałeś. Spróbuj ponownie.")
#         continue

#     # Wykonaj obliczenia
#     wynik = kalkulator(operacja, liczba1, liczba2)

#     # Wyświetl wynik pod wprowadzonym wyrażeniem
#     print(wynik)

# zad 15 Napisz funkcję która przyjmuje liczbę x jako jedyny argument i zwraca wartość funkcji
# f(x) = x^2 + 4x − 3 dla podanego argumentu x.
# Przydatne: def, return

# def funkcja_kwadratowa(x):
#     return x**2 + 4*x - 3

# argument = float(input("Podaj wartość x: "))
# wynik = funkcja_kwadratowa(argument)
# print(f"Wartość funkcji dla x = {argument} to: {wynik}")

# zad 16 Napisz funkcję, która przyjmuje jako argument listę liczb całkowitych, tworzy kopie tej listy imodyfikuje jej kopie w następujący sposób:
# • Usuwa wszystkie podzielne przez 3 liczby,
# • Wkleja wartość -1 przed każdą liczbą parzystą.
# Przydatne: def, return Po dokonaniu modyfikacji zmodyfikowana wersja listy ma być zwrócona z funkcji.
# Przy tym funkcję należy napisać tak, żeby lista, podana jako argument została niezmieniona.
# Zademonstruj działanie funkcji na liście liczb losowych z zakresu od 0 do 10.

# import random

# def modyfikuj_liste(lista):
#     lista_kopia = lista.copy()
#     lista_kopia = [x for x in lista_kopia if x % 3 != 0]
#     i = 0
#     while i < len(lista_kopia):
#         if lista_kopia[i] % 2 == 0:
#             lista_kopia.insert(i, -1)
#             i += 2
#         else:
#             i += 1
#     return lista_kopia


# lista_liczb = [random.randint(0, 10) for _ in range(10)]
# print("Oryginalna lista:", lista_liczb)

# zmodyfikowana_lista = modyfikuj_liste(lista_liczb)
# print("Zmodyfikowana lista:", zmodyfikowana_lista)


# 17. Napisz funkcję, która przyjmuje dwie listy a i b o dowolnych długościach jako argumenty i zwraca iloczyn kartezjański elementów tych dwóch list
# w postaci listy krotek (list of tuples). Przydatne:
# for in, def, return, []

# def iloczyn_kartezjanski(a, b):
#     wynik = [(x, y) for x in a for y in b]
#     return wynik

# lista_a = [1, 2, 3, 4, 5]
# lista_b = ['a', 'b', 'c']
# wynik_iloczynu = iloczyn_kartezjanski(lista_a, lista_b)

# print("Lista 1:", lista_a)
# print("Lista 2:", lista_b)
# print("Iloczyn kartezjański:", wynik_iloczynu)


# Zaznajom się ze składnią list składanych (list comprehension), następnie napisz program, który utworzy używając tej składni trzy listy:
# • Lista składająca się z kwadratów liczb naturalnych od 0 do 10.
# • Lista składająca się z kwadratów liczb naturalnych od 0 do 20 pod warunkiem że kwadrattej liczby jest nieparzysty.
# • Lista składająca się z na przemian z kwadratów i sześcianów liczb naturalnych od 0 do 10.
# Jeżeli liczba jest parzysta, to zapisujemy jej kwadrat, inaczej sześcian. Początek listy: [0, 1, 4, 27, 16, 125...
# Przydatne: List comprehension
# Zabronione w tym zadaniu: append(), insert()


# • Lista składająca się z kwadratów liczb naturalnych od 0 do 10.
kwadraty = [x**2 for x in range(11)]

# • Lista składająca się z kwadratów liczb naturalnych od 0 do 20 pod warunkiem że kwadrattej liczby jest nieparzysty.
kwadraty_nieparzyste = [x**2 for x in range(21) if x**2 % 2 != 0]

# • Lista składająca się z na przemian z kwadratów i sześcianów liczb naturalnych od 0 do 10.
kwadraty_i_szesciany = [x**2 if x % 2 == 0 else x**3 for x in range(11)]

# Wyświetlenie wyników
print("Lista kwadratów:", kwadraty)
print("Lista kwadratów nieparzystych:", kwadraty_nieparzyste)
print("Lista na przemian kwadratów i sześcianów:", kwadraty_i_szesciany)
