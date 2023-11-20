import random
import math
import collections
import itertools

# Zadanie 1
# Utwórz funkcję, która przyjmuje trzy argumenty n, a, b i zwraca listę o długości n, wypełnioną
# losowymi liczbami całkowitymi z zakresu od a do b. Argument n ma mieć wartość domyślną 10,
# argument a wartość domyślną 0 i argument b wartość domyślną 10.
# Przydatne: def, return, random.randrange()
def zadanie_1():
    def rand_list(a=0, b=10, n=10):
        return [random.randrange(a, b) for _ in range(n)]

    print(rand_list())
    print(rand_list(1,3))
    print(rand_list(2,5,3))
    pass


# Zadanie 2
# Napisz funkcję, która przyjmuje jeden argument n, i wykonuje następujące rzeczy:
# • Utworzy listę liczb losowych z zakresu od 0 do 10 o długości n (można użyć funkcję z
# poprzedniego zadania).
# • Wypisze na ekran wylosowaną listę.
# • Wypisze na ekran najmniejszą liczbę z listy.
# • Wypisze indeks pod którym znajduje się największa liczba w liście.
# • Wypisze sumę liczb w liście.
# • Wypisze posortowaną listę liczb (przy tym zachowując też wersje nieposortowaną).
# • Wypisze ile razy w liście występuje wartość 3.
# • Wypisze zbiór liczb unikalnych występujących w tej liście.
# Przydatne: print(), max(), min(), index(), sum(), count(), set(), sorted()
def zadanie_2():
    def rand_list_info(n):
        rand_list = [random.randrange(0, 10) for _ in range(n)]
        print('List: ', rand_list)
        print('Min: ', min(rand_list))
        print('Max index: ', rand_list.index(max(rand_list)))
        print('Sum: ', sum(rand_list))
        print('Sorted: ', sorted(rand_list))
        print('3 Count: ', rand_list.count(3))
        print('Unique: ', set(rand_list))

    rand_list_info(10)
    pass


# Zadanie 3
# Napisz program, który wygeneruje listę składającą się z 20 całkowitych liczb losowych od -100 do
# 100, a następnie obliczy sumę liczb dodatnich z tej listy, korzystając się ze składni list składanych
# (list comprehension).
# Przydatne: List comprehension, random.randrange()
def zadanie_3():
    rand_list = [random.randrange(-100, 100) for _ in range(20)]
    positive_sum = sum([x for x in rand_list if x >= 0])
    print('Random list: ', rand_list)
    print('Sum of positive numbers: ', positive_sum)
    pass
# Zadanie 4
# Napisz funkcję, która przyjmuje jeden argument który może być liczbą albo listą liczb. Jeżeli jako
# argument została podana liczba, należy zwrócić tą liczbę pomnożoną razy 2. Jeżeli jako argument
# została podana lista należy utworzyć nową listę, która będzie zawierała elementy pierwotnej listy,
# pomnożone razy 2. Zademonstruj działanie tej funkcji dla liczby i listy losowej
# Przydatne: List comprehension, random.randrange(), isinstance()
def zadanie_4():
    def func(n: int | list[int]) -> list[int] | int:
        return [i * 2 for i in n] if isinstance(n, list) else n * 2

    print(func(3))
    rand_list = [random.randrange(0,10) for _ in range(10)]
    print(func(rand_list))
    pass


# Zadanie 5
# Napisz program, który wygeneruje listę składającą się z 50 losowych liczb całkowitych z zakresu
# od 0 do 10, a następnie wyświetli 5 najczęściej spotykanych liczb. Do wykonania zadania należy
# użyć funkcji Counter(), z modułu collections.
# Przydatne: collections.Counter(), most_common(), random.randrange()
def zadanie_5():
    arr = [random.randrange(0, 10) for _ in range(50)]
    elements = collections.Counter(arr).most_common(5)
    print(arr)
    print('5 most common elements: ', [item for item, _ in elements])
    pass

# Zadanie 6
# Zastosuj funkcje z modułu itertools, żeby wypisać na ekran permutacje i kombinacje trzysymbo-
# lowe, które można złożyć z liter napisu podanego przez użytkownika.
# Przydatne: itertools.permutations(), itertools.combinations(), input()
def zadanie_6():
    chars = input('Podaj ciąg znaków: ')
    print('Permutacje: ', list( itertools.permutations(chars) ))
    print('Kombinacje: ', list( itertools.combinations(chars, 3) ))
    pass


# Zadanie 7
# Zaimplementuj funkcję służąca do obliczenia wyznacznika macierzy kwadratowych o rozmiarze
# 2. Macierz powinna być jedynym argumentem tej funkcji. W razie podania macierzy o złych
# wymiarach należy wyrzucić wyjątek ValueError z odpowiednią informacją.
# Przydatne: def, return, if, else, raise, ValueError()
def zadanie_7():
    def matrix_det(matrix):
        if not ( len(matrix) == len(matrix[0]) == len(matrix[1]) == 2 ):
            raise ValueError('Macierz nie jest wymiarów 2x2')
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    print('Matrix det: ', matrix_det([[1,2], [3,4]]))
    pass


# Zadanie 8
# Wczytaj plik points.txt, który zawiera współrzędne 100 punktów położonych w przestrzeni
# dwuwymiarowej (jeden wiersz - jeden punkt, współrzędne x i y są oddzielone od siebie spa-
# cjami). Pobierz od użytkownika dwie liczby będącymi współrzędnymi x, y kolejnego punktu.
# Następnie, wypisz na ekran współrzędne 10 punktów które są położone najbliżej tego wczyta-
# nego od użytkownika punktu.
# Przydatne: with, open(), read(), write(), math.dist()
def zadanie_8():
    with open('points.txt', 'r') as file:
        points = []
        for line in file.read().splitlines():
            point = line.split(' ')
            points.append([float( point[0] ), float( point[1] )])

        x = float(input('Podaj x: '))
        y = float(input('Podaj y: '))

        distances = [ math.dist([x, y], point) for point in points ]
        closest_points = [ points[distances.index(val)] for val in sorted(distances[:10:])]
        print(f'Punkty położone najbilżej punktu ({x}, {y}): {closest_points}')

# Zadanie 9
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
def zadanie_9():
    def quadratic(a, b, c):
        try:
            delt = math.sqrt(b**2 - 4 * a * c)
            return ((-b - delt)/(2*a), (-b + delt)/(2*a))
        except ValueError:
            return None

    results = []
    with open('equations.txt', 'r') as file:
        for line in file.read().splitlines()[:50]:
                data = [ float(val) for val in line.split(' ') ]
                res = '{} {}\n'.format(vals[0], vals[1]) if (vals := quadratic(*data)) != None else '\n'
                results.append(res)

    with open('equations_results.txt', 'w') as out:
        out.writelines(results)
    pass


# Zadanie 10
# Zaimplementuj funkcję, sprawdzającą czy liczba n podana jako argument jest liczbą pierwszą.
# Funkcja ma sprawdzać, czy liczba podana jako argument jest podzielna na potencjalne dzielniki
# tej liczby. Implementacja ma wykorzystywać następujące usprawnienia:
# • liczba 1 i wszystkie liczby ujemne nie są pierwsze,
# • liczby parzyste większe od 2 mogą być wyeliminowane od razu,
# • dla pozostałych liczb wystarczy sprawdzić ich podzielność na liczby nieparzyste od 3 do √n
# (włącznie!).
# Następnie, napisz program, który znajdzie które z pierwszych 30 liczb ciągu Fibonacciego są też
# liczbami pierwszymi. Liczby z ciągu Fibonacciego mogą być generowane w dowolny sposób.
# Przydatne: math.sqrt(), range()
def zadanie_10():
    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def fib(n):
        if n in [0,1]:
            return 1
        return fib(n - 1) + fib(n - 2)

    print('Liczby pierwsze ciągu Fibonacciego: ')
    for i in range(30):
        if is_prime(n:=fib(i)):
            print(n, end=' ')
    print()
    pass



# Zadanie 11
# Zaimplementuj generator, używającą słowo kluczowe yield która będzie służyć do generowania
# kolejnych wyrazów ciągu Collatz’a zaczynając od podanej jako argument funkcji liczby n do 1.
# Przy implementacji nie używamy rekurencji! Ciąg Collatz’a jest zdefiniowany następują-
# cym wzorem:
def zadanie_11():
    def collatz(n):
        while n > 1:
            yield n
            n = n/2 if n%2==0 else n*3+1
        yield n

    print('Generator ciągu Collatz\'a:')
    for i in collatz(10):
        print(i, end=" -> " if i != 1 else "\n")
    pass


# Zadanie 12
# Wczytaj plik cars.csv, który zawiera w kolejnych wierszach dane o samochodach w postaci produ-
# cent, model, rok, cena, oddzielone przycinkami. Należy wczytać te dane do struktury listy krotek
# (list of tuples). Następnie, należy użyć funkcji wbudowanych sorted(), min() z argumentem
# key i wyświetlić:
# • Dane o samochodach, posortowane od najtańszego do najdroższego,
# • Dane o samochodach, posortowane od najnowszego do najstarszego,
# • Dane o najtańszym samochodzie.
# Przydatne: sorted(), min(), lambda, with, open(), read(), splitlines(), split()
def zadanie_12():
    cars = []
    with open('cars.csv', 'r') as file:
        for line in file.read().splitlines():
            data = tuple(line.split(','))
            cars.append(data)
        print(f'Cena - najniższa -> najwiższa:\n {sorted(cars, key=lambda data: float(data[-1]))}\n')
        print(f'Rok - najnowszy -> najstarszy:\n {sorted(cars, key=lambda data: float(data[-2]), reverse=True)}\n')
        print(f'Najtańszy samochód:\n {min(cars, key=lambda data: float(data[-1]))}\n')
    pass


if __name__ == "__main__":
    zadanie_1()
    zadanie_2()
    zadanie_3()
    zadanie_4()
    zadanie_5()
    zadanie_6()
    zadanie_7()
    zadanie_8()
    zadanie_9()
    zadanie_10()
    zadanie_11()
    zadanie_12()
