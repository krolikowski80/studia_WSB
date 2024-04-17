# Zad. 3.1 Punkt i Prosta
# Utwórz dwie klasy: jedna klasa ma reprezentować punkt na płaszczyźnie i posiadać współrzędne x,y tego punktu
# jak atrybuty i argumenty konstruktora. Druga klasa ma reprezentować prostą i posiada takie atrybuty jak a i b,
# definiujące przebieg prostej o równaniu y = ax + b.
# Dodaj do klasy Punkt metodę, która przyjmuje jako argument obiekt klasy Prosta i zwraca True albo False w
# zależności od tego leży nasz punkt na tej prostej czy nie.


class Punkt:
    def __init__(self, x, y):
        """
        Konstruktor klasy Punkt, inicjalizuje współrzędne punktu.

        Args:
        x (float): Współrzędna x punktu.
        y (float): Współrzędna y punktu.
        """
        self.x = x
        self.y = y

    def na_prostej(self, prosta):
        """
        Sprawdza, czy punkt leży na danej prostej.

        Args:
        prosta (Prosta): Obiekt klasy Prosta, reprezentujący prostą y = ax + b.

        Returns:
        bool: True jeśli punkt leży na prostej, False w przeciwnym razie.
        """
        # Obliczamy wartość y dla danej wartości x według równania prostej.
        y_na_prostej = prosta.a * self.x + prosta.b
        # Sprawdzamy, czy obliczona wartość y jest równa współrzędnej y punktu.
        return self.y == y_na_prostej


class Prosta:
    def __init__(self, a, b):
        """
        Konstruktor klasy Prosta, inicjalizuje współczynniki prostej.

        Args:
        a (float): Współczynnik kierunkowy a prostej.
        b (float): Wyraz wolny b prostej.
        """
        self.a = a
        self.b = b


p1 = Punkt(1, 3)
prosta1 = Prosta(2, 1)

# Sprawdzamy, czy punkt (1, 3) leży na prostej y = 2x + 1.
print(p1.na_prostej(prosta1))  # Wypisze: True

p2 = Punkt(1, 4)
# Sprawdzamy, czy punkt (1, 4) leży na tej samej prostej.
print(p2.na_prostej(prosta1))  # Wypisze: False


# -----------------------------------------------

# Zad 3.2 Prostokąt
# Utwórz klasę reprezentującą prostokąt. Konstruktor tej klasy musi przyjmować dwa obiekty klasy Punkt jako
# argumenty. Dwa punkty definiujące prostokąt muszą leżeć na przekątnej. Należy zaimplementować metodę, która
# obliczy boki prostokąta na podstawie punktów podanych do konstruktora. Klasa ma posiadać metody do obliczenia
# pola i obwodu prostokąta. Klasa ma także posiadać metodę która narysuje zdefiniowany prostokąt za pomocą
# biblioteki matplotlib i zaznaczy punkty którymi został zdefiniowany (patrz Rysunek 1).
# Przykład:
# 1 >>> p1 = Punkt(1, 1)
# 2 >>> p2 = Punkt(2, 3)
# 3 >>> prost = Prostokat(p1, p2)
# 4 >>> prost.pole()
# 5 2
# 6 >>> prost.obwod()
# 7 6
# 8 >>> prost.rysuj()

from matplotlib import pyplot as plt


class Punkt:
    """Konstruktor, który inicjalizuje nowy punkt z danymi współrzędnymi x i y."""

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Prostokat:
    """Konstruktor, który przyjmuje dwa punkty, określające przekątne prostokąta."""

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.width = abs(p1.x - p2.x)
        self.height = abs(p1.y - p2.y)

    def pole(self):
        """Metoda, która zwraca pole prostokąta."""
        return self.width * self.height

    def obwod(self):
        """Metoda, która zwraca obwód prostokąta."""
        return 2 * (self.width + self.height)

    def rysuj(self):
        """Rysuje prostokąt na podstawie dwóch punktów."""
        # Współrzędne x i y wszystkich czterech rogów prostokąta
        ## ZROZUMIENIE  I DOBRE NAPISANIE TEGO ZAJĘŁO MI SPORO CZASU ;/
        x_values = [
            self.p1.x,
            self.p2.x,
            self.p2.x,
            self.p1.x,
            self.p1.x,
        ]
        y_values = [
            self.p1.y,
            self.p1.y,
            self.p2.y,
            self.p2.y,
            self.p1.y,
        ]

        plt.figure(figsize=(5, 5))
        plt.plot(x_values, y_values, "r")  # Rysowanie prostokąta
        plt.scatter(
            [self.p1.x, self.p2.x], [self.p1.y, self.p2.y], color="blue"
        )  # Zaznaczanie punktów
        plt.xlim(min(self.p1.x, self.p2.x) - 1, max(self.p1.x, self.p2.x) + 1)
        plt.ylim(min(self.p1.y, self.p2.y) - 1, max(self.p1.y, self.p2.y) + 1)
        plt.grid(True)
        plt.show()


p1 = Punkt(0, 0)
p2 = Punkt(4, 8)
prostokat = Prostokat(p1, p2)
print("Pole prostokąta:", prostokat.pole())
print("Obwód prostokąta:", prostokat.obwod())
prostokat.rysuj()


# -----------------------------------------------
# Zad 3.3 Notatka i Notatnik
# Utworzyć klasy Notatka (Note) i Notatnik (Notebook). Klasa notatki przechowuje autora, treść i czas stworzenia
# (autor i treść są podawane jako argumenty konstruktora, a czas jest pobierany i zapisywany przy tworzeniu obiektu).
# Konstruktor klasy Notatnik nie przyjmuje żadnych argumentów, lecz tworzy pustą listę do której będą dodawane
# obiekty klasy Notatka. Klasa Notatnika musi posiadać implementacje metod, pozwalających: dodać nową notatkę,
# dodać istniejącą notatkę, sprawdzić ile jest dodanych notatek, wyświetlić wszystkie dodane notatki. Dodatkowo
# musi być obsłużona sytuacja kiedy notatnik jest pusty.
# Przykład:
# 1 >>> nb = Notebook()
# 2 >>> nb.dodaj_nowa("Bartek", "Dokonczyc instrukcje")
# 3 >>> nb.wyswietl_wszystko()
# 7
# 4 Masz takie notatki:
# 5 1. Bartek: "Dokonczyc instrukcje" o godzinie 22:18
# 6 >>> n1 = Note("Andrii", "Sprawdzic instrukcje")
# 7 >>> nb.dodaj(n1)
# 8 >>> nb.wyswietl_wszystko()
# 9 Masz takie notatki:
# 10 1. Bartek: "Dokonczyc instrukcje" o godzinie 22:18
# 11 2. Andrii: "Sprawdzic instrukcje" o godzinie 22:20
# Podpowiedź: do reprezentacji czasu można użyć modułu datetime.
# Dokumentacja modułu datetime: https://docs.python.org/3/library/datetime.html
# Przykład:
# 1 >>> import datetime
# 2 >>> t = datetime.datetime.now()
# 3 >>> t
# 4 datetime.datetime(2021, 4, 8, 22, 39, 46, 274407)
# 5 >>> t.hour
# 6 22
# 7 >>> t.minute
# 8 27

import datetime


class Note:
    def __init__(self, author, content):
        """
        Inicjalizuje notatkę z podanym autorem, treścią i bieżącym czasem.

        Args:
            author (str): Autor notatki.
            content (str): Treść notatki.
        """
        self.author = author
        self.content = content
        self.creation_time = (
            datetime.datetime.now()
        )  # Zapisuje czas utworzenia notatki.

    def __str__(self):
        """
        Zwraca reprezentację stringową notatki.
        """
        return f'{self.author}: "{self.content}" o godzinie {self.creation_time.hour}:{self.creation_time.minute:02}'


class Notebook:
    def __init__(self):
        """
        Inicjalizuje pusty notatnik.
        """
        self.notes = []  # Lista przechowująca notatki.

    def dodaj_nowa(self, author, content):
        """
        Tworzy i dodaje nową notatkę do notatnika.

        Args:
            author (str): Autor notatki.
            content (str): Treść notatki.
        """
        new_note = Note(author, content)
        self.notes.append(new_note)

    def dodaj(self, note):
        """
        Dodaje istniejącą notatkę do notatnika.

        Args:
            note (Note): Obiekt notatki do dodania.
        """
        if isinstance(note, Note):
            self.notes.append(note)
        else:
            raise ValueError("Obiekt nie jest notatką")

    def ile_notatek(self):
        """
        Zwraca liczbę notatek w notatniku.

        Returns:
            int: Liczba notatek.
        """
        return len(self.notes)

    def wyswietl_wszystko(self):
        """
        Wyświetla wszystkie notatki w notatniku.
        """
        if self.notes:
            print("Masz takie notatki:")
            for idx, note in enumerate(self.notes, 1):
                print(f"{idx}. {note}")
        else:
            print("Notatnik jest pusty.")


nb = Notebook()
nb.dodaj_nowa("Bartek", "Dokonczyc instrukcje")
nb.wyswietl_wszystko()

n1 = Note("Andrii", "Sprawdzic instrukcje")
nb.dodaj(n1)
nb.wyswietl_wszystko()

# n2 = ("Tomasz", "Zacznij wreszcie się uczyć") #Nie jest instancją klasy Note
# nb.dodaj(n2)
# nb.wyswietl_wszystko()

# ------------------------------------------------------
# zad 3.4 Pracownik
# Stwórz klasę "Pracownik"w Pythonie, która będzie posiadać atrybuty "imie", "nazwisko"oraz "stanowisko". Klasa
# powinna zawierać publiczną metodę "przedstaw_sie()", która wyświetli imię i nazwisko pracownika oraz jego stanowisko.
# Dodatkowo, klasa powinna posiadać atrybut chroniony "_id_pracownika", który będzie nadawany automatycznie
# przy tworzeniu nowego obiektu i będzie unikalny dla każdego pracownika.
# Podpowiedź: użyć id(self): https://www.programiz.com/python-programming/methods/built-in/id
# Ostatecznie, klasa powinna mieć prywatne pole "__pensja", które będzie przechowywać informację o wynagrodzeniu
# pracownika oraz prywatną metodę "__zmien_pensje(self, nowa_pensja)", która będzie umożliwiała zmianę
# wynagrodzenia tylko z poziomu klasy. Dodatkowo zaimplementuj metodę wplata, która będzie wykorzystywała metode
# __zmien_pensje(self, nowa_pensja) o zadaną wartość. Należy obsłużyć wyjątek gdzie wartość jest ujemna.
# Przykład:
# 1 >>> pracownik1 = Pracownik("Jan", "Kowalski", "Inżynier")
# 2 >>> pracownik1.przedstaw_sie()
# 3 Cześć, nazywam się Jan Kowalski i pracuję na stanowisku Inżynier.
# 4 >>> pracownik2 = Pracownik("Anna", "Nowak", "Specjalista ds. marketingu")
# 5 >>> pracownik2.przedstaw_sie()
# 6 Cześć, nazywam się Anna Nowak i pracuję na stanowisku Specjalista ds. marketingu.
# 7 >>> print(f"ID pracownika 1: {pracownik1._id_pracownika}")
# 8 ID pracownika 1: 2532711240704
# 9 >>> print(f"ID pracownika 2: {pracownik2._id_pracownika}")
# 10 ID pracownika 2: 2532712894912
# 11 >>> pracownik1.wplata(1000)
# 12 >>> print(f"Wynagrodzenie pracownika 1: {pracownik1.get_pensja()}")
# 13 Wynagrodzenie pracownika 1: 1000

import datetime


class Pracownik:
    def __init__(self, imie, nazwisko, stanowisko):
        """
        Konstruktor klasy Pracownik, który inicjalizuje pracownika z podanym imieniem, nazwiskiem i stanowiskiem.
        Przypisuje również unikalne ID pracownika oraz ustawia początkowe wynagrodzenie na 0.
        """
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self._id_pracownika = id(self)  # Nadanie unikalnego ID pracownika.
        self.__pensja = 0  # Prywatne pole przechowujące pensję pracownika.

    def przedstaw_sie(self):
        """
        Publiczna metoda wyświetlająca informacje o pracowniku.
        """
        print(
            f"Cześć, nazywam się {self.imie} {self.nazwisko} i pracuję na stanowisku {self.stanowisko}."
        )

    def __zmien_pensje(self, nowa_pensja):
        """
        Prywatna metoda zmieniająca pensję pracownika na podaną wartość.
        """
        self.__pensja = nowa_pensja

    def wplata(self, kwota):
        """
        Metoda do zwiększania pensji pracownika o daną kwotę. Rzuca wyjątek, jeśli kwota jest ujemna.
        """
        if kwota < 0:
            raise ValueError("Kwota wpłaty nie może być ujemna.")
        self.__zmien_pensje(self.__pensja + kwota)

    def get_pensja(self):
        """
        Metoda do uzyskania aktualnej wartości pensji pracownika.
        """
        return self.__pensja


pracownik1 = Pracownik("Jan", "Kowalski", "Inżynier")
pracownik1.przedstaw_sie()  # Wyświetla informacje o pracowniku 1

pracownik2 = Pracownik("Anna", "Nowak", "Specjalista ds. marketingu")
pracownik2.przedstaw_sie()  # Wyświetla informacje o pracowniku 2

print(f"ID pracownika 1: {pracownik1._id_pracownika}")
print(f"ID pracownika 2: {pracownik2._id_pracownika}")

try:
    pracownik1.wplata(1000)
except ValueError as e:
    print(e)

print(f"Wynagrodzenie pracownika 1: {pracownik1.get_pensja()}")


# ------------------------------------------------------
# Zad 3.5 Player
# Stwórz klasę "Player"w Pythonie, która będzie przechowywać informacje o graczach w grze. Klasa powinna mieć
# pola publiczne "nick", prywatne "__health"oraz chronione "_score". Klasa powinna zawierać metody publiczne
# "attack(enemy)"oraz "heal()", które będą umożliwiać odpowiednio atakowanie przeciwnika oraz leczenie siebie.
# Metoda ataku powinna zmniejszać zdrowie przeciwnika, a metoda leczenia zwiększać zdrowie gracza.
# Pole "__health"powinno być prywatne, aby uniemożliwić bezpośrednią zmianę wartości z zewnątrz klasy. Do
# odczytu wartości pola "__health"powinna zostać utworzona metoda prywatna o nazwie "_get_health()", która
# będzie zwracać wartość pola "_health". Do zapisu wartości pola "__health"powinna zostać utworzona metoda
# prywatna o nazwie "_set_health()", która będzie zapisywać wartość pola "__health".
# Aby ułatwić odczyt wartości pola "__health", powinna zostać utworzona właściwość o nazwie "health", dekoratorem
# @property oraz @health.setter. Właściwość ta powinna korzystać z metod prywatnych "_get_health()"oraz
# "_set_health()".
# Dodatkowo, klasa "Player"powinna mieć pole publiczne "level", które będzie przechowywać poziom gracza. Pole
# to powinno zostać utworzone za pomocą dekoratora @property, w taki sposób, że poziom gracza będzie wyznaczany
# na podstawie wartości pola "_score". Np. jeśli "_score"będzie większe od 100, to poziom gracza będzie równy 2, a
# jeśli "_score"będzie większe od 200, to poziom gracza będzie równy 3, itd.
# Przykład:
# 1 # Tworzenie obiektów klasy Player
# 2 >>> player1 = Player("John")
# 3 >>> player2 = Player("Mike")
# 4
# 5 # Odczytanie pocz ˛ atkowych wartości pól obiektów
# 6 >>> print(f"{player1.nick}: health={player1.health}, level={player1.level}")
# 7 John: health=100, level=1
# 8 >>> print(f"{player2.nick}: health={player2.health}, level={player2.level}")
# 9 Mike: health=100, level=1
# 10
# 11 # Atakowanie przeciwnika
# 12 >>> player1.attack(player2)
# 13 >>> print(f"{player1.nick} attacked {player2.nick}")
# 14 John attacked Mike
# 15
# 16 # Odczytanie zmienionych wartości pól obiektów
# 17 >>> print(f"{player1.nick}: health={player1.health}, level={player1.level}")
# 18 John: health=100, level=1
# 19 >>> print(f"{player2.nick}: health={player2.health}, level={player2.level}")
# 20 Mike: health=90, level=1
# 21
# 22 # Uzdrawianie gracza
# 23 >>> player2.heal()
# 24 >>> print(f"{player2.nick} healed himself")
# 25 Mike healed himself
# 26
# 27 # Odczytanie zmienionych wartości pól obiektów
# 28 >>> print(f"{player1.nick}: health={player1.health}, level={player1.level}")
# 29 John: health=100, level=1
# 30 >>> print(f"{player2.nick}: health={player2.health}, level={player2.level}")
# 31 Mike: health=100, level=2
# 32
# 33 # Zmiana wartości pola health przy u˙zyciu wła´sciwo´sci health
# 34 >>> player1.health = 80
# 35 >>> print(f"{player1.nick} health value changed to {player1.health}")
# 36 John health value changed to 80
# 37
# 38 # Odczytanie zmienionych wartości pól obiektów
# 39 >>> print(f"{player1.nick}: health={player1.health}, level={player1.level}")
# 40 John: health=80, level=1
# 41 >>> print(f"{player2.nick}: health={player2.health}, level={player2.level}")
# 42 Mike: health=100, level=2


class Player:
    def __init__(self, nick):
        self.nick = nick
        self.__health = 100
        self._score = 0

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        elif value > 100:
            self.__health = 100
        else:
            self.__health = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = max(value, 0)  # Zapobiegamy negatywnym wynikom.

    @property
    def level(self):
        """Oblicza poziom gracza na podstawie jego wyniku (_score)."""
        return self._score // 100 + 1

    def attack(self, enemy):
        """Metoda umożliwiająca atak na przeciwnika."""
        if enemy.health > 0:
            enemy.health -= 10  # Zmniejszenie zdrowia przeciwnika o 10.
            self.score += 10  # Dodanie punktów do wyniku za atak.
            print(f"{self.nick} attacked {enemy.nick}")

    def heal(self):
        """Metoda umożliwiająca leczenie gracza. Wygląda też w przykładzie, że leczenie daje +1 do level"""
        self.health += 10  # Zwiększenie zdrowia gracza o 10.
        print(f"{self.nick} healed himself")

    def __str__(self):
        """Metoda magiczna str do zwracania reprezentacji tekstowej obiektu."""
        return f"{self.nick}: health={self.health}, level={self.level}"


# Tworzenie obiektów klasy Player
player1 = Player("John")
player2 = Player("Mike")

# Odczytanie początkowych wartości pól obiektów
print(f"{player1.nick}: health={player1.health}, level={player1.level}")
# 7 John: health=100, level=1

print(f"{player2.nick}: health={player2.health}, level={player2.level}")
# 9 Mike: health=100, level=1

# Atakowanie przeciwnika
player1.attack(player2)
print(f"{player1.nick} attacked {player2.nick}")
# 14 John attacked Mike

# Odczytanie zmienionych wartości pól obiektów
print(f"{player1.nick}: health={player1.health}, level={player1.level}")
# 18 John: health=100, level=1

print(f"{player2.nick}: health={player2.health}, level={player2.level}")
# 20 Mike: health=90, level=1

# 22 # Uzdrawianie gracza
player2.heal()
print(f"{player2.nick} healed himself")
# 25 Mike healed himself

# 27 # Odczytanie zmienionych wartości pól obiektów
print(f"{player1.nick}: health={player1.health}, level={player1.level}")
# 29 John: health=100, level=1
print(f"{player2.nick}: health={player2.health}, level={player2.level}")
# 31 Mike: health=100, level=2 - tego nie potrafię zrozumieć? Skąd ten level 2?
# CZyżby po uleczemnieu się miał być levelUp... as well?

# 33 # Zmiana wartości pola health przy użyciu właściwości health
player1.health = 80
print(f"{player1.nick} health value changed to {player1.health}")
# 36 John health value changed to 80

# 38 # Odczytanie zmienionych wartości pól obiektów
print(f"{player1.nick}: health={player1.health}, level={player1.level}")
# 40 John: health=80, level=1
print(f"{player2.nick}: health={player2.health}, level={player2.level}")
# 42 Mike: health=100, level=2 - tego nie potrafię zrozumieć? Skąd ten level 2?


player1.score = 250
print(f"{player1.nick}: health={player1.health}, level={player1.level}")
