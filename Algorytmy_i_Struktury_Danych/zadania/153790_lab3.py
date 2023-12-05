# Zad 1.
# Zaimplementować wzór na obliczenie n-tego wyrazu ciągu Fibonacciego (wzór poniżej) w sposób
# rekurencyjny. W komentarzach proszę podać która implementacja jest lepsza i dlaczego. Która
# implementacja jest bardziej czytelna?

import random
print("\nZadanie 1\n")


def fibonacci_rekurencyjnie(n):
    if n <= 1:
        return n
    else:
        return fibonacci_rekurencyjnie(n - 1) + fibonacci_rekurencyjnie(n - 2)


n = int(input("Podaj, który wyraz ciągi (n) chcesz poznać: "))
print(
    f"Wartość {n}-tego wyrazu ciągu Fibonacciego: {fibonacci_rekurencyjnie(n)}")

# Implementacja rekurencyjna jest prostsza i odzwierciedla bezpośrednio wzór na ciąg Fibonacciego.
# W mojej opinii jest czytelniejsza, wymaga jednak zrozumienia koncepcji wywoływania funkcji samej siebie.
# Jednak dla dużych wartości n, może to prowadzić do wydajnościowej słabości.
# dla n = 122 mój komputer "poddał się i nie obliczył"
#
# Tak to wyglądało:
# PID    COMMAND      %CPU  TIME     #TH    #WQ  #PORT MEM    PURG   CMPRS  PGRP  PPID  STATE    BOOSTS
# 43848  python3.12   98.8  06:07.81 1/1    0    15    5889K  0B     5232K  43848 43326 running  *0[1]


# -------------------------------------------------------------------------------------------------
# Zad 2. Zaimplementować rekurencyjny alogrytm obliczania silni.
print("\nZadanie 2\n")


def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)


n = int(input("Podaj, który wyraz silni (n) chcesz poznać: "))
print(f"Wartość {n}-tego wyrazu silni: {silnia(n)}")


# -----------------------------------------------------------------------------------------
# Zad 3.
# Zaimplementować funkcję który obliczy i wypisze kolejne elementy sekwencji Collatza (wzór
# poniżej) używając rekurencji. Algorytm ma wystartować od podawanej jako argument funkcji
# liczby cn i zakończyć działanie po wypisaniu n elementów
# c_n+1 ={1/2 C_n, gdy C_n jest parzysta ; 3c_n + 1, gdy c_n jest nieparzysta }
print("\nZadanie 3\n")


def collatz_rekurencyjnie(cn, n):
    print(cn)
    if n > 1:
        if cn % 2 == 0:
            collatz_rekurencyjnie(cn // 2, n - 1)
        else:
            collatz_rekurencyjnie(3 * cn + 1, n - 1)


start_value = 10  # Wartość początkowa ciągu Collatza
num_elements = 100  # Liczba elementów do wygenerowania

collatz_rekurencyjnie(start_value, num_elements)

# -------------------------------------------------------------------------
# Zad 4. Zaimplementować rekurencyjny algorytm szybkiego sortowania (quicksort) i przetestować jego działanie.

print("\nZadanie 4\n")


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


# Przykładowa lista do posortowania
lista = [random.randint(1, 100) for _ in range(15)]

print("Przed sortowaniem:", lista)
posortowana_lista = quicksort(lista)
print("Po sortowaniu:", posortowana_lista)
