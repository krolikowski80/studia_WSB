import random

# Zadanie 1
# Napisz program, który pobierze od użytkownika liczbę całkowitą. Jeżeli pobrana liczba jest nie-
# parzysta, należy podnieść ją do potęgi trzeciej i wyświetlić wynik tej operacji. Jeżeli liczba jest
# parzysta, należy podzielić ją przez 2 i wyświetlić wynik tej operacji.
def zadanie_1():
    n = int(input('Podaj liczbę całkowitą: '))
    if n % 2 == 0:
        print(f'Wynik: {n/2}')
        return
    print(f'Wynik: {n ** 3}')
    pass

# Zadanie 2
# Napisz program, który używając tylko pętli for i range() wypisze na ekran:
# (a) Liczby naturalne od 0 do 5 (bez 5),
# (b) Liczby naturalne od 5 do 10 (z 10),
# (c) Liczby naturalne od 0 do 10 z krokiem 3,
# (d) Liczby naturalne od 0 do -10 z krokiem -2.
def zadanie_2():
    ranges = [range(5), range(5,11), range(0,10,3), range(0, -10, -2)]
    for i, rang in enumerate(ranges):
        print(f'{i}: ', end='')
        for n in rang:
            print(f'{n} ', end='')
        print()

    pass

# Zadanie 3
# Napisz program który będzie pobierał od użytkownika słowa do momentu wprowadzenia słowa
# "koniec", a następnie wyświetli wszystkie wprowadzone słowa razem (w jednej linii (w postaci
# listy)).
def zadanie_3():
    words = []
    while word:=input('Podaj słowo: '):
        if word == 'koniec':
            break
        words.append(word)
    print(words)
    pass

# Zadanie 4
# Napisz program który znajdzie pozycje (indeks) i wartości największej i najmniejszej liczb w
# liście. Wartości do listy mogą być wpisane na sztywno lub pobierane od użytkownika. Proszę
# nie używać funkcji wbudowanych, a wykonać program używając operatorów for i if.
# Przydatne: for, range(), if, elif, else, [], append(), int()
# Zabronione w tym zadaniu: max(), min(), index()
def zadanie_4():
    nums = [x * (x//2) for x in range(32)]
    min_i = max_i = 0
    min_val = max_val = nums[0]
    for i, num in enumerate(nums[1::]):
        if num > max_val:
            max_val = num
            max_i = i
        if num < min_val:
            min_val = num
            min_i = i
    print(f'Wartość najmniejsza: {min_val} znajduje się w indeksie {min_i}')
    print(f'Wartość największa: {max_val} znajduje się w indeksie {max_i}')
    pass

# Zadanie 5
# Napisz program, który sprawdzi czy z trzech podanych przez użytkownika długości odcinków
# można utworzyć trójkąt prostokątny. Zakładamy że użytkownik będzie wprowadzać tylko liczby
# dodatnie. Boki trójkąta prostokątnego spełniają twierdzenie Pitagorasa (a2 + b2 = c2).
# Przydatne: if, elif, else, int(), float()
def zadanie_5():
    sides = [float( input("Podaj długość boku: ") ) for _ in range(3)]
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print(f'Z boków: {sides[::]} można utworzyć trójkąt prostokątny')
        return
    print(f'Z boków: {sides[::]} nie można utworzyć trójkąta prostokątnego')
    pass

# Zadanie 6
# Napisz program który pobierze od użytkownika liczbę całkowitą, a następnie obliczy sumę cyfr
# z których składa się ta liczba. Przykładowo, dla liczby 1234 mamy otrzymać wynik 1 + 2 + 3 +
# 4 = 10.
# Przydatne: while, //, %
def zadanie_6():
    num = abs(int(input("Podaj liczbę całkowitą: ")))
    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10

    print(f'Suma: {sum}')
    pass

# Zadanie 7
# Napisz program, który pobierze od użytkownika napis i w kolejnych linijkach wypisze:
# (a) długość napisu,
# (b) czwarty znak napisu,
# (c) przedostatni znak,
# (d) pierwsze 10 znaków napisu,
# (e) wszystkie znaki napisu oprócz ostatnich 5,
# (f) wszystkie znaki od 5 do 5 od końca znaku (włącznie),
# (g) znaki o indeksach parzystych w odwrotnej kolejności,
# Zakładamy że zawsze będzie podany napis wystarczającej długości. Do zadania należy użyć
# notacje "slice".
# Przydatne: len(), print(), [start:stop:step]
def zadanie_7():
    s = input('Podaj napis: ')
    l = len(s)
    print(f'(a){l}')
    print(f'(b){s[3]}')
    print(f'(c){s[-2]}')
    print(f'(d){s[:10]}')
    print(f'(e){s[:-5]}')
    print(f'(f){s[5:-4]}')
    print(f'(g){s[l - l % 2::-2]}')
    pass

# Zadanie 8
# Napisz program, który sprawdzi czy napis jest palindromem. Napis może być pobierany przez
# użytkownika, lub wpisany na sztywno. Zadanie należy wykonać bez użycia funkcji re-
# versed i slice’sów, a posługując się pętlą i indeksowaniem. Do usunięcia spacji można
# posłużyć się funkcjami split() i join(). Palindrom to napis, który czyta się jednakowo z obu stron.
# Przydatne: for, range(), split(), join(), if, elif, else
# Zabronione w tym zadaniu: reversed(), [start:stop:step]
def zadanie_8():
    s = input('Podaj napis: ').replace(' ', '')
    size = len(s) - 1
    for i in range(len(s) // 2 + 1):
        if s[i] != s[size - i]:
            print('Podane wyrażenie nie jest palindromem')
            return
    print('Podane wyrażenie jest palindromem')
    pass

# Zadanie 9
# Napisz program, który pobierze od użytkownika napis (ewentualnie może być wpisany na sztywno),
# a następnie w każdym drugim słowie zamieni literę ”a” na dużą literę ”A”. Pozostałe słowa należy
# zmienić tak, żeby zaczynały się z dużej litery. Zakładamy że zawsze będą wprowadzone minimum
# 2 słowa, oddzielone spacjami.
# Przydatne: split(), join(), replace(), capitalize(), title()
def zadanie_9():
    words = input('Podaj napis: ').split(' ')
    for i, word in enumerate(words):
        if i % 2 == 1:
            words[i] = word.replace('a', 'A')
            continue
        words[i] = word.title()
    print(' '.join(words))
    pass

# Zadanie 10
# Napisz program, który obliczy i wyświetli listę, składającą się z N wyrazów ciągu Fibonacciego,
# zdefiniowanego poniższym wzorem:
# Liczba wyrazów do wygenerowania N może być pobierana od użytkownika lub wpisana na
# sztywno.
# Przydatne: for, range()
def zadanie_10():
    n = int(input('Podaj liczbę wyrazów ciągu Fibonacciego: '))
    nums = [1, 2]

    if n == 0 or n == 1:
        print(f'{nums[n]}')

    for i in range(2, n):
        nums.append(nums[i-1] + nums[i-2])
    print(nums)
    pass

# Zadanie 11
# Dane są dwie listy, zawierające liczby. Należy napisać program, który przeiteruje po obu listach
# jednocześnie i wyświetli w oddzielnych wierszach elementy z obu list, stojące na tej samej pozy-
# cji i ich sumę, jeżeli te elementy są różne. W przypadku gdy te elementy są jednakowe, należy
# wyświetlić ich iloczyn. Wyjście programu należy sformatować tak jak to jest pokazane w przy-
# kładzie. Należy użyć funkcji zip() i formatowania napisów.
# Przydatne: for, zip(), if, else
# Zabronione w tym zadaniu: range()
def zadanie_11():
    nums_1 = [1, 4, 3, 5, 2]
    nums_2 = [4, 2, 1, 5, 3]

    for x, y in zip(nums_1, nums_2):
        op = '+' if x != y else '*'
        res = x+y if x != y else x ** 2
        print(f'{x} {op} {y} = {res}')
    pass

# Zadanie 12
# Podana jest lista zawierająca słowa. Napisz program, który wypisze w kolejnych wierszach indeks
# elementu listy wraz ze słowem znajdującym się pod tym indeksem, a dodatkowo wskaże na słowa
# (dopisać strzałkę jak przy przykładzie), w których liczba liter ”a” jest równa indeksu słowa w
# liście. Proszę użyć funkcji enumerate() i count()
# Przydatne: for, if, else, enumerate()
# Zabronione w tym zadaniu: range()
def zadanie_12():
    words = ["orange", "apple", "cherry", "banana"]
    for i, word in enumerate(words):
        mark = ['', '<--']
        print(f'{i}: {word} {mark[word.count("a") == i]}')
    pass

# Zadanie 13
# Przyjmij listę składającą się z 10 liczb losowych z przedziału od 0 do 10 (10 nie włączamy), a
# następnie oblicz wystąpienia poszczególnych liczb w tym napisie. Do wykonania tego zadania
# należy posłużyć się słownikiem.
# Przydatne: for, in, [], , if, else, randrange()
# Zabronione w tym zadaniu: count()
def zadanie_13():
    nums = [random.randrange(0,10) for _ in range(10) ]
    counted = {key: 0 for key in set(nums)}

    for n in nums:
        counted[n] += 1

    print(counted)
    pass

# Zadanie 14
# Napisz prosty program do manipulacji napisami. Program w pętli ma pobierać od użytkownika
# dane w formacie polecenie jakieś słowa, gdzie polecenie będzie jednym z czterech napisów: lower
# (zamień wszystkie litery na małe), upper (zamień wszystkie litery na duże), title (zrób pierwszą
# literę każdego słowa dużą), reverse (odwróć znaki w napisie). W zależności od tego które po-
# lecenie będzie podane, należy wyświetlić odpowiednio zmodyfikowaną resztę napisu pobranego
# od użytkownika. Należy zakończyć działanie programu, jeżeli nie zostanie wprowadzone nic (po
# prostu wciśnięcie Enter). W przypadku podania nieznanego polecenia należy poinformować użyt-
# kownika o tym. Należy użyć funkcji lower(), upper(), title(), reversed() lub slice’ów.
# Przydatne: split(), upper(), lower(), title(), reversed(), join(), [start:stop:step]
def zadanie_14():
    cmds = lambda s, cmd : { 'upper': s.upper(), 'lower': s.lower(),
                            'title': s.title(), 'reversed': s[-1::-1]
                            }.get(cmd)

    while (line := input('Wpisz napis z komendą: ')) != '':
        words = line.split(' ')
        cmd = words[0]
        string = ' '.join(words[1::])
        print('Nieprawidłowa komenda' if (res := cmds(string, cmd))== None else res)
    pass

# Zadanie 15
# Napisz funkcję która przyjmuje liczbę x jako jedyny argument i zwraca wartość funkcji f (x) =
# x3 − 3x2 + 8x − 2 dla podanego argumentu x.
# Przydatne: def, return
def zadanie_15():
    x = float(input('Podaj wartość x: '))
    print(f'f({x}) = {(lambda x: x ** 3 - 3 * x ** 2 + 8 * x - 2)(x)}')
    pass

# Zadanie 16
# Napisz funkcję, która przyjmuje jako argument listę liczb całkowitych, tworzy kopie tej listy i
# modyfikuje jej kopie w następujący sposób:
# • Usuwa wszystkie podzielne przez 4 liczby,
# • Wkleja wartość -1 przed każdą liczbą nieparzystą.
# Po dokonaniu modyfikacji zmodyfikowana wersja listy ma być zwrócona z funkcji. Przy tym
# funkcję należy napisać tak, żeby lista, podana jako argument została niezmieniona. Zademonstruj
# działanie funkcji na liście liczb losowych z zakresu od 0 do 10.
# Przydatne: def, return, copy(), del, pop(), insert()
def zadanie_16():

    def f(nums: list[int]) -> list[int]:
        vals = []
        for i, val in enumerate(nums):
            if val % 2 == 1:
                vals.append(-1)
            vals.append(val)
        return list(filter(lambda x: x % 4 != 0, vals))

    nums = [random.randrange(0,10) for _ in range(10) ]
    print('Lista: {}', nums)
    print('Wynik: {}', f(nums))
    pass

# Zadanie 17
# Napisz funkcję, która przyjmuje napis o dowolnej długości jako jedyny argument i zwraca listę
# napisów będących kombinacjami par symboli, z których składa się podany jako argument napis.
# Przydatne: for in, def, return, range(), enumerate()
def zadanie_17():
    def get_all_pairs(s: str) -> list[str]:
        pairs = []
        for i, x in enumerate(s):
            for j, y in enumerate(s):
                if i == j:
                    continue
                pairs.append(''.join([x,y]))

        return pairs

    print(get_all_pairs(input('Podaj ciąg znaków: ')))
    pass

# Zadanie 18
# Zaznajom się ze składnią list składanych (list comprehension), następnie napisz program, który
# utworzy używając tej składni trzy listy:
# • Lista składająca się z sześcianów liczb naturalnych od 0 do 10.
# • Lista składająca się z sześcianów liczb naturalnych od 0 do 10 pod warunkiem że sześcian tej liczby jest podzielny przez 3.
# • Lista składająca się z na przemian kwadratów i sześcianów liczb naturalnych od 0 do 10.
# • Jeżeli liczba jest podzielna na 3, to zapisujemy jej sześcian, inaczej kwadrat. Początek listy:
# [0, 1, 4, 27, 16, ...
def zadanie_18():
    print([x ** 3 for x in range(10)])
    print([x ** 3 for x in range(10) if x ** 3 % 3 == 0])
    print([x ** 3 if x % 2 == 1 else x ** 2 for x in range(10)])
    print([x ** 3 if x % 3 == 0 else x ** 2 for x in range(10)])
    pass

if __name__ == "__main__":
    # zadanie_1()
    # zadanie_2()
    # zadanie_3()
    # zadanie_4()
    # zadanie_5()
    # zadanie_6()
    # zadanie_7()
    # zadanie_8()
    # zadanie_9()
    # zadanie_10()
    # zadanie_11()
    # zadanie_12()
    # zadanie_13()
    # zadanie_14()
    # zadanie_15()
    # zadanie_16()
    # zadanie_17()
    zadanie_18()
    pass


