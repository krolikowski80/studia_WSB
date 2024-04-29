# # Zadanie 1
# # Napisać funkcje implementującą metodę prostokątów służącą do całkowania numerycznego.
# # Przy implementacji proszę założyć że liczymy tylko pola funkcji znajdujących się w I ćwiartce układu kartezjańskiego
# # (mamy tylko dodatnie wartości dla X i Y).
# # Przykładowe argumenty: funkcja przyjmuje funkcje f pole pod którą ma być obliczone, przedział całkowania
# # [a, b], oraz liczbę prostokątów (ewentualnie krok, zależy od sposobu implementacji). Liczba prostokątów (krok)
# # wypływa na dokładność rozwiązania. Funkcja ma zwrócić obliczone pole (jedna wartość).
# # Przykład:
# # Obliczymy pole pod funkcją f(x) = x
# # 3 w przedziale [0, 2] za pomocą 20 prostokątów (krok około 0.1).
# def metoda_prostokatow(f, a, b, rect_cnt):
#    step = (b-a)/rect_cnt
#    x0 = a + (step / 2)
#    s = 0
#
#    for _ in range(rect_cnt):
#        s += f(x0) * step
#        x0 += step
#
#    return s
#
#
# # Funkcja f(x) = x^3
# def f(x):
#     return x ** 3
#
# # Obliczymy pole pod funkcją f(x) = x  w przedziale [0, 2] za pomocą 20 prostokątów (krok około 0.1).
# pole = metoda_prostokatow(f, 0, 2, 20)
# print(f"Przybliżona wartość całki: {pole}")

# # -----------------------------------------------------------------

# Zadanie 2
# Rozbudować funkcjonalność funkcji z Zadania 1 tak żeby była pokazywana wizualizacja działania zaimplementowanej metody. Proszę zwrócić uwagę,
# że do wizualizacji używamy mniejszej liczby prostokątów (większy krok).
# Przykład takiej wizualizacji jest pokazany na Rysunku poniżej

import numpy as np
import matplotlib.pyplot as plt


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
