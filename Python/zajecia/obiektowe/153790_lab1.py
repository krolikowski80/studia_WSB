# Zadanie 3.1 Samochód i droga
# Stwórz klasę o nazwie "Samochod", która będzie miała atrybuty takie jak marka, model, rok produkcji oraz prędkość
# maksymalna. Dodaj konstruktor, który będzie przyjmował wartości tych atrybutów, a także destruktor, który będzie
# wyświetlał informację o zniszczeniu obiektu.
# Stwórz klasę o nazwie "Droga", która będzie miała atrybuty takie jak rodzaj oraz maksymalna prędkość. Dodaj
# konstruktor, który będzie przyjmował wartości tych atrybutów.
# Dodatkowo do klasy "Samochod", dodaj metodę o nazwie "jedź", która będzie przyjmowała wartość prędkości
# oraz obiekt klasy "Droga"i wypisywała komunikat o tym, że samochód jedzie z podaną prędkością oraz o ile km/h
# przekracza maksymalną prędkość w zależności od obiektu "Droga".
#
# Przykład:
# 1 >>> moj_samochod = Samochod("Ferrari", "250 GTO", 2019)
# 2 >>> moja_droga = Droga("Autostrada", 140)
# 3 >>> moj_samochod.jedz(200, moja_droga)
# 4 Samochód marki Ferrari, model 250 GTO z 2019 roku jedzie z pr˛edko´sci ˛ a 200 km/h.
# 5 Przekraczasz maksymalną prędkość o 60 km/h na drodze rodzaju Autostrada!


class Samochod:
    def __init__(self, marka, model, rok_produkcji, predkosc_maksymalna):
        """Konstruktor klasy Samochod"""
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.predkosc_maksymalna = predkosc_maksymalna

    def __del__(self):
        """Destruktor klasy Samochod"""
        print(
            f"Samochód {self.marka} {self.model} z {self.rok_produkcji} roku został zniszczony."
        )

    def jedz(self, predkosc, droga):
        """Metoda, która przyjmuje jako argumenty wartość prędkości i sprawdza, czy prędkość jest wyższa niż maksymalna prędkość samochodu"""
        if predkosc > self.predkosc_maksymalna:
            print(
                f"Nie jesteś w stanie jechać z prędkością {predkosc} km/h, ponieważ przekracza ona maksymalną prędkość tego samochodu {self.predkosc_maksymalna} km/h. Używam maksymalnej prędkości samochodu do obliczeń."
            )
            predkosc = self.predkosc_maksymalna

        print(
            f"Samochód marki {self.marka}, model {self.model} z {self.rok_produkcji} roku jedzie z prędkością {predkosc} km/h."
        )
        if predkosc > droga.maksymalna_predkosc:
            przekroczenie = predkosc - droga.maksymalna_predkosc
            print(
                f"Przekraczasz maksymalną prędkość o {przekroczenie} km/h na drodze rodzaju {droga.rodzaj}!"
            )


class Droga:
    def __init__(self, rodzaj, maksymalna_predkosc):
        """Konstruktor klasy Droga"""
        self.rodzaj = rodzaj
        self.maksymalna_predkosc = maksymalna_predkosc


moj_samochod = Samochod("Ferrari", "250 GTO", 2019, 280)
moja_droga = Droga("Autostrada", 140)
moj_samochod.jedz(300, moja_droga)

# ---------------------------------------------------------------------

# Zad. 3.2 Konto bankowe
# Stwórz klasę o nazwie "KontoBankowe", która będzie miała atrybuty takie jak numer konta, imię właściciela, nazwisko
# właściciela oraz saldo. Dodaj konstruktor, który będzie przyjmował wartości tych atrybutów oraz destruktor,
# który będzie wyświetlał informację o usunięciu obiektu.
# Dodatkowo, dodaj metody o nazwach "wpłata"i "wypłata", które będą dodawać lub odejmować od salda odpowiednią
# kwotę. Metoda "wpłata"powinna przyjmować kwotę wpłaty, a metoda "wypłata"powinna sprawdzać, czy
# na koncie jest wystarczająca ilość środków, aby dokonać wypłaty i wypłacać tylko wtedy, gdy saldo na koncie jest
# większe niż kwota wypłaty.
# Przykład:
# 1 >>> moje_konto = KontoBankowe("123456789", "Jan", "Kowalski", 1000.0)
# 2 >>> moje_konto.wpłata(500.0)
# 3 Wpłata na konto o numerze 123456789 została wykonana. Aktualne saldo: 1500
# 4 >>> print(moje_konto.saldo)
# 5 1500
# 6 >>> moje_konto.wypłata(1500.0)
# 7 Wypłata z konta o numerze 123456789 została wykonana. Aktualne saldo: 0
# 8 >>> print(moje_konto.saldo)
# 9 0
# 10 Konto o numerze 123456789 należące do Jan Kowalski zostało usunięte.


class KontoBankowe:
    def __init__(self, numer_konta, imie_wlasciciela, nazwisko_wlasciciela, saldo):
        """Konstruktor klasy KontoBankowe"""
        self.numer_konta = numer_konta
        self.imie_wlasciciela = imie_wlasciciela
        self.nazwisko_wlasciciela = nazwisko_wlasciciela
        self.saldo = saldo

    def __del__(self):
        """Destruktor klasy KontoBankowe"""
        print(
            f"Konto o numerze {self.numer_konta} należące do {self.imie_wlasciciela} {self.nazwisko_wlasciciela} zostało usunięte."
        )

    def wplata(self, kwota):
        """Metoda, która przyjmuje jako argumenty wartość wpłaty"""
        self.saldo += kwota
        print(
            f"Wpłata na konto o numerze {self.numer_konta} została wykonana. Aktualne saldo: {self.saldo}"
        )

    def wyplata(self, kwota):
        """Metoda, która przyjmuje jako argumenty wartość wypłaty"""
        if self.saldo >= kwota:
            self.saldo -= kwota
            print(
                f"Wypłata z konta o numerze {self.numer_konta} została wykonana. Aktualne saldo: {self.saldo}"
            )
        else:
            print(
                f"Nie można wykonać operacji. Mie masz wystarczających środkó na koncie. Dostępne saldo: {self.saldo}"
            )


moje_konto = KontoBankowe("123456789", "Jan", "Kowalski", 1000.0)
moje_konto.wplata(500.0)
print(moje_konto.saldo)
moje_konto.wyplata(1500.0)
print(moje_konto.saldo)
moje_konto.wplata(700)
print(moje_konto.saldo)
moje_konto.wyplata(1000)
print(moje_konto.saldo)

# --------------------------------------------------------------

# Zad. 3.3 Elektrownie
# Stwórz klasę "EnergiaOdnawialna", która będzie reprezentować źródło energii odnawialnej. Klasa powinna mieć
# atrybuty nazwa (nazwa źródła), moc (moc w megawatach) oraz lokacja (lokalizacja źródła). Klasa powinna także
# mieć konstruktor, który przyjmuje argumenty nazwa, moc i lokacja i ustawia je jako atrybuty obiektu.
# Zaimplementuj metodę get_info, które zwróci informacje o elektrowni. Dodatkowo zaimplementuj metodę magiczną
# __eq__ do porównań. Rozszerz klasę o metody związane z wyświetlaniem.
# Przykład:
# 1 >>> elektrownia_wiatrowa = EnergiaOdnawialna("Wiatr", 50, "Niemcy")
# 2 >>> elektrowania_sloneczna = EnergiaOdnawialna("Slonce", 30, "Polska")
# 3 >>> elektrownia_wiatrowa.get_info()
# 4 ´Zródło: Wiatr, Moc: 50 MW, Lokalizacja: Niemcy
# 5 >>> elektrowania_sloneczna.get_info()
# 6 ´Zródło: Slonce, Moc: 30 MW, Lokalizacja: Polska
# 7 >>> elektrowania_hybrydowa = elektrownia_wiatrowa + elektrowania_sloneczna
# 8 >>> elektrowania_hybrydowa.get_info()
# 9 ´Zródło: Wiatr, Slonce, Moc: 80 MW, Lokalizacja: Polska, Niemcy
# 10 >>> print(elektrownia_wiatrowa)
# 11 ´Zródło: Wiatr, Moc: 50 MW
# 12 >>> print(elektrownia_wiatrowa == elektrowania_sloneczna)
# 13 False


class EnergiaOdnawialna:
    def __init__(self, nazwa, moc, lokacja):
        """Konstruktor klasy EnergiaOdnawialna"""
        self.nazwa = nazwa
        self.moc = moc
        self.lokacja = lokacja

    def get_info(self):
        """Metoda, która zwróci informacje o elektrowni"""
        return f"Źródło: {self.nazwa}, Moc: {self.moc} MW, Lokalizacja: {self.lokacja}"

    def __eq__(self, other):
        """Metoda, która porównuje dwa źródła"""
        return (
            self.nazwa == other.nazwa
            and self.moc == other.moc
            and self.lokacja == other.lokacja
        )

    def __str__(self):
        """Metoda, która zwróci informacje o elektrowni"""
        return f"Źródło: {self.nazwa}, Moc: {self.moc} MW"

    def __add__(self, other):
        """Metoda, która dodaje dwa źródła"""
        new_nazwa = f"{self.nazwa}, {other.nazwa}"
        new_moc = self.moc + other.moc
        new_lokacja = f"{self.lokacja}, {other.lokacja}"
        return EnergiaOdnawialna(new_nazwa, new_moc, new_lokacja)


elektrownia_wiatrowa = EnergiaOdnawialna("Wiatr", 50, "Niemcy")
elektrowania_sloneczna = EnergiaOdnawialna("Słońce", 30, "Polska")
print(elektrownia_wiatrowa.get_info())
print(elektrowania_sloneczna.get_info())
elektrowania_hybrydowa = elektrownia_wiatrowa + elektrowania_sloneczna
print(elektrowania_hybrydowa.get_info())
print(elektrownia_wiatrowa)
print(elektrownia_wiatrowa == elektrowania_sloneczna)

# --------------------------------------------------------------

# Zad. 3.4 Ułamek
# Napisać klase, reprezentującą ułamek (fraction) w postaci a/b , gdzie a jest licznikiem, b mianownikiem.
# W wyniku ma powstać kod klasy spełniający poniższe warunku oraz kod demonstrujący działanie zaimplementowanej klasy.
# Powstała klasa ma spełniać następujące warunki:


# • Tworzymy obiekt z dwóch liczb (licznik i mianownik). Przy tworzeniu klasy ułamek ma zostać skrócony (można
# użyć metody gcd z modułu math). Przy próbie podania mianowniku 0, wyrzucamy wyjątek ZeroDivisionError.

# Przykład:
# 1 >>> Fraction(3, 4)
# 2 Fraction(3, 4)
# 3 >>> Fraction(6, 12)
# 4 Fraction(1, 2)


# • Dwie metody do wypisywania obiektów naszej klasy: __repr__ i __str__. Reprezentacja musi zwracać polecenia
# którym można utworzyć nasz obiekt, a zamiana na string pokazywać postać ułamkową (patrz przykład).

# Przykład:
# 1 >>> f = Fraction(3, 4)
# 2 >>> print(repr(f))
# 3 Fraction(3, 4)
# 4 >>> print(f) # Niejawnie wywołane __str__
# 5 3/4
# 6 >>> f2 = Fraction(5, 4)
# 7 >>> print(f2) # W przypadku gdy mamy ułamek nie właściwy to oddzielamy czść całą
# 8 1 1/4

# • Obiekty klasy muszą wspierać podstawowe operacje arytmetyczne (przeciążenia operatorów): dodawanie,
# odejmowanie, mnożenie, dzielenie, wartość bezwzględna. Przy wykonaniu operacji ma powstać nowy obiekt.
# Wszystkie operacje wykonujemy tylko na obiektach naszej klasy (nie trzeba implementować mnożenia przez
# liczbę i t.d.).

# Przykład:
# 1 >>> Fraction(1, 4) + Fraction(2, 4)
# 2 Fraction(3, 4)
# • Obiekty tej klasy można porównywać (6 operatorów do przeciążenia):
# Przykład:
# 1 >>> Fraction(1, 4) < Fraction(2, 4)
# 2 True
# 3 >>> Fraction(1, 4) == Fraction(2, 4)
# 4 False

# • Klasa musi mieć zaimplementowane metody rzutowania na inne typy danych (float, int, bool).
# • Klasa musi posiadać implementacje metody __round__, żeby umożliwić zaokrąglanie jednocześnie z rzutowaniem na float.


from math import gcd  # Importuję funkcję gcd, aby móc skrócić ułamek.


class Fraction:
    def __init__(self, numerator, denominator):
        """Konstruktor klasy Fraction"""
        if denominator == 0:
            raise ZeroDivisionError(
                "Mianownik nie może być równy zero."
            )  # Sprawdzam, czy mianownik nie jest zerem.
        common_divisor = gcd(numerator, denominator)  # Skracam ułamek za pomocą gcd.
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor
        if (
            self.denominator < 0
        ):  # Jeśli mianownik jest ujemny, przenoszę znak na licznik.
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __repr__(self):
        """Metoda, która zwróci reprezentację obiektu. Zapewnia reprezentację, którą można użyć do ponownego utworzenia tego samego obiektu"""
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        """Metoda, która zwróci string reprezentujący obiekt. Zwraca ułamek w formie łańcucha tekstowego, odpowiednio formatując ułamki właściwe i niewłaściwe"""
        if abs(self.numerator) >= self.denominator:
            whole = self.numerator // self.denominator
            remainder = abs(self.numerator % self.denominator)
            if remainder == 0:
                return f"{whole}"
            else:
                return f"{whole} {remainder}/{self.denominator}"
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """Metoda, która dodaje dwa ułamki"""
        new_numerator = (
            self.numerator * other.denominator + other.numerator * self.denominator
        )
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """Metoda, która odejmuje dwa ułamki"""
        new_numerator = (
            self.numerator * other.denominator - other.numerator * self.denominator
        )
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """Metoda, która mnoży dwa ułamki"""
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """Metoda, która dzieli dwa ułamki"""
        if other.numerator == 0:
            raise ZeroDivisionError(
                "Nie można dzielić przez ułamek o liczniku równym zero."
            )
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        """Metoda, która porównuje dwa ułamki czy dwa ułamki są równe."""
        return (
            self.numerator == other.numerator and self.denominator == other.denominator
        )

    def __lt__(self, other):
        """Metoda, która porównuje czy jeden ułamek jest mniejszy od drugiego"""
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        """Metoda, którea porównuje, czy jeden ułamek jest mniejszy lub równy drugiemu"""
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        """Metoda, która porównuje, czy jeden ułamek jest większy od drugiego"""
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        """Metoda, która sprawdza, czy jeden ułamek jest większy lub równy drugiemu."""
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __bool__(self):
        """Metoda, która sprawdza, czy ułamek jest prawdziwiwy, jeśli licznik nie jest zerem."""
        return self.numerator != 0

    def __float__(self):
        """Metoda, która rzutuje ułamek na float"""
        return self.numerator / self.denominator

    def __int__(self):
        """Metoda, która rzutuje ułamek na int"""
        return self.numerator // self.denominator

    def __round__(self, ndigits=None):
        """Metoda, która zaokrągla ułamek do określonej liczby miejsc po przecinku"""
        return round(float(self), ndigits)


f = Fraction(3, 4)
f2 = Fraction(5, 4)
print(repr(f))  # "Fraction(3, 4)"
print(f)  # "3/4"
print(f2)  # "1 1/4"
print(Fraction(1, 4) + Fraction(2, 4))  # "Fraction(3, 4)"
print(Fraction(1, 4) < Fraction(2, 4))  # True
print(Fraction(1, 4) > Fraction(2, 4))  # False
print(Fraction(1, 4) == Fraction(2, 4))  # False
