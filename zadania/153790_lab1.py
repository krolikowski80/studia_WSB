# Tomasz Królikowski
# Numer albumu: 153790

# zad 1
first_name = input("Podaj swoje imię: ")
last_name = input("Podaj swoje nazwisko: ")
print(f"Cześć {last_name} {first_name}")

# zad 2
file_name = input("Podaj nazwę pliku: ")
ext = file_name.split(".")
print(f"Rozszerzenie pliku to: {ext[-1]}")

# zad 3
day = input("Podaj dzień: ")
month = input("Podaj miesiąc: ")
year = input("Podaj rok: ")
print(f"Data wydarzenia to: {day}/{month}/{year}")

# zad 4
num_1 = int(input("Podaj pierwsaą liczbę: "))
num_2 = int(input("Podaj drugą liczbę: "))
out = num_1+num_2
print(f"Suma {num_1} oraz {num_2} to {out}")

# zad 5
num_1 = int(input("Podaj pierwsaą liczbę: "))
num_2 = int(input("Podaj drugą liczbę: "))
num_3 = float(input("Podaj trzecią liczbę: "))
num_4 = float(input("Podaj czwartą liczbę: "))
print(f"Pierwsza liczba jest typu: {type(num_1)}")
print(f"Druga liczba jest typu: {type(num_2)}")
print(f"Trzecia liczba jest typu: {type(num_3)}")
print(f"Czwarta liczba  jest typu: {type(num_4)}")

# Dodaj pierwszą i trzecią do siebie
out_1 = num_1 + num_3
print(f"Wynik dodawania liczby {num_1} do {
      num_3} jest równy: {out_1} i jest to typ: {type(out_1)}")

# odejmij drugą od czwartej
out_2 = num_4 - num_2
print(f"Wynik odejmowania liczby {num_2} od {
      num_4}  jest równy: {out_2} i jest to typ: {type(out_1)}")

# dodaj do siebie liczby wynikowe z poprzednich operacji.
out_3 = out_1 + out_2
print(f"Wynikiem doawania poprzednich działań, czyli {
      out_1} + {out_2} jest: {out_3} i jest to format {type(out_3)}")


# zad 6
num = int(input("Podaj liczbę: "))
sqr = int(input("Podaj stopień pierwiastka: "))
out = num**(1/sqr)
print(f"Pierwiastek {sqr} stopnia z {num} wynosi: {out}")

# zad 7
word_1 = input("Napisz coś: ")
word_2 = input("I jeszcze coś: ")
word_3 = input("Ostatnie coś: ")
print(f"napisałeś: {word_1}, potem: {word_2} i na końcu: {word_3}")
print("napisałeś: {}, potem: {} i na końcu: {}".format(word_1, word_2, word_3))
print("napisałeś: {1}, oraz: {0} i jeszcze: {2}".format(
    word_1, word_2, word_3), end=".")

# zad 8
# Pobieranie danych od użytkownika
a = float(input("Wprowadź pierwszy bok: "))
b = float(input("Wprowadź drugi bok: "))
c = float(input("Wprowadź trzeci bok: "))
# Wynik
A = (a+b+c)/2
P = (A*(A-a)*(A-b)*(A-c))**(1/2)
print(f"Pole trójkąta o bokach {a}, {b} i {c} wynosi {P}")


# zad 9
km = float(input("Wprowadź wartość w kilometrach: "))
mil = km * 0.62137
print(f"Odległość w milach to: {"{:.2f}".format(mil)}")

# zad 10
cel = float(input("Wprowadź temperaturę w stopniach Celsjusza: "))
fah = (1.8 * cel)+32
print(f"Wynik temp {cel} w stopniach {fah}")
