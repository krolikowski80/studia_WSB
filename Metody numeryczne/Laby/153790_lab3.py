# Zadanie 1
# Napisać funkcje implementującą metodę prostokątów służącą do całkowania numerycznego.
# Przy implementacji proszę założyć że liczymy tylko pola funkcji znajdujących się w I ćwiartce układu kartezjańskiego
# (mamy tylko dodatnie wartości dla X i Y).
# Przykładowe argumenty: funkcja przyjmuje funkcje f pole pod którą ma być obliczone, przedział całkowania
# [a, b], oraz liczbę prostokątów (ewentualnie krok, zależy od sposobu implementacji). Liczba prostokątów (krok)
# wypływa na dokładność rozwiązania. Funkcja ma zwrócić obliczone pole (jedna wartość).
# Przykład:
# Obliczymy pole pod funkcją f(x) = x
# 3 w przedziale [0, 2] za pomocą 20 prostokątów (krok około 0.1).
import random
import matplotlib.pyplot as plt
import numpy as np


def metoda_prostokatow(f, a, b, rect_cnt):
    step = (b-a)/rect_cnt
    x0 = a + (step / 2)
    s = 0

    for _ in range(rect_cnt):
        s += f(x0) * step
        x0 += step

    return s


# Funkcja f(x) = x^3
def f(x):
    return x ** 3


# Obliczymy pole pod funkcją f(x) = x  w przedziale [0, 2] za pomocą 20 prostokątów (krok około 0.1).
pole = metoda_prostokatow(f, 0, 2, 20)
print(f"Przybliżona wartość całki: {pole}")

# -----------------------------------------------------------------

# Zadanie 2
# Rozbudować funkcjonalność funkcji z Zadania 1 tak żeby była pokazywana wizualizacja działania zaimplementowanej metody. Proszę zwrócić uwagę,
# że do wizualizacji używamy mniejszej liczby prostokątów (większy krok).
# Przykład takiej wizualizacji jest pokazany na Rysunku poniżej


def metoda_prostokatow(f, a, b, rect_cnt):
    step = (b-a)/rect_cnt
    x0 = a + (step / 2)
    s = 0
    rects = []  # Lista do przechowywania informacji o prostokątach dla wizualizacji

    for _ in range(rect_cnt):
        s += f(x0) * step
        # Zapisanie informacji o każdym prostokącie
        rects.append((x0 - step / 2, f(x0)))
        x0 += step

    return s, rects, step  # Zwracanie wyniku, danych do wizualizacji i kroku


def f(x):
    return x ** 3


# Obliczymy pole pod funkcją f(x) = x  w przedziale [0, 2] za pomocą 20 prostokątów (krok około 0.1)
pole, rectangles, step = metoda_prostokatow(f, 0, 2, 20)
print(f"Przybliżona wartość całki: {pole}")

# Wizualizacja
x = np.linspace(0, 2, 1000)
y = f(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='$f(x) = x^3$', zorder=5)  # Rysowanie funkcji

# Rysowanie prostokątów
for x0, height in rectangles:
    plt.gca().add_patch(plt.Rectangle((x0, 0), step, height,
                                      edgecolor='r', facecolor='none', linewidth=1.5, zorder=10))

plt.title('Metoda prostokątów dla $f(x) = x^3$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

# ----------------------------------------------------------------
# Zadanie 3
# Napisać funkcje implementującą metodę trapezów służącą do całkowania numerycznego.
# Przy implementacji proszę założyć że liczymy tylko pola funkcji znajdujących się w I ćwiartce układu kartezjańskiego
# (mamy tylko dodatnie wartości dla X i Y).
# Przykład:
# Obliczymy pole pod funkcją f(x) = x^3 w przedziale [0, 2] używając 20 trapezów (krok około 0.1).
# Listing 3: Przykładowe wywołanie funkcji.
# Funkcja f jest zdefiniowana poprzednio
# print(trapezoidal_method(f, 0, 2, 20))
# 4.01
# Jak widzimy, dostaliśmy wynik bliski temu wyniku który uzyskaliśmy całkując tą funkcję analitycznie, ale w
# dalszym ciągu mamy małe odchylenie.


def trapezoidal_method(f, a, b, n):
    # Obliczenie szerokości trapezu
    h = (b - a) / n

    # Obliczenie wartości funkcji w punktach podziałowych
    # i sumowanie pola trapezów
    integral = 0.5 * (f(a) + f(b))  # suma wartości na krańcach
    for i in range(1, n):
        x = a + i * h
        integral += f(x)  # suma wartości w punktach wewnętrznych

    integral *= h  # mnożymy sumę wartości przez szerokość trapezu

    return round(integral, 2)

# Przykładowa funkcja podcałkowa


def f(x):
    return x ** 3


# Wywołanie funkcji dla zadanych parametrów
print(trapezoidal_method(f, 0, 2, 20))  # powinno wyjść wartość bliska 4

# ----------------------------------------------------------------------------------
# Zadanie 4
# Rozbudować funkcjonalność funkcji z Zadania 3 tak żeby była pokazywana wizualizacja działania zaimplementowanej
# metody.


def trapezoidal_method(f, a, b, n, show_graph=True):
    h = (b - a) / n
    x_points = np.linspace(a, b, n+1)
    y_points = f(x_points)

    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(x_points[i])
    integral *= h

    if show_graph:
        plt.figure(figsize=(10, 5))
        # Rysowanie funkcji
        x_curve = np.linspace(a, b, 1000)
        y_curve = f(x_curve)
        plt.plot(x_curve, y_curve, label="f(x)", color="blue")

        # Rysowanie trapezów
        for i in range(n):
            x_trap = [x_points[i], x_points[i], x_points[i+1], x_points[i+1]]
            y_trap = [0, y_points[i], y_points[i+1], 0]
            plt.fill(x_trap, y_trap, 'b', edgecolor='b', alpha=0.3)

        plt.title("Wizualizacja metody trapezów")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        plt.show()

    return round(integral, 2)

# Przykładowa funkcja podcałkowa


def f(x):
    return x ** 3


# Wywołanie funkcji z wizualizacją
result = trapezoidal_method(f, 0, 2, 20)
print("Przybliżona wartość całki:", result)

# ------------------------------------------------------------------------------------
# Zadanie 5
# Napisać funkcje implementującą metodę Monte Carlo służącą do całkowania numerycznego.
# Przy implementacji proszę założyć że liczymy tylko pola funkcji znajdujących się w I ćwiartce układu kartezjańskiego
# (mamy tylko dodatnie wartości dla X i Y).
# **Przykład:**
# Obliczymy pole pod funkcją f(x) = x3 w przedziale [0, 2], używając do tego 10000 wylosowanych punktów:
# Listing 4: Przykładowe wywołanie funkcji.
# Jako argumenty podajemy funkcje, zakres, oraz liczbe strzałów
# print(monte_carlo(f, 0, 2, 10000))
# 4.078998042399999


def monte_carlo(f, a, b, n):
    # Obliczanie maksymalnej wartości funkcji na danym przedziale
    # przybliżone maksimum na krańcach (to może nie wystarczyć dla bardziej skomplikowanych funkcji)
    max_y = max(f(a), f(b))

    # Dokładniejsze oszacowanie maksimum dla prostych przypadków
    x_max = 2  # analityczne oszacowanie dla funkcji x^3 w przedziale [0, 2]
    max_y = f(x_max)

    under_curve_count = 0
    total_area = (b - a) * max_y

    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, max_y)
        if y <= f(x):
            under_curve_count += 1

    estimated_area = (under_curve_count / n) * total_area
    return estimated_area

# Przykładowa funkcja podcałkowa


def f(x):
    return x ** 3


# Wywołanie funkcji
result = monte_carlo(f, 0, 2, 10000)
print("Przybliżona wartość całki:", result)

# Zadanie 6
# Rozbudować funkcjonalność funkcji z Zadania 5 tak żeby była pokazywana wizualizacja działania zaimplementowanej
# metody.


def monte_carlo(f, a, b, n, show_graph=True):
    x_max = 2  # Wartość x, dla której funkcja osiąga maksymalne y na przedziale
    max_y = f(x_max)  # Maksymalne y osiągane przez funkcję na przedziale

    under_curve_count = 0
    total_area = (b - a) * max_y
    points_under_curve = []
    points_above_curve = []

    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, max_y)
        if y <= f(x):
            under_curve_count += 1
            points_under_curve.append((x, y))
        else:
            points_above_curve.append((x, y))

    estimated_area = (under_curve_count / n) * total_area

    if show_graph:
        plt.figure(figsize=(10, 6))
        # Rysowanie punktów
        points_under_curve = np.array(points_under_curve)
        points_above_curve = np.array(points_above_curve)
        if len(points_under_curve) > 0:
            plt.scatter(points_under_curve[:, 0], points_under_curve[:, 1],
                        color='green', marker='.', label='Points under curve')
        if len(points_above_curve) > 0:
            plt.scatter(points_above_curve[:, 0], points_above_curve[:, 1],
                        color='red', marker='.', label='Points above curve')

        # Rysowanie funkcji
        x_curve = np.linspace(a, b, 1000)
        y_curve = f(x_curve)
        plt.plot(x_curve, y_curve, label="f(x) = x^3", color="blue")

        plt.title("Visualization of Monte Carlo Method")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)
        plt.show()

    return estimated_area

# Przykładowa funkcja


def f(x):
    return x ** 3


# Wywołanie funkcji z wizualizacją
result = monte_carlo(f, 0, 2, 1000)
print("Przybliżona wartość całki:", result)
