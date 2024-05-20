# Zadanie 2.1 Zwierzęta
# Utwórz dwie klasy: jedna klasa bazowa oraz dwie klasy dziedziczące po niej. Klasę bazową nazwij Ssak, a dwie
# kolejne dowolnymi zwierzętami które są ssakami. Klasa bazowa powinna posiadać pole do definiowanego obiektu o
# nazwie info oraz metodę o nazwie ciekawostka, gdzie info jest polem publicznym (posiada wartość domyślną), a
# ciekawostka metodą publiczną wyświetlającą pole info. Wszystkie klasy powinny posiadać zmienną (pole klasy) o
# nazwie rodzaj. W konstruktorze klasy Ssak powinna być wyświetlana informacja o rodzaju obiektu. Do dziedziczonego
# konstruktora klasy bazowej powinien być przekazywany parametr info z klasy dziedziczonej. Poniżej znajduje
# się przykład utworzenia dwóch obiektów wraz z wywoływaniem dla nich metody ciekawostka.
# Przykład
# s = Ssak()
# Stworzyłeś: Ssak
# s.ciekawostka()
# Brak ciekawostki
# p = Pies()
# Stworzyłeś: Pies
# p.ciekawostka()
# Ma cztery łapy

class Ssak:
    """Klasa bazowa dla ssaków."""
    rodzaj = "Ssak"

    def __init__(self, info='Brak ciekawostki'):
        """Inicjalizacja ssaka z podstawową informacją."""
        self.info = info
        print(f"Stworzyłeś: {self.rodzaj}")

    def ciekawostka(self):
        """Wyświetla ciekawostkę o ssaku."""
        print(self.info)


class Pies(Ssak):
    """Klasa reprezentująca psa, dziedzicząca po klasie Ssak."""
    rodzaj = "Pies"

    def __init__(self, info="Ma cztery łapy"):
        """Inicjalizacja psa z informacją specyficzną dla psa."""
        super().__init__(info)


class Kot(Ssak):
    """Klasa reprezentująca kota, dziedzicząca po klasie Ssak."""
    rodzaj = "Kot"

    def __init__(self, info="Lubi polować na myszy"):
        """Inicjalizacja kota z informacją specyficzną dla kota."""
        super().__init__(info)


# Tworzenie obiektu klasy Ssak
s = Ssak()
s.ciekawostka()

# Tworzenie obiektu klasy Pies
p = Pies()
p.ciekawostka()

# Tworzenie obiektu klasy Kot
k = Kot()
k.ciekawostka()

#------------------------------------------------------------------------------------------------------------------

# Zadanie 2.2 Zegar
# Napisz program, który definiuje trzy klasy tj. Zegar, ZegarElektroniczny oraz ZegarCzwartyWymiar, gdzie:
# • Zegar ma pola: godzina, minuta, sekunda. Posiada także metodę ustaw_czas(), która pozwala na ustawienie
# godziny, minuty i sekundy.
# • ZegarElektroniczny dziedziczy po klasie Zegar i dodaje pola: dni_tygodnia, dzien_miesiaca, miesiac,
# rok. Metoda ustaw_czas() zostaje nadpisana w celu uwzględnienia nowych pól.
# • ZegarCzwartyWymiar dziedziczy po klasie ZegarElektroniczny i dodaje pole czas_kwantowy. Metoda ustaw_czas()
# zostaje ponownie nadpisana.

class Zegar:
    def __init__(self, godzina=0, minuta=0, sekunda=0):
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda

    def ustaw_czas(self, godzina, minuta, sekunda):
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda

    def __str__(self):
        return f"{self.godzina:02d}:{self.minuta:02d}:{self.sekunda:02d}"


class ZegarElektroniczny(Zegar):
    def __init__(self, godzina=0, minuta=0, sekunda=0, dni_tygodnia=1, dzien_miesiaca=1, miesiac=1, rok=2000):
        super().__init__(godzina, minuta, sekunda)
        self.dni_tygodnia = dni_tygodnia
        self.dzien_miesiaca = dzien_miesiaca
        self.miesiac = miesiac
        self.rok = rok

    def ustaw_czas(self, godzina, minuta, sekunda, dni_tygodnia, dzien_miesiaca, miesiac, rok):
        super().ustaw_czas(godzina, minuta, sekunda)
        self.dni_tygodnia = dni_tygodnia
        self.dzien_miesiaca = dzien_miesiaca
        self.miesiac = miesiac
        self.rok = rok

    def __str__(self):
        return f"{super().__str__()} {self.dni_tygodnia} {self.dzien_miesiaca:02d}/{self.miesiac:02d}/{self.rok}"


class ZegarCzwartyWymiar(ZegarElektroniczny):
    def __init__(self, godzina=0, minuta=0, sekunda=0, dni_tygodnia=1, dzien_miesiaca=1, miesiac=1, rok=2000, czas_kwantowy=0):
        super().__init__(godzina, minuta, sekunda,
                         dni_tygodnia, dzien_miesiaca, miesiac, rok)
        self.czas_kwantowy = czas_kwantowy

    def ustaw_czas(self, godzina, minuta, sekunda, dni_tygodnia, dzien_miesiaca, miesiac, rok, czas_kwantowy):
        super().ustaw_czas(godzina, minuta, sekunda,
                           dni_tygodnia, dzien_miesiaca, miesiac, rok)
        self.czas_kwantowy = czas_kwantowy

    def __str__(self):
        return f"{super().__str__()} Czas kwantowy: {self.czas_kwantowy}"


# Przykłady
zegar = Zegar()
zegar.ustaw_czas(12, 30, 0)
print("Zegar:", zegar)
# Zegar: 12:30:00

zegar_elektroniczny = ZegarElektroniczny()
zegar_elektroniczny.ustaw_czas(12, 30, 0, 2, 22, 3, 2023)
print("ZegarElektroniczny:", zegar_elektroniczny)
# ZegarElektroniczny: 12:30:00, 22-03-2023

zegar_czwarty_wymiar = ZegarCzwartyWymiar()
zegar_czwarty_wymiar.ustaw_czas(12, 30, 0, 2, 22, 3, 2023, 0.5)
print("ZegarCzwartyWymiar:", zegar_czwarty_wymiar)
# ZegarCzwartyWymiar: 12:30:00, 22-03-2023, 0.5

# ------------------------------------------------------------------------------------------------
# Zadanie 2.3 Książka
# Utwórz klasę Ksiazka, reprezentującą książkę, posiadającą pola takie jak tytul, autor oraz cena. Klasa powinna
# posiadać metody magiczne __repr__ oraz __str__. A następnie stwórz:
# • Klasę pochodną po klasie Ksiazka o nazwie KsiazkaFantasy, która będzie posiadała dodatkowe pole o nazwie
# podgatunek_fantasy.
# • Klasę pochodną po klasie Ksiazka o nazwie KsiazkaKryminalna, która będzie posiadała dodatkowe pole o
# nazwie liczba_zabojst.
# • Dla chętnych: Klasę o nazwie KsiazkaFantastycznoKryminalna, która będzie dziedziczyć zarówno po
# klasie KsiazkaFantasy oraz KsiazkaKryminalna. Podpowiedź: Zmienić implementację klas żeby używały
# **kwargs.
# • Klasę o nazwie Biblioteka, która będzie posiadała listę dostępnych książek oraz słownik wypożyczonych książek
# przez zadane osoby. Dodatkowo klasa musi posiadać metody lista_ksiazek, dodaj_ksiazke, wypozycz
# oraz zwroc. Funkcjonalność tych metod jest następująca:
# – lista_ksiazek - wyświetla dostępne książki w bibliotece (należy pamiętać o niewyświetlaniu książek
# wypożyczonych). W przypadku braku książek wyświetla że brakuje książek w bibliotece.
# – dodaj_ksiazke - dodaje zadaną książkę do listy książek
# – wypozycz - dodaje do słownika o kluczu książka zadaną osobę. Posiada takie argumenty jak ksiazka
# oraz osoba. Należy zaimplementować funkcję w taki sposób aby wyświetlała czy książka jest dostępna w
# bibliotece bądź czy jest wypożyczona przez inną osobę.
# – zwroc - usunie zadaną książkę ze słownika wypożyczonych książek. W innym przypadku wyświetli że
# książka nie jest wypożyczona.
# UWAGA! Zaopatrz klasy pochodne w obsługę metod magicznych związanych z wyświetlaniem.

class Ksiazka:
    """
    Klasa reprezentująca książkę.

    Atrybuty:
        tytul (str): Tytuł książki.
        autor (str): Autor książki.
        cena (float): Cena książki.
    """

    def __init__(self, tytul, autor, cena):
        self.tytul = tytul
        self.autor = autor
        self.cena = cena

    def __str__(self):
        """
        Zwraca stringową reprezentację książki.
        """
        return f"{self.tytul}, autor: {self.autor}, cena: {self.cena}"

    def __repr__(self):
        """
        Zwraca reprezentację książki.
        """
        return f"Ksiazka(tytul='{self.tytul}', autor='{self.autor}', cena={self.cena})"


class KsiazkaFantasy(Ksiazka):
    """
    Klasa reprezentująca książkę fantasy, dziedzicząca po klasie Ksiazka.

    Atrybuty:
        podgatunek_fantasy (str): Podgatunek fantasy książki.
    """

    def __init__(self, tytul, autor, cena, podgatunek_fantasy):
        super().__init__(tytul, autor, cena)
        self.podgatunek_fantasy = podgatunek_fantasy

    def __str__(self):
        """
        Zwraca stringową reprezentację książki fantasy.
        """
        return super().__str__() + f", podgatunek fantasy: {self.podgatunek_fantasy}"

    def __repr__(self):
        """
        Zwraca reprezentację książki fantasy.
        """
        return f"KsiazkaFantasy(tytul='{self.tytul}', autor='{self.autor}', cena={self.cena}, podgatunek_fantasy='{self.podgatunek_fantasy}')"


class KsiazkaKryminalna(Ksiazka):
    """
    Klasa reprezentująca książkę kryminalną, dziedzicząca po klasie Ksiazka.

    Atrybuty:
        liczba_zabojstw (int): Liczba zabójstw w książce.
    """

    def __init__(self, tytul, autor, cena, liczba_zabojstw):
        super().__init__(tytul, autor, cena)
        self.liczba_zabojstw = liczba_zabojstw

    def __str__(self):
        """
        Zwraca stringową reprezentację książki kryminalnej.
        """
        return super().__str__() + f", liczba zabójstw: {self.liczba_zabojstw}"

    def __repr__(self):
        """
        Zwraca reprezentację książki kryminalnej.
        """
        return f"KsiazkaKryminalna(tytul='{self.tytul}', autor='{self.autor}', cena={self.cena}, liczba_zabojstw={self.liczba_zabojstw})"


class KsiazkaFantastycznoKryminalna(KsiazkaFantasy, KsiazkaKryminalna):
    """
    Klasa reprezentująca książkę fantastyczno-kryminalną, dziedzicząca po klasach KsiazkaFantasy i KsiazkaKryminalna.

    Atrybuty:
        podgatunek_fantasy (str): Podgatunek fantasy książki.
        liczba_zabojstw (int): Liczba zabójstw w książce.
    """

    def __init__(self, tytul, autor, cena, podgatunek_fantasy, liczba_zabojstw):
        # Inicjalizacja pól z klas bazowych
        Ksiazka.__init__(self, tytul, autor, cena)
        self.podgatunek_fantasy = podgatunek_fantasy
        self.liczba_zabojstw = liczba_zabojstw

    def __str__(self):
        """
        Zwraca stringową reprezentację książki fantastyczno-kryminalnej.
        """
        return Ksiazka.__str__(self) + f", podgatunek fantasy: {self.podgatunek_fantasy}, liczba zabójstw: {self.liczba_zabojstw}"

    def __repr__(self):
        """
        Zwraca reprezentację książki fantastyczno-kryminalnej.
        """
        return f"KsiazkaFantastycznoKryminalna(tytul='{self.tytul}', autor='{self.autor}', cena={self.cena}, podgatunek_fantasy='{self.podgatunek_fantasy}', liczba_zabojstw={self.liczba_zabojstw})"


class Biblioteka:
    """
    Klasa reprezentująca bibliotekę.

    Atrybuty:
        dostepne_ksiazki (list): Lista dostępnych książek w bibliotece.
        wypozyczone_ksiazki (dict): Słownik wypożyczonych książek z przypisanymi osobami.
    """

    def __init__(self):
        self.dostepne_ksiazki = []
        self.wypozyczone_ksiazki = {}

    def lista_ksiazek(self):
        """
        Wyświetla dostępne książki w bibliotece.
        """
        if not self.dostepne_ksiazki:
            print("Brakuje książek w bibliotece.")
        else:
            for ksiazka in self.dostepne_ksiazki:
                print(ksiazka)

    def dodaj_ksiazke(self, ksiazka):
        """
        Dodaje książkę do listy dostępnych książek w bibliotece.

        Argumenty:
            ksiazka (Ksiazka): Książka do dodania.
        """
        self.dostepne_ksiazki.append(ksiazka)

    def wypozycz(self, ksiazka, osoba):
        """
        Wypożycza książkę osobie.

        Argumenty:
            ksiazka (Ksiazka): Książka do wypożyczenia.
            osoba (str): Imię i nazwisko osoby wypożyczającej książkę.
        """
        if ksiazka in self.dostepne_ksiazki:
            self.dostepne_ksiazki.remove(ksiazka)
            self.wypozyczone_ksiazki[ksiazka] = osoba
            print(f"Wypożyczono książkę '{ksiazka.tytul}' osobie {osoba}.")
        elif ksiazka in self.wypozyczone_ksiazki:
            print(f"Książka '{ksiazka.tytul}' jest już wypożyczona przez {
                  self.wypozyczone_ksiazki[ksiazka]}.")
        else:
            print(f"Książka '{ksiazka.tytul}' nie jest dostępna w bibliotece.")

    def zwroc(self, ksiazka):
        """
        Zwraca książkę do biblioteki.

        Argumenty:
            ksiazka (Ksiazka): Książka do zwrotu.
        """
        if ksiazka in self.wypozyczone_ksiazki:
            self.dostepne_ksiazki.append(ksiazka)
            del self.wypozyczone_ksiazki[ksiazka]
            print(f"Książka '{ksiazka.tytul}' została zwrócona.")
        else:
            print(f"Książka '{ksiazka.tytul}' nie jest wypożyczona.")

    def lista_wypozyczonych(self):
        """
        Wyświetla listę wypożyczonych książek.
        """
        if not self.wypozyczone_ksiazki:
            print("Brak wypożyczonych książek.")
        else:
            for ksiazka, osoba in self.wypozyczone_ksiazki.items():
                print(f"{ksiazka.tytul}, wypożyczona przez: {osoba}")


# Tworzenie kilku książek
ksiazka1 = Ksiazka("Dune", "Frank Herbert", 39.99)
ksiazka2 = KsiazkaFantasy(
    "Władca Pierścieni", "J.R.R. Tolkien", 49.99, "high fantasy")
ksiazka3 = KsiazkaKryminalna(
    "Zbrodnia i kara", "Fiodor Dostojewski", 29.99, 10)
ksiazka4 = KsiazkaFantastycznoKryminalna(
    "Miasto Cienia", "Cassandra Clare", 59.99, "urban fantasy", 5)

# Tworzenie biblioteki i dodawanie książek
biblioteka = Biblioteka()
biblioteka.dodaj_ksiazke(ksiazka1)
biblioteka.dodaj_ksiazke(ksiazka2)
biblioteka.dodaj_ksiazke(ksiazka3)
biblioteka.dodaj_ksiazke(ksiazka4)

# Wyświetlanie listy książek
print("Dostępne książki w bibliotece:")
biblioteka.lista_ksiazek()

# Wypożyczanie książek
biblioteka.wypozycz(ksiazka2, "Jan Kowalski")
biblioteka.wypozycz(ksiazka4, "Adam Nowak")

# Wyświetlanie listy wypożyczonych książek
print("\nWypożyczone książki:")
biblioteka.lista_wypozyczonych()

# Zwracanie książek
biblioteka.zwroc(ksiazka2)
biblioteka.zwroc(ksiazka4)

# Wyświetlanie listy książek i wypożyczonych książek po zwrocie
print("\nDostępne książki w bibliotece po zwrocie:")
biblioteka.lista_ksiazek()

print("\nWypożyczone książki po zwrocie:")
biblioteka.lista_wypozyczonych()

# --------------------------------------------------------------------------------
# 2.4 Meble
# Stwórz klasę Furniture, która będzie miała pola __material (pole prywatne) i size (pole publiczne), oraz metody
# do ustawiania i pobierania materiału zaimplementowane z wykorzystaniem dekoratora @property.
# Następnie stwórz klasę Table dziedziczącą po klasie Furniture oraz dodaj do niej pole __legs (pole prywatne)
# i dekorator @property dla pola __legs.
#
# Stwórz klasę Chair dziedziczącą po klasie Furniture oraz dodaj do niej pole __has_armrests (pole prywatne)
# i dekorator @property dla pola __has_armrests.
# Przykład
# table = Table(’wood’, ’large’, 4)
# chair = Chair(’metal’, ’medium’, True)
#
# print(’Table material:’, table.material)
# Table material: wood
# table.material = ’plastic’
# print(’Table material after modification:’, table.material)
# Table material after modification: plastic
# print(’Table size:’, table.size)
# Table size: large
# print(’Table legs:’, table.legs)
# Table legs: 4
#
# table.legs = 6
# print(’Table legs after modification:’, table.legs)
# Table legs after modification: 6
#
# print(’Chair material:’, chair.material)
# Chair material: metal
# print(’Chair size:’, chair.size)
# Chair size: medium
# print(’Chair has armrests:’, chair.has_armrests)
# Chair has armrests: True
#
# chair.has_armrests = False
# print(’Chair has armrests after modificatio

class Furniture:
    """
    Klasa reprezentująca meble.

    Atrybuty:
        __material (str): Materiał mebli (pole prywatne).
        size (str): Rozmiar mebli (pole publiczne).
    """

    def __init__(self, material, size):
        self.__material = material  # Pole prywatne
        self.size = size  # Pole publiczne

    @property
    def material(self):
        """
        Getter dla pola __material.

        Zwraca:
            str: Materiał mebli.
        """
        return self.__material

    @material.setter
    def material(self, material):
        """
        Setter dla pola __material.

        Argumenty:
            material (str): Nowy materiał mebli.
        """
        self.__material = material

    def __str__(self):
        """
        Zwraca stringową reprezentację mebli.
        """
        return f"Material: {self.__material}, Size: {self.size}"


class Table(Furniture):
    """
    Klasa reprezentująca stół, dziedzicząca po klasie Furniture.

    Atrybuty:
        __legs (int): Liczba nóg stołu (pole prywatne).
    """

    def __init__(self, material, size, legs):
        super().__init__(material, size)
        self.__legs = legs  # Pole prywatne

    @property
    def legs(self):
        """
        Getter dla pola __legs.

        Zwraca:
            int: Liczba nóg stołu.
        """
        return self.__legs

    @legs.setter
    def legs(self, legs):
        """
        Setter dla pola __legs.

        Argumenty:
            legs (int): Nowa liczba nóg stołu.
        """
        self.__legs = legs

    def __str__(self):
        """
        Zwraca stringową reprezentację stołu.
        """
        return f"{super().__str__()}, Legs: {self.__legs}"


class Chair(Furniture):
    """
    Klasa reprezentująca krzesło, dziedzicząca po klasie Furniture.

    Atrybuty:
        __has_armrests (bool): Czy krzesło ma podłokietniki (pole prywatne).
    """

    def __init__(self, material, size, has_armrests):
        super().__init__(material, size)
        self.__has_armrests = has_armrests  # Pole prywatne

    @property
    def has_armrests(self):
        """
        Getter dla pola __has_armrests.

        Zwraca:
            bool: Czy krzesło ma podłokietniki.
        """
        return self.__has_armrests

    @has_armrests.setter
    def has_armrests(self, has_armrests):
        """
        Setter dla pola __has_armrests.

        Argumenty:
            has_armrests (bool): Czy krzesło ma podłokietniki.
        """
        self.__has_armrests = has_armrests

    def __str__(self):
        """
        Zwraca stringową reprezentację krzesła.
        """
        return f"{super().__str__()}, Has armrests: {self.__has_armrests}"


# Przykłady
table = Table('wood', 'large', 4)
chair = Chair('metal', 'medium', True)

print('Table material:', table.material)  # Wyświetla: wood
table.material = 'plastic'
print('Table material after modification:',
      table.material)  # Wyświetla: plastic
print('Table size:', table.size)  # Wyświetla: large
print('Table legs:', table.legs)  # Wyświetla: 4

table.legs = 6
print('Table legs after modification:', table.legs)  # Wyświetla: 6

print('Chair material:', chair.material)  # Wyświetla: metal
print('Chair size:', chair.size)  # Wyświetla: medium
print('Chair has armrests:', chair.has_armrests)  # Wyświetla: True

chair.has_armrests = False
print('Chair has armrests after modification:',
      chair.has_armrests)  # Wyświetla: False
