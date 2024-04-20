import numpy as np
import matplotlib.pyplot as plt

# Zadanie 1
# Zaimplementować funkcję znajdującą pierwiastek podanej jako argument funkcji za pomocą metody połowienia.
# Poniżej jest pokazane przykładowe wywołanie zaimplementowanej funkcji w celu znalezienia pierwiastka funkcji
# f(x) = (x − 2)^3 − x^2 + 2x
# Przykład
# def f(x):
#   return (x - 2)**3 - x**2 + 2*x
#   print(bisection_method(f, 1.5, 3, eps=10**-6, max_iter=100))
# 2.000000238418579


def bisection_method(func, a, b, eps, max_iter):
    """
    Znajduje pierwiastek funkcji 'func' w przedziale [a, b] za pomocą metody bisekcji.
    'eps' określa dokładność wyniku, a 'max_iter' ogranicza liczbę iteracji.

    Param:
        func (callable): Funkcja, dla której ma być znaleziony pierwiastek.
        a (float): Początek przedziału.
        b (float): Koniec przedziału.
        eps (float): Dokładność wyniku.
        max_iter (int): Maksymalna liczba iteracji.

    Zwraca:
        float: Przybliżony pierwiastek funkcji.
    """
    # sprawdzenie warunku wstępnego, które musi być spełnione,
    # aby metoda bisekcji mogła zostać skutecznie zastosowana
    # do znajdowania pierwiastka funkcji w danym przedziale.
    if (
        func(a) * func(b) >= 0
    ):  # oblicza wartości funkcji na końcach przedziału, czyli func(a) i func(b), a następnie mnoży te dwie wartości.
        raise ValueError(
            "Funkcja nie ma przeciwnych znaków na końcach przedziału [a, b]."
        )  # Jeżeli wynik tego mnożenia jest większy lub równy zero, oznacza to, że obie wartości mają ten sam znak (obie są dodatnie lub obie są ujemne) lub przynajmniej jedna z nich jest równa zero.

    iteration = 0
    while (b - a) / 2.0 > eps and iteration < max_iter:
        c = (a + b) / 2.0
        if func(c) == 0 or (b - a) / 2.0 < eps:
            break
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iteration += 1

    return c


# funkcja, dla której cszukamy pierwiastka
def f(x):
    return (x - 2) ** 3 - x**2 + 2 * x


wynik = bisection_method(f, 1.5, 3, eps=10**-6, max_iter=100)
print(f"Pierwiastek funkcji wynosi w przybliżeniu: {wynik}")

# -------------------------------------------------------------
# Zadanie 2
# Rozbudować funkcjonalność funkcji z Zadania 1 tak żeby była pokazywana wizualizacja działania zaimplementowanej metody.


def bisection_method(func, a, b, eps, max_iter):
    """
    Znajduje pierwiastek funkcji 'func' w przedziale [a, b] za pomocą metody bisekcji.
    'eps' określa dokładność wyniku, a 'max_iter' ogranicza liczbę iteracji.

    Param:
        func (callable): Funkcja, dla której ma być znaleziony pierwiastek.
        a (float): Początek przedziału.
        b (float): Koniec przedziału.
        eps (float): Dokładność wyniku.
        max_iter (int): Maksymalna liczba iteracji.

    Zwraca:
        float: Przybliżony pierwiastek funkcji.
    """
    # sprawdzenie warunku wstępnego, które musi być spełnione,
    # aby metoda bisekcji mogła zostać skutecznie zastosowana
    # do znajdowania pierwiastka funkcji w danym przedziale.
    if (
        func(a) * func(b) >= 0
    ):  # oblicza wartości funkcji na końcach przedziału, czyli func(a) i func(b), a następnie mnoży te dwie wartości.
        raise ValueError(
            "Funkcja nie ma przeciwnych znaków na końcach przedziału [a, b]."
        )  # Jeżeli wynik tego mnożenia jest większy lub równy zero, oznacza to, że obie wartości mają ten sam znak (obie są dodatnie lub obie są ujemne) lub przynajmniej jedna z nich jest równa zero.
    points = [(a, func(a)), (b, func(b))]
    iteration = 0
    while (b - a) / 2.0 > eps and iteration < max_iter:
        c = (a + b) / 2.0
        points.append((c, func(c)))
        if func(c) == 0 or (b - a) / 2.0 < eps:
            break
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iteration += 1
    # Wizualizacja
    x = np.linspace(min(a, b, c) - 1, max(a, b, c) + 1, 300)
    y = np.vectorize(func)(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="f(x)")
    plt.axhline(0, color="gray", lw=0.5)
    for point in points:
        plt.axvline(
            x=point[0],
            color="red",
            linestyle="--",
            lw=1,
            label="Kroki bisekcji" if point == points[0] else "",
        )
    plt.title("Wizualizacja")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

    return c


# funkcja, dla której cszukamy pierwiastka
def f(x):
    return (x - 2) ** 3 - x**2 + 2 * x


wynik = bisection_method(f, 1.5, 3, eps=10**-6, max_iter=100)
print(f"Pierwiastek funkcji wynosi w przybliżeniu: {wynik}")

# ---------------------------------------------------------------------------

# Zadanie 3
# Zaimplementować funkcję znajdującą pierwiastek podanej jako argument funkcji za pomocą metody Newtona.
# Poniżej jest pokazane przykładowe wywołanie zaimplementowanej funkcji w celu znalezienia pierwiastka funkcji
# f(x) = (x − 2)^2 − 1, w punktem początkowym x0 = 4
# Przykład:
# def f2(x):
#   return (x - 2)**2 - 1
# newton(f2, 4)
# 3.000000000000003
#
# Przykładowe argumenty: funkcja przyjmuje funkcje f której miejsce zerowe musi być znalezione, punkt startu
# x0, w okolicach którego miejsce zerowe jest szukane, oraz dwa argumenty eps i max_iter, określające dokładność
# i maksymalną liczbę iteracji (kroków) odpowiednio. Funkcja ma zwrócić odnalezione rozwiązanie (jedna wartość).
# W przypadku gdy zostanie osiągnięta maksymalna liczba iteracji, a przedział poszukiwań nie zawęził się poniżej
# wskazanej dokładności należy wyświetlić stosowny komunikat.
#
# Podpowiedź: Do obliczania wartości pochodnej funkcji w punkcie x0 należy użyć wzoru:
# f′(x0) = (f(x0 + h) − f(x0)) / h
# gdzie h jest bardzo małą wartością (np. h = 10**-7).
#
# Podpowiedź 2: Styczną do funkcji w punkcie (x0, f(x0)) możemy wyrazić jako:
# y = f′(x0)(x − x0) + f(x0)


def newton(f, x0, eps=10**-7, max_iter=100):
    """
    Znajduje pierwiastek funkcji f używając metody Newtona (metody stycznych).

    param:
        f (callable): Funkcja, dla której miejsce zerowe ma być znalezione.
        x0 (float): Początkowy punkt startowy dla metody Newtona.
        eps (float): Dokładność docelowego wyniku.
        max_iter (int): Maksymalna liczba iteracji (kroków).

    Zwraca:
        float: Znalezione miejsce zerowe funkcji.
    """
    h = 10**-7  # Mała wartość używana do obliczenia pochodnej
    iter = 0

    while iter < max_iter:
        f_x0 = f(x0)  # Oblicz wartość funkcji w punkcie x0

        # Obliczenie pochodnej funkcji w punkcie x0
        derivative = (f(x0 + h) - f_x0) / h
        if derivative == 0:
            raise ValueError(
                "Pochodna wynosi zero, metoda Newtona może nie znaleźć rozwiązania."
            )

        # Oblicz kolejny punkt wg wzoru x1 = x0 - f(x0) / f'(x0)
        x1 = x0 - f_x0 / derivative

        # Sprawdź, czy osiągnięto pożądaną dokładność
        if abs(x1 - x0) < eps:
            return x1  # Zwróć znaleziony pierwiastek
        else:
            x0 = x1  # Aktualizuj x0 do nowo obliczonej wartości
            iter += 1  # Zwiększ licznik iteracji

    # Wyświetl komunikat, jeśli nie znaleziono pierwiastka w określonej liczbie iteracji
    print("Nie znaleziono miejsca zerowego w zakresie maksymalnej liczby iteracji.")
    return x0  # Zwróć ostatnią obliczoną wartość x0


# Definicja funkcji, dla której szukamy miejsca zerowego
def f2(x):
    return (x - 2) ** 2 - 1


# wywołanie funkcji newton
wynik = newton(f2, 4)
print(f"Pierwiastek funkcji wynosi w przybliżeniu: {wynik}")

# ------------------------------------------------------------------

# Zadanie 4
# Rozbudować funkcjonalność funkcji z Zadania 3 tak żeby była pokazywana wizualizacja działania zaimplementowanej metody.
# Proszę się upewnić, że zaimplementowana funkcja działa prawidłowo dla wszystkich przykładów z Tabeli.
# Funkcja                       x0      Oczekiwany wynik
# f(x) = (x − 2)^3 − x^2 + 2x   1.5     ≈ 2
# f(x) = x^2 − 2                2       ≈ 1.41
# f(x) = sin(x)                 3       ≈ 3.14
# f(x) = x^3 − 2^x + 2          0       Wypisze się komunikat o osiągnięciu maksymalnej liczby iteracji
#
# Uwaga: proszę ustawić eps = 10^−6 i max_iter = 100.


def newton_with_visualization_and_tangents(f, x0, eps=10**-6, max_iter=100):
    """
    Znajduje pierwiastek funkcji f używając metody Newtona i wizualizuje poszczególne kroki wraz ze stycznymi.

    Param:
        f (callable):   Funkcja, dla której miejsce zerowe ma być znalezione.
        x0 (float):     Początkowy punkt startowy dla metody Newtona.
        eps (float):    Dokładność docelowego wyniku.
        max_iter (int): Maksymalna liczba iteracji (kroków).

    Zwraca:
        float:          Znalezione miejsce zerowe funkcji.
    """
    h = eps = 10**-7  # Mała wartość używana do obliczenia pochodnej
    iter = 0
    points = [(x0, f(x0))]  # Lista do przechowywania punktów do wizualizacji

    while iter < max_iter:
        f_x0 = f(x0)
        derivative = (f(x0 + h) - f_x0) / h
        if derivative == 0:
            raise ValueError(
                "Pochodna wynosi zero, metoda Newtona może nie znaleźć rozwiązania."
            )

        x1 = x0 - f_x0 / derivative
        points.append((x1, f(x1)))

        if abs(x1 - x0) < eps:
            break

        x0 = x1
        iter += 1

    # Wizualizacja
    x_vals = np.linspace(
        min(p[0] for p in points) - 1, max(p[0] for p in points) + 1, 400
    )
    y_vals = np.vectorize(f)(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label="f(x)")

    # Dodanie stycznych do wykresu
    for x, fx in points:
        tangent_x = np.linspace(x - 1, x + 1, 10)  # Zakres dla linii stycznej
        tangent_y = derivative * (tangent_x - x) + fx
        plt.plot(tangent_x, tangent_y, "r--", linewidth=1)

    plt.scatter(*zip(*points), color="red", s=50, label="Iteracje metody Newtona")
    plt.title(f"x = {x0:.10f}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.axhline(0, color="gray", lw=0.5)
    plt.legend()
    plt.grid(True)
    plt.show()

    if iter == max_iter:
        print("Nie znaleziono miejsca zerowego w zakresie maksymalnej liczby iteracji.")
        return x0

    return x0


# Definicja funkcji
def f2(x):
    return (x - 2) ** 2 - 1


# Przykładowe wywołanie funkcji z wizualizacją z poprzedniego zadania
wynik = newton_with_visualization_and_tangents(f2, 4)
print(f"Pierwiastek funkcji wynosi w przybliżeniu: {wynik}")


# Przykładowe wywołanie funkcji z wizualizacją dla  f(x) = (x − 2)^3 − x^2 + 2x   x0 = 1.5   Oczekiwany wynik  ≈ 2
# Niestety ja mam wynik "Pierwiastek funkcji wynosi w przybliżeniu: 4.000000000005075"


# Definicja funkcji
def f2(x):
    return ((x - 2) ** 3) - (x**2) + (2 * x)


wynik = newton_with_visualization_and_tangents(f2, 1.5)
print(f"Pierwiastek funkcji wynosi w przybliżeniu: {wynik}")


# Przykładowe wywołanie funkcji z wizualizacją dla  f(x) = x^2 − 2 ; x0 = 2  ; Oczekiwany wynik  ≈ 1.41
# Wynik: Pierwiastek funkcji wynosi w przybliżeniu: 1.414213562374764
# Definicja funkcji
def f2(x):
    return (x**2) - 2


wynik = newton_with_visualization_and_tangents(f2, 2)
print(f"Pierwiastek funkcji wynosi w przybliżeniu: {wynik}")


# Przykładowe wywołanie funkcji z wizualizacją dla  f(x) = sin(x) ; x0 = 3  ; Oczekiwany wynik  ≈ 1.41
# Wynik: Pierwiastek funkcji wynosi w przybliżeniu: 3.1415926532988707
def f2(x):
    return np.sin(x)


wynik = newton_with_visualization_and_tangents(f2, 3)
print(f"Pierwiastek funkcji wynosi w przybliżeniu: {wynik}")


# Przykładowe wywołanie funkcji z wizualizacją dla  f(x) = x^3 - 2x + 2 ; x0 = 0  ; Oczekiwany wynik Wypisze się komunikat o osiągnięciu maksymalnej liczby iteracji
# Wynik: Nie znaleziono miejsca zerowego w zakresie maksymalnej liczby iteracji.
def f2(x):
    return x**3 - 2 * x + 2


wynik = newton_with_visualization_and_tangents(f2, 0)
print(f"Pierwiastek funkcji wynosi w przybliżeniu: {wynik}")
