# Zadanie 1
# Napisz program w Pythonie, który przyjmuje od użytkownika imię i nazwisko, a następnie wy-
# świetla je w odwrotnej kolejności ze spacją między nimi i powitaniem.
def zadanie_1():
    name = input("Podaj imię: ")
    surname = input("Podaj nazwisko: ")
    greeting = "Cześć"

    print(f"{greeting} {surname} {name}!")
    pass

# Zadanie 2
# Napisz program w Pythonie, który przyjmuje nazwę pliku od użytkownika i wypisuje jego roz-
# szerzenie.
def zadanie_2():
    filename = input("Podaj nazwę pliku: ")
    ext = filename.split(sep=".")[-1]
    print(f"Rozszerzenie pliku to: {ext}")
    pass

# Zadanie 3
# Napisz program, który pobierze trzy wartości od użytkownika, a następnie wyświetli datę wyda-
# rzenia w formacie "DD/MM/YYYY"
def zadanie_3():
    day = int(input("Podaj dzień: "))
    month = int(input("Podaj miesiąc: "))
    year = int(input("Podaj rok: "))

    print(f"{day}/{month}/{year}")
    pass

# Zadanie 4
# Pobierz od użytkownika dwie liczby całkowite, dodaj je do siebie i wyświetl wynik. Wynik powi-
# nien zostać wyświetlony w poniższej postaci.
def zadanie_4():
    x = int(input("Podaj liczbę: "))
    y = int(input("Podaj liczbę: "))

    print(f"Suma {x} oraz {y} to {x+y}")
    pass

# Zadanie 5
# Pobierz od użytkownika cztery liczby, dwie całkowite i dwie zmiennoprzecinkowe. Dodaj pierwszą
# i trzecią do siebie, odejmij drugą od czwartej, a następnie dodaj do siebie liczby wynikowe z
# poprzednich operacji. Wyświetl poszczególne operacje oraz typy tych zmiennych (pobranych od
# użytkownika oraz przejściowych, tj. tych po każdej z operacji)
def zadanie_5():
    i1 = int(input("Podaj liczbę całkowitą: "))
    i2 = int(input("Podaj liczbę całkowitą: "))
    f1 = float(input("Podaj liczbę zmiennoprzecinkową: "))
    f2 = float(input("Podaj liczbę zmiennoprzecinkową: "))

    x = i1 + f1
    print(f"{i1} + {f1} = {x}, {x} jest typem {type(x)}")
    y = i2 + f2
    print(f"{i2} + {f2} = {i2+f2}, {y} jest typem {type(y)}")
    res = x + y
    print(f"{x} + {y} = {res}, {res} jest typem {type(res)}")
    pass

# Zadanie 6
# Pobierz od użytkownika dwie wartości, liczbę oraz stopień pierwiastka, następnie oblicz i wyświetl
# sformatowany wynik.
def zadanie_6():
    val = int(input("Podaj wartość: "))
    n = int(input("Podaj stopień pierwiastka: "))

    print(f"Pierwiastek {n} stopnia z {val} to {val ** (1/n)}")
    pass

# Zadanie 7
# Pobierz od użytkownika dwa napisy, a następnie wyświetl je w jednej linii wykorzystując trzy
# różne sposoby formatowania.
def zadanie_7():
    str_1 = input("Podaj napis (1):")
    str_2 = input("Podaj napis (2):")

    print(f"{str_1},{str_2}")
    print("{},{}".format(str_1,str_2))
    print(str_1+","+str_2)
    pass


# Zadanie 8
# Pobierz od użytkownika trzy boki trójkąta, a następnie oblicz pole trójkąta korzystając ze wzoru
# Herona, który został podany poniżej. Program powinien działać w następujący sposób.
def zadanie_8():
    a = float(input("Podaj pierwszy bok: "))
    b = float(input("Podaj drugi bok: "))
    c = float(input("Podaj trzeci bok: "))

    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** (0.5)
    print("Pole trójkąta wynosi: {:.2f}".format(area))
    pass

# Zadanie 9
# Pobierz od użytkownika odległość w kilometrach, a następnie dokonaj konwersji na mile. Wynik
# wyświetl w poniszy sposób
def zadanie_9():
    km = float(input("Podaj kilometry: "))
    CONV_VAL = 0.621371
    mi = km * CONV_VAL
    print(f'{km}km to {"{:.2f}".format(mi)}mi')
    pass

# Zadanie 10
# Pobierz od użytkownika temperaturę w stopniach Celsjusza, a następnie dokonaj konwersji na
# Fahrenheita. Wynik wyświetl w poniższy sposób.
def zadanie_10():
    temp_c = float(input("Podaj temperaturę w stopniach Celsjusza: "))
    temp_f = temp_c * 9/5 + 32
    print(f'{temp_c} stopni Celsjusza to {temp_f} stopni Fahrenheita')
    pass

if __name__ == "__main__":
    # Zadania na ocenę
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

