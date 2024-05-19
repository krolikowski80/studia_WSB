# # Zadanie 2.1 Zwierzęta
# # Utwórz dwie klasy: jedna klasa bazowa oraz dwie klasy dziedziczące po niej. Klasę bazową nazwij Ssak, a dwie
# # kolejne dowolnymi zwierzętami które są ssakami. Klasa bazowa powinna posiadać pole do definiowanego obiektu o
# # nazwie info oraz metodę o nazwie ciekawostka, gdzie info jest polem publicznym (posiada wartość domyślną), a
# # ciekawostka metodą publiczną wyświetlającą pole info. Wszystkie klasy powinny posiadać zmienną (pole klasy) o
# # nazwie rodzaj. W konstruktorze klasy Ssak powinna być wyświetlana informacja o rodzaju obiektu. Do dziedziczonego
# # konstruktora klasy bazowej powinien być przekazywany parametr info z klasy dziedziczonej. Poniżej znajduje
# # się przykład utworzenia dwóch obiektów wraz z wywoływaniem dla nich metody ciekawostka.
# # Listing 1: Przykład
# # s = Ssak()
# # Stworzyłeś: Ssak
# # s.ciekawostka()
# # Brak ciekawostki
# # p = Pies()
# # Stworzyłeś: Pies
# # p.ciekawostka()
# # Ma cztery łapy

# class Ssak:
#     """Klasa bazowa dla ssaków."""
#     rodzaj = "Ssak"

#     def __init__(self, info='Brak ciekawostki'):
#         """Inicjalizacja ssaka z podstawową informacją."""
#         self.info = info
#         print(f"Stworzyłeś: {self.rodzaj}")

#     def ciekawostka(self):
#         """Wyświetla ciekawostkę o ssaku."""
#         print(self.info)


# class Pies(Ssak):
#     """Klasa reprezentująca psa, dziedzicząca po klasie Ssak."""
#     rodzaj = "Pies"

#     def __init__(self, info="Ma cztery łapy"):
#         """Inicjalizacja psa z informacją specyficzną dla psa."""
#         super().__init__(info)


# class Kot(Ssak):
#     """Klasa reprezentująca kota, dziedzicząca po klasie Ssak."""
#     rodzaj = "Kot"

#     def __init__(self, info="Lubi polować na myszy"):
#         """Inicjalizacja kota z informacją specyficzną dla kota."""
#         super().__init__(info)


# # Tworzenie obiektu klasy Ssak
# s = Ssak()
# s.ciekawostka()

# # Tworzenie obiektu klasy Pies
# p = Pies()
# p.ciekawostka()

# # Tworzenie obiektu klasy Kot
# k = Kot()
# k.ciekawostka()

# #------------------------------------------------------------------------------------------------------------------

# # Zadanie 2.2 Zegar
# # Napisz program, który definiuje trzy klasy tj. Zegar, ZegarElektroniczny oraz ZegarCzwartyWymiar, gdzie:
# # • Zegar ma pola: godzina, minuta, sekunda. Posiada także metodę ustaw_czas(), która pozwala na ustawienie
# # godziny, minuty i sekundy.
# # • ZegarElektroniczny dziedziczy po klasie Zegar i dodaje pola: dni_tygodnia, dzien_miesiaca, miesiac,
# # rok. Metoda ustaw_czas() zostaje nadpisana w celu uwzględnienia nowych pól.
# # • ZegarCzwartyWymiar dziedziczy po klasie ZegarElektroniczny i dodaje pole czas_kwantowy. Metoda ustaw_czas()
# # zostaje ponownie nadpisana.
# # Przykład
# # zegar = Zegar()
# # zegar.ustaw_czas(12, 30, 0)
# # print("Zegar:", zegar)
# # Zegar: 12:30:00
# # zegar_elektroniczny = ZegarElektroniczny()
# # zegar_elektroniczny.ustaw_czas(12, 30, 0, 2, 22, 3, 2023)
# # print("ZegarElektroniczny:", zegar_elektroniczny)
# # ZegarElektroniczny: 12:30:00, 22-03-2023
# # zegar_czwarty_wymiar = ZegarCzwartyWymiar()
# # zegar_czwarty_wymiar.ustaw_czas(12, 30, 0, 2, 22, 3, 2023, 0.5)
# # print("ZegarCzwartyWymiar:", zegar_czwarty_wymiar)
# # ZegarCzwartyWymiar: 12:30:00, 22-03-2023, 0.5

# class Zegar:
#     def __init__(self, godzina=0, minuta=0, sekunda=0):
#         self.godzina = godzina
#         self.minuta = minuta
#         self.sekunda = sekunda

#     def ustaw_czas(self, godzina, minuta, sekunda):
#         self.godzina = godzina
#         self.minuta = minuta
#         self.sekunda = sekunda

#     def __str__(self):
#         return f"{self.godzina:02d}:{self.minuta:02d}:{self.sekunda:02d}"


# class ZegarElektroniczny(Zegar):
#     def __init__(self, godzina=0, minuta=0, sekunda=0, dni_tygodnia=1, dzien_miesiaca=1, miesiac=1, rok=2000):
#         super().__init__(godzina, minuta, sekunda)
#         self.dni_tygodnia = dni_tygodnia
#         self.dzien_miesiaca = dzien_miesiaca
#         self.miesiac = miesiac
#         self.rok = rok

#     def ustaw_czas(self, godzina, minuta, sekunda, dni_tygodnia, dzien_miesiaca, miesiac, rok):
#         super().ustaw_czas(godzina, minuta, sekunda)
#         self.dni_tygodnia = dni_tygodnia
#         self.dzien_miesiaca = dzien_miesiaca
#         self.miesiac = miesiac
#         self.rok = rok

#     def __str__(self):
#         return f"{super().__str__()} {self.dni_tygodnia} {self.dzien_miesiaca:02d}/{self.miesiac:02d}/{self.rok}"


# class ZegarCzwartyWymiar(ZegarElektroniczny):
#     def __init__(self, godzina=0, minuta=0, sekunda=0, dni_tygodnia=1, dzien_miesiaca=1, miesiac=1, rok=2000, czas_kwantowy=0):
#         super().__init__(godzina, minuta, sekunda,
#                          dni_tygodnia, dzien_miesiaca, miesiac, rok)
#         self.czas_kwantowy = czas_kwantowy

#     def ustaw_czas(self, godzina, minuta, sekunda, dni_tygodnia, dzien_miesiaca, miesiac, rok, czas_kwantowy):
#         super().ustaw_czas(godzina, minuta, sekunda,
#                            dni_tygodnia, dzien_miesiaca, miesiac, rok)
#         self.czas_kwantowy = czas_kwantowy

#     def __str__(self):
#         return f"{super().__str__()} Czas kwantowy: {self.czas_kwantowy}"


# # Przykłady
# zegar = Zegar()
# zegar.ustaw_czas(12, 30, 0)
# print("Zegar:", zegar)
# # Zegar: 12:30:00

# zegar_elektroniczny = ZegarElektroniczny()
# zegar_elektroniczny.ustaw_czas(12, 30, 0, 2, 22, 3, 2023)
# print("ZegarElektroniczny:", zegar_elektroniczny)
# # ZegarElektroniczny: 12:30:00, 22-03-2023

# zegar_czwarty_wymiar = ZegarCzwartyWymiar()
# zegar_czwarty_wymiar.ustaw_czas(12, 30, 0, 2, 22, 3, 2023, 0.5)
# print("ZegarCzwartyWymiar:", zegar_czwarty_wymiar)
# # ZegarCzwartyWymiar: 12:30:00, 22-03-2023, 0.5
