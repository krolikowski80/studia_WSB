# Tomasz Królikowski
# Numer albumu: 153790
# -------------------------------------------------------------------------------

# Zadanie 1.
# Zaimplementować wyszukiwania największej liczby w nieposortowanej liście liczb.
# Przetestować jego działanie i oszacować złożoność obliczeniową tego algorytmu.
# Krótko (1-2 zdania) opisać dlaczego ten algorytm ma taką złożoność obliczeniową

import random




def najwieksza_liczba(lista):
    """
    Wyszukiwanie największej liczby w nieposortowanej liście liczb."""
    if not lista:
        return None
    max_liczba = lista[0]
    for liczba in lista:
        if liczba > max_liczba:
            max_liczba = liczba
    return max_liczba


przypadkowa_lista = [1, 4, 5, 6, 6, 2, 102, 3, 4, 6, 23, 43, 54, 56, 98]
# pzypadkowa_lista = [random.randint(1, 1000) for _ in range(1000)]
print(f"Największa liczba z tej listy to: {
      najwieksza_liczba(przypadkowa_lista)}")

# Złożoność obliczeniowa tego algorytmu wynosi O(n), gdzie n to liczba elementów w liście.
# CZas wyszukiwania jest lniowy, ponieważ trzeba sprawdzić kazdy element listy.

# ----------------------------------------------------------------

# Zadanie 2
# Zaimplementować algorytm sortowania przez wstawianie (insertion sort). Przetestować jego dzia-
# łanie i oszacować złożoność obliczeniową tego algorytmu. Krótko (1-2 zdania) opisać dlaczego ten
# algorytm ma taką złożoność obliczeniową


def insertion_sort(lista):
    """Sortowanie przez wstawianie."""
    for i in range(1, len(lista)):
        klucz = lista[i]
        j = i - 1
        while j >= 0 and klucz < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = klucz
    return lista


lista_liczb = [1, 4, 5, 6, 6, 2, 8, 76, 45, 8, 1]
print(f"Nieposortowana lista: {lista_liczb}")
posortowana = insertion_sort(lista_liczb)
print(f"Posortowana lista: {posortowana}")

# Złożoność obliczeniowa tego algorytmu wynosi O(n^2) w najgorszym przypadku, gdzie n to liczba elementów w liście.
# Działa on poprzez porównywanie każdego elementu z pozostałymi.
# W najgorszym przypadku, kiedy lista jest odwrotnie posortowana lub posortowana tylko częściowo, każdy kolejny element musi być porównywany z każdym poprzednim elementem.

# ----------------------------------------------------------------
# Zadanie 3
# Zaimplementować opisany poniżej algorytm i oszacować jego złożoność obliczeniową.
# Krótko (1-2 zdania) opisać dlaczego ten algorytm ma taką złożoność obliczeniową.
# Algorytm: na wejściu funkcja dostaje dwa ciągi znaków o różnych długościach s1 i s2.
# Algorytm ma zliczyć ile razy w ciągu s1 występują znaki zawierające się w ciągu s2.
# W poniższym przykładzie zliczamy ile samogłosek występuje w zadanym ciągu.


def licz_znaki(s1, s2):
    """Liczy ile razy w ciągu s1 występują znaki zawierające się w ciągu s2"""
    count = 0
    for ch1 in s1:
        count += 1 if ch1 in s2 else 0
    return count


s = input("Wpisz jakieś zdanie a ja policzę ile w nim jest samogłosek: ")
s1 = ''.join(s.split())
s2 = "aeiouy"

print(f'Wynik: {licz_znaki(s1, s2)}')

# ----------------------------------------------------------------
# zadanie 4
# Zaimplementować algorytm obliczający sumę cyfr wprowadzanej przez użytkownika liczby.
# Przykładowo,dla liczby 1234 wynik działania algorytmu ma wynosić 1 + 2 + 3 + 4 = 10.
# Oszacować złożoność obliczeniową tego algorytmu oraz krótko (1-2 zdania) opisać dlaczego ten algorytm ma taką złożoność.Pod
# powiedź : Wykonujemy pętle tyle razy ile jest cyfr w liczbie.
# Jak matematycznie znaleźć liczbę cyfr w liczbie?


def suma_cyfr(num):
    """algorytm obliczający sumę cyfr wprowadzanej przez użytkownika liczby"""
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


input_num = int(input('Podaj liczbę: '))
print(f"Suma cyfr z tej liczby: {suma_cyfr(input_num)}")

# Złożoność obliczeniowa tego algorytmu wynosi O(n), gdzie n to liczba elementów w liście.
# Pętla wykona się tyle razy,ile jest cyfr w liczbie.

# --------------- KONIEC --------------------------------
