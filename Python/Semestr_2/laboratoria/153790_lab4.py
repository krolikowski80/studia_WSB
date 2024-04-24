# Zadanie 2.1 Zwierzęta
# Utwórz dwie klasy: jedna klasa bazowa oraz dwie klasy dziedziczące po niej. Klasę bazową nazwij Ssak, a dwie
# kolejne dowolnymi zwierzętami które są ssakami. Klasa bazowa powinna posiadać pole do definiowanego obiektu o
# nazwie info oraz metodę o nazwie ciekawostka, gdzie info jest polem publicznym (posiada wartość domyślną), a
# ciekawostka metodą publiczną wyświetlającą pole info. Wszystkie klasy powinny posiadać zmienną (pole klasy) o
# nazwie rodzaj. W konstruktorze klasy Ssak powinna być wyświetlana informacja o rodzaju obiektu. Do dziedziczonego
# konstruktora klasy bazowej powinien być przekazywany parametr info z klasy dziedziczonej. Poniżej znajduje
# się przykład utworzenia dwóch obiektów wraz z wywoływaniem dla nich metody ciekawostka.
# Listing 1: Przykład
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
