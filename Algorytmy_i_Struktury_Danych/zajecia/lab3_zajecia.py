# # Zad 1.
# # Zaimplementować wzór na obliczenie n-tego wyrazu ciągu Fibonacciego (wzór poniżej) w sposóbiteracyjny.
# # 0, n = 0
# # 1, n = 1
# # an−2 + an−1, n > 1

# def fibonacci(n):
#     """Obliczanie Fibonacciego w sposób iteracyjny"""
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         a, b = 0, 1
#         for _ in range(2, n+1):
#             c = a + b
#             a, b = b, c
#         return b


# n = int(input("Podaj, który wyraz ciągi (n) chcesz poznać: "))
# print(f"Wartość {n}-tego wyrazu ciągu Fibonacciego: {fibonacci(n)}")

# # #-------------------------------------------------------------------------------------------------
# # Zad 2.

# import random


# def insertion_sort_recursive(arr, n):
#     # Bazowy warunek zakończenia rekurencji - gdy lista ma mniej niż 2 elementy, jest już posortowana
#     if n <= 1:
#         return

#     # Sortowanie rekurencyjne pierwszych n-1 elementów
#     insertion_sort_recursive(arr, n - 1)

#     # Wstawianie ostatniego elementu na odpowiednie miejsce w posortowanej części listy
#     last_element = arr[n - 1]
#     j = n - 2

#     while j >= 0 and arr[j] > last_element:
#         arr[j + 1] = arr[j]
#         j -= 1

#     arr[j + 1] = last_element


# # Przykładowe użycie
# arr_to_sort = [random.randint(1, 1000) for _ in range(15)]
# insertion_sort_recursive(arr_to_sort, len(arr_to_sort))
# print("Posortowana lista:", arr_to_sort)

# # -----------------------------------------------------------------------------------------
# # Zad 3.
# # Zaimplementować rekurencyjny algorytm sortowania przez scalanie (merge sort). Przetestować
# # jego działanie i oszacować złożoność obliczeniową tego algorytmu. Krótko (1-2 zdania) opisać
# # dlaczego ten algorytm ma taką złożoność obliczeniową.
# import random


# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2  # Oblicz środek listy
#         left_half = arr[:mid]  # Podziel listę na dwie części
#         right_half = arr[mid:]

#         # Rekurencyjnie sortuj obie części
#         merge_sort(left_half)
#         merge_sort(right_half)

#         # Scal posortowane części
#         i = j = k = 0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         # Dodaj ewentualne pozostałe elementy
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1
#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1


# # Przykładowe użycie
# arr_to_sort = [random.randint(1, 100) for _ in range(15)]
# merge_sort(arr_to_sort)
# print("Posortowana lista:", arr_to_sort)

# # -------------------------------------------------------------------------
# # Zad 4.
# # Zaimplementować rekurencyjny algorytm rozwiązujący problem wieży Hanoi. Algorytm ma
# # wypisywać kolejne kroki konieczne do przeniesienia N krążków ze słupka A na słupek C. Przykład
# # działania niżej. Jaką złożoność obliczeniową ma ten algorytm (Jaką liczbę kroków musimy
# # wykonać żeby przenieść N krążków)? Uzasadnij odpowiedź.
# # 1 >>> hanoi(3)
# # 2 Move (1) from A to C
# # 3 Move (2) from A to B
# # 4 Move (1) from C to B
# # 5 Move (3) from A to C
# # 6 Move (1) from B to A
# # 7 Move (2) from B to C
# # 8 Move (1) from A to C

# def hanoi(n, source, target, auxiliary):
#     if n > 0:
#         # Przeniesienie (n-1) krążków ze źródła do słupka pomocniczego
#         hanoi(n - 1, source, auxiliary, target)

#         # Przeniesienie największego krążka ze źródła do celu
#         print(f"Move ({n}) from {source} to {target}")

#         # Przeniesienie (n-1) krążków z pomocniczego do celu
#         hanoi(n - 1, auxiliary, target, source)


# # Przykładowe użycie
# num_discs = 3
# hanoi(num_discs, 'A', 'C', 'B')
