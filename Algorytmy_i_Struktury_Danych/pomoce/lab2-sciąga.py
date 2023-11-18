import random

# Zadanie 1
# Zaimplementować wyszukiwania największej liczby w nieposortowanej liście liczb. Przetestować
# jego działanie i oszacować złożoność obliczeniową tego algorytmu. Krótko (1-2 zdania) opisać
# dlaczego ten algorytm ma taką złożoność obliczeniową
def zadanie_1():
    '''
    Złożoność algorytmu `find_max` to O(n).
    Pętla wykonuje się n razy dla listy o rozmiarze n.
    '''
    def find_max(nums):
        max_val = nums[0]
        for n in range(1, len(nums)):
            max_val = n if n >= max_val else max_val
        return max_val

    rand_list = [random.randrange(0, 10) for _ in range(10)]
    print(f'Największa wartość w liście {rand_list} to: {find_max(rand_list)}')
    pass

# Zadanie 2
# Zaimplementować algorytm sortowania przez wstawianie (insertion sort). Przetestować jego dzia-
# łanie i oszacować złożoność obliczeniową tego algorytmu. Krótko (1-2 zdania) opisać dlaczego ten
# algorytm ma taką złożoność obliczeniową
def zadanie_2():
    '''
    Złożoność `insert_sort` w najgorszym wypadku
    (w tym przypadku, gdy lista jest posortowana wartościami od największej do najmniejszej)
    wynosi O(n^2), gdyż w po przeiterowaniu przez całą listę w ostatnim kroku będzie musiał zobić to ponownie
    (od końca listy do jej początku).
    '''
    def insert_sort(nums):
        for i in range(1, len(nums)):
            prev_i = i - 1
            curr_item = nums[i]
            while curr_item < nums[prev_i] and prev_i >= 0:
                nums[prev_i + 1] = nums[prev_i]
                prev_i -= 1
            nums[prev_i + 1] = curr_item
        pass

    rand_list = [random.randrange(0, 10) for _ in range(10)]
    print(f'Nieposortowana lista {rand_list}')
    insert_sort(rand_list)
    print(f'Posortowana lista {rand_list}')

    print('')
    pass

# Zadanie 3
# Zaimplementować opisany poniżej algorytm i oszacować jego złożoność obliczeniową. Krótko (1-2
# zdania) opisać dlaczego ten algorytm ma taką złożoność obliczeniową.
# Algorytm: na wejściu funkcja dostaje dwa ciągi znaków o różnych długościach s1 i s2. Algo-
# rytm ma zliczyć ile razy w ciągu s1 występują znaki zawierające się w ciągu s2. W poniższym
# przykładzie zliczamy ile samogłosek występuje w zadanym ciągu.
def zadanie_3():
    '''
    n = len(s1)
    k = len(s2)
    Złożoność algorytmu `count_chars` w najgorszym przypadku wynosi O(n^2) (jeżeli n == k).
    Pętla for wykonuje się n razy dla argumentu `s1` oraz dla każdej z tych iteracji
    operator `in` w najgorszym wypadku iteruje k razy dla argumentu `s2`.
    '''
    def count_chars(s1: str, s2: str) -> int:
        count = 0
        for ch1 in s1:
            count += 1 if ch1 in s2 else 0
        return count
    s1 = 'ala ma kota'
    s2 = 'aeiouy'
    print(f'Wynik: {count_chars(s1, s2)}')
    pass
# Zadanie 4
# Zaimplementować algorytm obliczający sumę cyfr wprowadzanej przez użytkownika liczby. Przy-
# kładowo, dla liczby 1234 wynik działania algorytmu ma wynosić 1 + 2 + 3 + 4 = 10. Oszacować
# złożoność obliczeniową tego algorytmu oraz krótko (1-2 zdania) opisać dlaczego ten algorytm ma
# taką złożoność.
def zadanie_4():
    '''
    Złożoność algorytmu `sum_digits` wynosi O(n).
    Gdzie n == liczba cyfr w liczbie, 
    gdyż pętla wykonuje się raz dla każdej cyfry.
    '''
    def sum_digits(num):
        sum = 0
        while num != 0:
            sum += num % 10
            num //= 10
        return sum
    num = int(input('Podaj liczbę: '))
    print(f'Suma: {sum_digits(num)}')
    pass


if __name__ == "__main__":
    zadanie_1()
    zadanie_2()
    zadanie_3()
    zadanie_4()
    pass
