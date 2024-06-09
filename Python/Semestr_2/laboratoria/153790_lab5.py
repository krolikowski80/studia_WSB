# Zadanie 3.1 Transport
# Zaimplementuj hierarchię klas w języku Python dla firmy logistycznej. Klasa abstrakcyjna będzie reprezentować
# transport, a klasy pochodne reprezentują różne środki transportu, takie jak samolot, statek i ciężarówka.
# Klasa abstrakcyjna Transport powinna mieć trzy pola: start, koniec i ładunek, które będą reprezentować miejsce
# rozpoczęcia transportu, miejsce docelowe i ładunek. Klasa abstrakcyjna powinna mieć również cztery metody:
# • transportuj - abstrakcyjna metoda, która będzie zaimplementowana w klasach pochodnych (posiada argument
# nowy_koniec)
# • get_start - zwraca miejsce rozpoczęcia transportu
# • get_koniec - zwraca miejsce docelowe transportu
# • get_ladunek - zwraca informacje o ładunku
# Klasy pochodne Samolot, Statek i Ciezarowka powinny dziedziczyć po klasie abstrakcyjnej Transport i dodawać
# dwa dodatkowe pola:
# • dla Samolot - ilosc_pasazerow, ilosc_bagazy
# • dla Statek - rodzaj_ladunku, ilosc_kontenerow
# • dla Ciezarowka - ilosc_palet, typ_ladunku
# Każda klasa pochodna powinna mieć metodę transportuj, która będzie implementowała transport dla danego
# środka transportu. Metoda ta powinna również wykorzystywać pola dziedziczone z klasy abstrakcyjnej. Metoda
# transportuj powinna realizować przemieszczenie ładunku z miejsca startu do miejsca docelowego, czyli musi zmieniać
# wartość pola start na wartość pola koniec, a wartość pola koniec zamieniać na wartość argumentu podanego
# do metody transportuj.
# W klasie Samolot, metoda transportuj ma wyglądać następująco:
# • Wyświetl komunikat, że samolot startuje z miejsca start do miejsca koniec.
# • Wyświetl informacje o ilości pasażerów i bagażu.
# • Przemieszczenie samolotu z miejsca start do miejsca koniec.
# 2
# W klasie Statek, metoda transportuj ma wyglądać następująco:
# • Wyświetl komunikat, że statek wypływa z portu start do portu koniec.
# • Wyświetl informacje o rodzaju ładunku i ilości kontenerów.
# • Przemieszczenie statku z portu start do portu koniec
# W klasie Ciezarowka, metoda transportuj może wyglądać następująco:
# • Wyświetl komunikat, że ciężarówka rusza z miejsca start do miejsca koniec.
# • Wyświetl informacje o ilości palet i typie ładunku.
# • Przemieszczenie ciężarówki z miejsca start do miejsca koniec.
# W każdej klasie pochodnej metoda transportuj powinna wykorzystywać metody dziedziczone z klasy abstrakcyjnej
# w celu pobrania informacji o miejscu startu, miejscu docelowym i ładunku. Klasy powinny również zawierać
# metodę magiczną __str__ i __repr__ w celu wyświetlenia informacji o obiekcie. Niech w przypadku tego zadania
# metoda __repr__ wywołuje zawsze metodę __str__.

# Listing 1: Przykład
# tworzenie obiektu statku
# statek = Statek("Gda´nsk", "New York", "kontenery", "Towar A", 100)
# # wywołanie metody transportuj na obiekcie statku
# statek.transportuj("Hamburg")
# Statek wypływa z Gdańsk do New York.
# 6 Rodzaj ładunku: kontenery, ilość kontenerów: 100.
# 7 Statek dotarł do New York
# # wyświetlenie informacji o statku
# print(statek)
# Statek(start=New York, koniec=Hamburg, ladunek=kontenery, rodzaj_ladunku=Towar A, ilosc_kontenerow=100)


import math
import random
from abc import ABC, abstractmethod


class Transport(ABC):
    """
    Klasa abstrakcyjna reprezentująca transport.
    """

    def __init__(self, start, koniec, ladunek):
        """
        Inicjalizacja obiektu klasy Transport.

        Parameters:
        start (str): Miejsce rozpoczęcia transportu.
        koniec (str): Miejsce docelowe transportu.
        ladunek (str): Rodzaj ładunku transportowanego.
        """
        self.start = start
        self.koniec = koniec
        self.ladunek = ladunek

    @abstractmethod
    def transportuj(self, nowy_koniec):
        """
        Abstrakcyjna metoda transportowania, implementowana w klasach pochodnych.

        Parameters:
        nowy_koniec (str): Nowe miejsce docelowe transportu.
        """
        pass

    def get_start(self):
        """
        Zwraca miejsce rozpoczęcia transportu.
        """
        return self.start

    def get_koniec(self):
        """
        Zwraca miejsce docelowe transportu.
        """
        return self.koniec

    def get_ladunek(self):
        """
        Zwraca informacje o ładunku.
        """
        return self.ladunek

    def __str__(self):
        """
        Metoda magiczna zwracająca czytelny opis obiektu.
        """
        return f"{self.__class__.__name__}(start={self.start}, koniec={self.koniec}, ladunek={self.ladunek})"

    def __repr__(self):
        """
        Metoda magiczna zwracająca reprezentację obiektu.
        """
        return self.__str__()


class Samolot(Transport):
    """
    Klasa reprezentująca transport samolotem.
    """

    def __init__(self, start, koniec, ladunek, ilosc_pasazerow, ilosc_bagazy):
        """
        Inicjalizacja obiektu klasy Samolot.

        Parameters:
        start (str): Miejsce rozpoczęcia transportu.
        koniec (str): Miejsce docelowe transportu.
        ladunek (str): Rodzaj ładunku transportowanego.
        ilosc_pasazerow (int): Ilość pasażerów.
        ilosc_bagazy (int): Ilość bagażu.
        """
        super().__init__(start, koniec, ladunek)
        self.ilosc_pasazerow = ilosc_pasazerow
        self.ilosc_bagazy = ilosc_bagazy

    def transportuj(self, nowy_koniec):
        """
        Metoda realizująca transport samolotem.

        Parameters:
        nowy_koniec (str): Nowe miejsce docelowe transportu.
        """
        print(f"Samolot startuje z {self.start} do {nowy_koniec}.")
        print(f"Ilość pasażerów: {self.ilosc_pasazerow}, ilość bagażu: {
              self.ilosc_bagazy}.")
        self.start = self.koniec
        self.koniec = nowy_koniec


class Statek(Transport):
    """
    Klasa reprezentująca transport statkiem.
    """

    def __init__(self, start, koniec, ladunek, rodzaj_ladunku, ilosc_kontenerow):
        """
        Inicjalizacja obiektu klasy Statek.

        Parameters:
        start (str): Miejsce rozpoczęcia transportu.
        koniec (str): Miejsce docelowe transportu.
        ladunek (str): Rodzaj ładunku transportowanego.
        rodzaj_ladunku (str): Rodzaj ładunku statku.
        ilosc_kontenerow (int): Ilość kontenerów.
        """
        super().__init__(start, koniec, ladunek)
        self.rodzaj_ladunku = rodzaj_ladunku
        self.ilosc_kontenerow = ilosc_kontenerow

    def transportuj(self, nowy_koniec):
        """
        Metoda realizująca transport statkiem.

        Parameters:
        nowy_koniec (str): Nowe miejsce docelowe transportu.
        """
        print(f"Statek wypływa z portu {self.start} do portu {nowy_koniec}.")
        print(f"Rodzaj ładunku: {self.rodzaj_ladunku}, ilość kontenerów: {
              self.ilosc_kontenerow}.")
        self.start = self.koniec
        self.koniec = nowy_koniec


class Ciezarowka(Transport):
    """
    Klasa reprezentująca transport ciężarówką.
    """

    def __init__(self, start, koniec, ladunek, ilosc_palet, typ_ladunku):
        """
        Inicjalizacja obiektu klasy Ciezarowka.

        Parameters:
        start (str): Miejsce rozpoczęcia transportu.
        koniec (str): Miejsce docelowe transportu.
        ladunek (str): Rodzaj ładunku transportowanego.
        ilosc_palet (int): Ilość palet.
        typ_ladunku (str): Typ ładunku.
        """
        super().__init__(start, koniec, ladunek)
        self.ilosc_palet = ilosc_palet
        self.typ_ladunku = typ_ladunku

    def transportuj(self, nowy_koniec):
        """
        Metoda realizująca transport ciężarówką.

        Parameters:
        nowy_koniec (str): Nowe miejsce docelowe transportu.
        """
        print(f"Ciężarówka rusza z {self.start} do {nowy_koniec}.")
        print(f"Ilość palet: {self.ilosc_palet}, typ ładunku: {
              self.typ_ladunku}.")
        self.start = self.koniec
        self.koniec = nowy_koniec


# Testowanie kodu
if __name__ == "__main__":
    # Tworzenie obiektów
    samolot = Samolot("Warszawa", "Londyn", "bagaz", 150, 100)
    statek = Statek("Gdańsk", "New York", "kontenery", "Towar A", 100)
    ciezarowka = Ciezarowka("Kraków", "Wrocław", "paczki", 50, "elektronika")

    # Wywołanie metody transportuj na obiektach
    samolot.transportuj("Paryż")
    statek.transportuj("Hamburg")
    ciezarowka.transportuj("Katowice")

    # Wyświetlenie informacji o obiektach
    print(samolot)
    print(statek)
    print(ciezarowka)


# -----------------------------------------------------------------------------------------
# Zadanie 3.2 Gracz i potwory
# Utworzyć klasę abstrakcyjną GameObject. Ta klasa ma posiadać konstruktor przyjmujący jako jedyny argument
# liczby punktów zdrowia obiektu. Ta klasa ma posiadać także metodę sprawdzającą czy obiekt "żyje"(zwracamy
# True jeżeli punkty zdrowia są większe od zera), oraz metodę abstrakcyjną .interact() która ma przyjmować jeden
# argument (później będzie wyjaśnione jaki).
# Po tej klasie muszą dziedziczyć trzy inne klasy: Player, Monster, oraz Door, które reprezentują odpowiednio
# gracza, potwora i drzwi.
# Żadna z utworzonych klas nie nadpisuje konstruktora, ponieważ będzie używany konstruktor z klasy bazowej.
# W klasie Player metoda .interact() musi być nadpisana, lecz nie musi ona posiadać implementacji (jeżeli
# użyć dekorator @abstractmethod i nie nadpisać tej metody w klasie odziedziczonej to nie będziemy mogli utworzyć
# obiektu tej klasy). Zakładamy, że jako argument do dej metody będzie zawsze trafiał obiekt klasy Player.
# W klasie Door metoda .interact() musi wyświetlać informacje o tym że gracz przeszedł przez drzwi.
# Wklasie Monster metoda .interact() musi zmniejszyć liczbę punktów zdrowie obiektu podanego jako argument
# (czyli gracza) o 10, następnie ustawić punkty zdrowia tego potwora na 0 i wyświetlić informacje o tym że potwór
# został zabity przez gracza.
# Po utworzeniu wyżej opisanych klas, należy napisać kod symulujący prostą grę: tworzymy obiekt gracza (obiekt
# klasy Player), następnie tworzymy listę i losowo wypełniamy ją zadaną liczbą obiektów klas Monster albo Door
# (używamy warunek który pozwoli wybrać losowo obiekt której klasy zostanie dodany do listy).
# Następnie, należy napisać pętlę, która będzie przechodziła po obiektach z tej listy i wywoływać metodę .interact()
# na obiektach z tej listy. Podajemy wcześniej utworzony obiekt gracza jako argument do tej metody (obj.inteact(player)).
# Na końcu każdej iteracji sprawdzamy czy gracz jeszcze żyje (metoda do tego była zaimplementowana w klasie bazowej).
# W przypadku gdyby grać zmarł, wyświetlamy informacje o tym i przerywamy działania pętli.
# Na listingu niżej jest pokazany przykładowy wynik działania takiego programu, założenia wstępne są takie: 10
# obiektów na liście, 50 punktów zdrowia u gracza, oraz 70% szansa że na listę zostanie dodany potwór.
#
# Listing 2: Przykład działania programu.
# 1 Gracz przeszedł przez drzwi.
# 2 Gracz przeszedł przez drzwi.
# 3 Gracz zabił potwora.
# 4 Gracz zabił potwora.
# 5 Gracz zabił potwora.
# 6 Gracz przeszedł przez drzwi.
# 7 Gracz zabił potwora.
# 8 Gracz przeszedł przez drzwi.
# 9 Gracz zabił potwora.
# 10 Gracz został zabity!

# from abc import ABC, abstractmethod


class GameObject(ABC):
    """
    Klasa abstrakcyjna reprezentująca obiekt w grze.
    """

    def __init__(self, health_points):
        """
        Konstruktor klasy GameObject.

        Parameters:
        health_points (int): Liczba punktów zdrowia obiektu.
        """
        self.health_points = health_points

    def is_alive(self):
        """
        Metoda sprawdzająca, czy obiekt jest żywy.

        Returns:
        bool: True, jeśli obiekt ma więcej niż 0 punktów zdrowia, False w przeciwnym razie.
        """
        return self.health_points > 0

    @abstractmethod
    def interact(self, player):
        """
        Abstrakcyjna metoda interakcji obiektu z graczem.

        Parameters:
        player (Player): Obiekt gracza, z którym obiekt ma interakcję.
        """
        pass


class Player(GameObject):
    """
    Klasa reprezentująca gracza w grze.
    """

    def interact(self, player):
        """
        Metoda interakcji gracza.

        Gracz nie wykonuje żadnych działań podczas interakcji.

        Parameters:
        player (Player): Obiekt gracza, z którym gracz ma interakcję.
        """
        pass


class Monster(GameObject):
    """
    Klasa reprezentująca potwora w grze.
    """

    def interact(self, player):
        """
        Metoda interakcji potwora.

        Potwór atakuje gracza, zabierając mu 10 punktów zdrowia i ustawiając swoje punkty zdrowia na 0.

        Parameters:
        player (Player): Obiekt gracza, z którym potwór ma interakcję.
        """
        player.health_points -= 10
        self.health_points = 0
        print("Potwór został zabity przez gracza.")


class Door(GameObject):
    """
    Klasa reprezentująca drzwi w grze.
    """

    def interact(self, player):
        """
        Metoda interakcji drzwi.

        Wyświetla informację o przejściu przez drzwi.

        Parameters:
        player (Player): Obiekt gracza, który przechodzi przez drzwi.
        """
        print("Gracz przeszedł przez drzwi.")


# Tworzenie obiektu gracza
player = Player(50)

# Tworzenie listy obiektów potworów i drzwi
objects = []
num_objects = 10
for _ in range(num_objects):
    # Losowanie czy dodajemy potwora czy drzwi
    if random.random() < 0.7:
        objects.append(Monster(30))
    else:
        objects.append(Door(0))

# Symulacja gry
for obj in objects:
    obj.interact(player)
    # Sprawdzenie czy gracz nadal żyje
    if not player.is_alive():
        print("Gracz został zabity!")
        break

# ------------------------------------------------------------------------
# Zadanie 3.3 Równania
# Utwórz klasę abstrakcyjną reprezentującą równanie o zadanych współczynnikach. Klasa abstrakcyjna równania musi
# posiadać konstruktor, przyjmujący listę współczynników równania, oraz metodę .solve() która musi rozwiązywać
# równanie (nie będzie posiadała żadnej implementacji w klasie abstrakcyjnej).
# Następnie stwórz dwie klasy, dziedziczące po klasie równania. Te klasy muszą reprezentować równanie liniowe i
# kwadratowe. Należy nadpisać i zaimplementować metodę .solve() która będzie rozwiązywać równanie o współczynnikach
# podanych jako argument konstruktora. Należy także nadpisać konstruktor klasy bazowej w celu sprawdzenia
# czy podana liczba współczynników odpowiada temu równaniu (sprawdzamy czy lista posiada dwa współczynniki
# dla równania liniowego albo czy posiada trzy współczynniki w przypadku równania kwadratowego).
# Listing 3: Przykład
# eq = LinearEquation([2, 0])
# eq.solve()
# x = 0
# eq1 = LinearEquation([0, 2])
# eq1.solve()
# Brak rozwiązań
# eq2 = QuadraticEquation([1, -5, 6])
# eq2.solve()
# x1 = 2, x2 = 3

# from abc import ABC, abstractmethod


class Equation(ABC):
    """
    Klasa abstrakcyjna reprezentująca równanie.
    """

    def __init__(self, coefficients):
        """
        Inicjalizacja obiektu klasy Equation.

        Parameters:
        coefficients (list): Lista współczynników równania.
        """
        self.coefficients = coefficients

    @abstractmethod
    def solve(self):
        """
        Abstrakcyjna metoda rozwiązująca równanie.
        """
        pass


class LinearEquation(Equation):
    """
    Klasa reprezentująca równanie liniowe.
    """

    def __init__(self, coefficients):
        """
        Inicjalizacja obiektu klasy LinearEquation.

        Parameters:
        coefficients (list): Lista współczynników równania liniowego.
        """
        super().__init__(coefficients)
        if len(self.coefficients) != 2:
            raise ValueError(
                "Invalid number of coefficients for a linear equation")

    def solve(self):
        """
        Metoda rozwiązująca równanie liniowe.
        """
        a, b = self.coefficients
        if a == 0:
            if b == 0:
                print("Nieskończenie wiele rozwiązań")
            else:
                print("Brak rozwiązań")
        else:
            x = -b / a
            print(f"x = {x}")


class QuadraticEquation(Equation):
    """
    Klasa reprezentująca równanie kwadratowe.
    """

    def __init__(self, coefficients):
        """
        Inicjalizacja obiektu klasy QuadraticEquation.

        Parameters:
        coefficients (list): Lista współczynników równania kwadratowego.
        """
        super().__init__(coefficients)
        if len(self.coefficients) != 3:
            raise ValueError(
                "Invalid number of coefficients for a quadratic equation")

    def solve(self):
        """
        Metoda rozwiązująca równanie kwadratowe.
        """
        a, b, c = self.coefficients
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Brak rozwiązań")
        elif delta == 0:
            x = -b / (2*a)
            print(f"x = {x}")
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print(f"x1 = {x1}, x2 = {x2}")


# Testowanie kodu
if __name__ == "__main__":
    # Tworzenie i rozwiązywanie równań
    eq = LinearEquation([2, 0])
    eq.solve()

    eq1 = LinearEquation([0, 2])
    eq1.solve()

    eq2 = QuadraticEquation([1, -5, 6])
    eq2.solve()
