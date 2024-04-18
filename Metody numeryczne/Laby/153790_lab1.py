# Zadania do wykonania
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Zad 1. Stwórz wektor (np.array) składający się z pięciu dowolnych wartości liczbowych. Wyświetl utworzony wektor.
# Następnie, zmień liczbę na drugiej pozycji (nie pod indeksem 2, tylko na drugiej pozycji) na -1, a liczbę
# znajdującą się na pozycji czwartej powiększ dwa razy.


# Stwórz wektor (np.array) składający się z pięciu dowolnych wartości liczbowych. Wyświetl utworzony wektor.
y = np.random.randint(1, 15, size=5)
print(y)

# mień liczbę na drugiej pozycji (nie pod indeksem 2, tylko na drugiej pozycji) na -1, a liczbę
# # znajdującą się na pozycji czwartej powiększ dwa razy.
y[1] = -1
y[3] *= 2
§
print(y)

# -------------------------------------------------------------------------
# Zad 2. Stwórz macierz dwuwymiarową o wymiarach 3 na 4 (3 wiersze, 4 kolumny) składającą się z losowych wartości
# za pomocą polecenia np.random.randint. Przedział wartości może być dowolny.
# Następnie, wyświetl wygenerowaną macierz.
# Wykonaj następujące polecenia:
# • Wyświetl drugi wiersz macierzy (tutaj i dalej to są pozycje, nie indeksy. Chyba że jest powiedziane pod
# indeksem);
# • Wyświetl drugą kolumnę macierzy;
# • Pomnóż cały pierwszy wiersz razy dwa.
# • Wyświetl kwadratową macierz 2x2 składają się z pierwszych dwóch elementów pierwszego wiersza i
# pierwszych dwóch elementów drugiego wiersza.

x = np.array(np.random.randint(1, 30, (3, 4)))
print(x)

# Wyświetl drugi wiersz macierzy;
print(f"drugi wiersz to:{x[1, :]}")

# Pomnóż cały pierwszy wiersz razy dwa
print(f"Pierwszy wiersz x 2 {x[0, ::]*2}")

# Wyświetl kwadratową macierz 2x2 składają się z pierwszych dwóch elementów pierwszego wiersza i
# pierwszych dwóch elementów drugiego wiersza.

print(f"Macierz 2x2. \n{x[:2, :2]}")


# -------------------------------------------------------------------------
# zad 3. Napisz funkcję simple_plot(a, b), która wyświetli wykres, dwóch podanych wektorów a oraz b. Wektor a będzie
# określony przerywaną linią czerwoną, natomiast wektor b będzie określony ciągłą linią niebieską. Legenda do
# wykresu pojawi się w prawym górnym rogu. Oś x powinna być podpisana x, oś y powinna być podpisana y.
# Dodatkowo należy dodać podpis wykresu oraz siatkę. Siatka powinna być zdefiniowana zieloną linią przerywaną
# z przezroczystością 0.5 i grubością linii 1.15.


def simple_plot(a, b):
    plt.plot(a, "r--", label="Wektor a")
    plt.plot(b, "b-", label="Wektor b")
    plt.xlabel("Oś x")
    plt.ylabel("Oś y")
    plt.title("Wykres wektorów  a oraz b")
    plt.legend(loc="upper right")
    plt.grid(color="green", linestyle="--", linewidth=1.15, alpha=0.5)
    plt.show()


a = [10, 8, 6, 4, 1]
b = [5, 4, 3, 2, 1]

simple_plot(a, b)

# ----------------------------------------------------------------
# zad 4 Napisz funkcje func_plot(vmin, vmax, step), która wykona wykres funkcji
# f(x) = x^2 − x ∗ 4 + 8. Argument vmin oznacza wartość początkową wektora x, vmax oznacza wartość końcową wektora x,
# step oznacza krok w wektorze x.


def func_plot(vmin, vmax, step):
    x = np.arange(vmin, vmax, step)
    f_x = x**2 - x * 4 + 8
    plt.plot(x, f_x, label="f(x) = $x^2 - 4x + 8$")
    plt.xlabel("oś X")
    plt.ylabel("oś Y")
    plt.title("Wykres funkcji $f(x) = x^2 - 4x + 8$")
    plt.show()


func_plot(-10, 10, 0.1)

# -------------------------------------------------------------------------
# zad 5. Napisz funkcję multi_plot(sizes, labels), która w jednym oknie wyświetli dwa wykresy: wykres kołowy dla
# podanych rozmiarów w wektorze sizes oraz podpisów labels, oraz wykres słupkowy dla podanych rozmiarów
# w wektorze sizes oraz podpisów labels. Jako przykładowe dane można wziąć na przykład liczbę mieszkańców
# 4-5 polskich miast oraz nazwy tych miast.

# Szacunkowa liczba mieszkańców w wybranych miastach:
# Gdańsk: Około 470,000 mieszkańców
# Szczecin: Około 400,000 mieszkańców
# Bydgoszcz: Około 350,000 mieszkańców
# Toruń: Około 200,000 mieszkańców
# Grudziądz: Około 95,000 mieszkańców


def multi_plot(sizes, labels):
    # Tworzenie figury i dwóch osi
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    colors = [
        "blue",
        "green",
        "red",
        "purple",
        "orange",
    ]
    # Tworzenie wykresu słupkowego
    ax1.bar(cities, populations, color=colors)  # Utworzenie słupków w różnych kolorach

    # Dodawanie tytułów i etykiet
    ax1.set_title("Populacja w wybranych miastach Polski")  # Tytuł wykresu
    ax1.set_xlabel("Miasta")  # Etykieta osi X
    ax1.set_ylabel("Liczba mieszkańców")  # Etykieta osi Y

    # Dodanie tekstu na słupkach dla lepszej czytelności - ale coś nie działa przy 2 wykresach na jednym rysunku
    for i, (city, pop) in enumerate(zip(cities, populations)):
        plt.text(i, pop + 5000, f"{pop:,}", ha="center")

    # Wykres kołowy
    ax2.pie(
        populations, labels=cities, autopct="%1.1f%%", startangle=90, colors=colors
    )  # Utworzenie wycinków w różnych kolorach
    ax2.set_title("Procentowy udział populacji miast")
    # Wyświetlenie wykresu
    plt.tight_layout()  # Dostosowanie layoutu
    plt.show()


# Przybliżona liczba mieszkańców
populations = [470000, 400000, 350000, 200000, 95000]

# Nazwy miast
cities = ["Gdańsk", "Szczecin", "Bydgoszcz", "Toruń", "Grudziądz"]

multi_plot(populations, cities)

# -------------------------------------------------------------------------
# zad 6. Napisz funkcję scatter_plot(), która wyświetli wykres punktowy dwóch zestawów danych (po 100 punktów
# każdy): współrzędne x i y punktów w pierwszym zestawie ma być wygenerowane za pomocą funkcji
# np.random.rand(), a współrzędne drugiego zestawu danych mają być wygenerowane za pomocą funkcji
# np.ranom.randn(). Pierwszy zestaw punktów ma być wizualizowany w kolorze niebieskim, a drugi w kolorze
# zielonym. Punkty drugiego zestawu danych muszą być w postaci gwiazdek (marker). Na wykresie ma
# być pokazana legenda i siatka.


def scatter_plot():
    # Losowe dane dla pierwszego wykresu punktowego
    x1 = np.random.randn(100)
    y1 = np.random.randn(100)

    # Losowe dane dla drugiego wykresu punktowego
    x2 = np.random.randn(100)
    y2 = np.random.randn(100)

    fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # 1 rząd, 2 kolumny

    # Wykres punktowy z kropkami na pierwszej osi
    axs[0].scatter(x1, y1, color="blue", marker="o", label="Kropki")
    axs[0].set_title("Wykres punktowy z kropkami")
    axs[0].set_xlabel("Wartości X")
    axs[0].set_ylabel("Wartości Y")
    axs[0].grid(True)
    axs[0].legend()

    # Wykres punktowy z gwiazdkami na drugiej osi
    axs[1].scatter(x2, y2, color="green", marker="*", label="Gwiazdki")
    axs[1].set_title("Wykres punktowy z gwiazdkami")
    axs[1].set_xlabel("Wartości X")
    axs[1].set_ylabel("Wartości Y")
    axs[1].grid(True)
    axs[1].legend()

    # Wyświetlenie wykresu
    plt.tight_layout()
    plt.show()


scatter_plot()

# -------------------------------------------------------------------------
# Zad 7. Napisz funkcję make_3D(x, y), która wyświetli wykres powierzchni 3D funkcji
# funkcji f(x, y) = sqrt(x^2 + y^2)
# Oś x powinna być podpisana x, oś y powinna być podpisana y, oś z powinna być podpisana jako z.


def make_3D(x, y):
    # Tworzenie siatki współrzędnych
    X, Y = np.meshgrid(x, y)
    # Obliczanie wartości Z na podstawie danej funkcji
    Z = np.sqrt(X**2 + Y**2)

    # Tworzenie figury i osi 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Rysowanie wykresu powierzchniowego
    ax.plot_surface(X, Y, Z, cmap="viridis")  # Używam colormap 'viridis'

    # Dodawanie etykiet
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    # Dodawanie tytułu
    ax.set_title(r"Wykres powierzchni 3D funkcji $f(x, y) = \sqrt{x^2 + y^2}$")

    # Wyświetlenie wykresu
    plt.show()


# Definiowanie zakresów dla x i y
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)

# Wywołanie funkcji
make_3D(x, y)
