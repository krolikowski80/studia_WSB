import random

# Zadanie 1
# Zaimplementować wzór na obliczenie n-tego wyrazu ciągu Fibonacciego (wzór poniżej) w sposób
# rekurencyjny. W komentarzach proszę podać która implementacja jest lepsza i dlaczego. Która
# implementacja jest bardziej czytelna?
#
# Funkcja rekurencyjna jest bardziej czytelna.
# Wersja iteracyjna wydaje się lepsza, gdyż wywoływanie funkcji w wersji rekurencyjnej będzie
# wymagać od komputera większej ilości pamięci niż wersja iteracyjna
def zadanie_1():
    def fib(n):
        if n < 2:
            return n
        return fib(n-2) + fib(n-1)
    pass
    print([fib(i) for i in range(10)])
    print(fib(7))


# Zadanie 2
# Zaimplementować rekurencyjny alogrytm obliczania silni.
def zadanie_2():
    def factorial(n):
        if n == 0: return 1
        return factorial(n-1) * n
    print(factorial(5))


# Zadanie 3
# Zaimplementować funkcję który obliczy i wypisze kolejne elementy sekwencji Collatza (wzór
# poniżej) używając rekurencji. Algorytm ma wystartować od podawanej jako argument funkcji
# liczby cn i zakończyć działanie po wypisaniu n elementów ciągu.
def zadanie_3():
    def collatz(n, arr):
        arr.append(n)
        if n == 1: return
        x = n // 2 if n % 2 == 0 else 3 * n + 1
        collatz(x, arr)

    arr = []
    collatz(10, arr)
    print(arr)


# Zadanie 4
# Zaimplementować rekurencyjny algorytm szybkiego sortowania (quicksort) i przetestować jego
# działanie
def zadanie_4():
    def quick_sort(low, high, arr):
        if low >= high or low < 0: return
        pivot = partition(low, high, arr)

        quick_sort(low, pivot - 1, arr)
        quick_sort(pivot + 1, high, arr)

    def partition(low, high, arr):
        pivot = arr[high]
        index = low - 1
        for i in range(low, high):
            if arr[i] <= pivot:
                index += 1
                arr[i], arr[index] = arr[index], arr[i]
        index += 1
        arr[index], arr[high] = arr[high], arr[index]
        return index

    arr = [random.randint(0, 10) for _ in range(10)]
    print(arr)
    quick_sort(0,len(arr)-1, arr)
    print(arr)

if __name__ == "__main__":
    zadanie_1()
    zadanie_2()
    zadanie_3()
    zadanie_4()
