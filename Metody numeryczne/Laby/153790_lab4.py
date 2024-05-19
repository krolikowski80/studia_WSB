# Zadanie 2.1 Rozwiązywanie równań nieliniowych
# Użyć funkcje z modułu scipy.optimize (przykładowo fsolve()) w celu rozwiązywania poniższych równań nieliniowych.
# Funkcja x0 Oczekiwany wynik
# FUNKCJA                           |  X0   | Oczekiwany wynik
# -------------------------------------------------------------------------
# f(x) = (x − 2)^3 − x^2 + 2x       | 1.5   | ≈ 2
# f(x) = x^2 − 2                    | 2     | ≈ 1.41
# f(x) = sin(x)                     | 3     | ≈ 3.14
# f(x) = x^3 − 2x + 2               | -1    | ≈ −1.769

from scipy.integrate import quad
import numpy as np
from scipy.optimize import fsolve

# Definiowanie funkcji


def func1(x):
    """
    Funkcja reprezentująca równanie: f(x) = (x - 2)^3 - x^2 + 2x
    """
    return (x - 2)**3 - x**2 + 2*x
    # Tutaj coś nie wychodzi


def func2(x):
    """
    Funkcja reprezentująca równanie: f(x) = x^2 - 2
    """
    return x**2 - 2


def func3(x):
    """
    Funkcja reprezentująca równanie: f(x) = sin(x)
    """
    return np.sin(x)


def func4(x):
    """
    Funkcja reprezentująca równanie: f(x) = x^3 - 2x + 2
    """
    return x**3 - 2*x + 2


# Lista funkcji, punktów startowych i oczekiwanych wyników
functions = [func1, func2, func3, func4]
initial_guesses = [1.5, 2, 3, -1]
expected_results = [2, 1.41, 3.14, -1.769]

# Rozwiązywanie równań i wyświetlanie wyników
for func, x0, expected in zip(functions, initial_guesses, expected_results):
    solution = fsolve(func, x0)
    print(f"Rozwiązanie dla f(x) = {func.__name__} z x0 = {
          x0}: x = {solution[0]}, oczekiwany wynik = {expected}")

# -------------------------------------------------------------------------------------------------------------
# Zadanie 2.2 Całkowanie numeryczne
# Użyć funkcje z modułu scipy.integrate (przykładowo quad()) w celu rozwiązywania obliczenia poniższych całek.
# 1.  ∫ 0 to 2 x^3dx = 4
# 2. ∫ 0 to 4 (x^3 − 6x^2 + 9x + 2)dx = 16
# 3. ∫ 0 to π (sin(2x) + 1)dx = π
# 4. ∫ 1 to 4 [(sin(8x)/x)+1]dx ≈ 2.970054955


# Definiowanie funkcji dla każdej z całek

# 1. ∫ 0 to 2 x^3 dx

def func10(x):
    return x**3

# 2. ∫ 0 to 4 (x^3 − 6x^2 + 9x + 2) dx


def func20(x):
    return x**3 - 6*x**2 + 9*x + 2

# 3. ∫ 0 to π (sin(2x) + 1) dx


def func30(x):
    return np.sin(2*x) + 1

# 4. ∫ 1 to 4 [(sin(8x)/x) + 1] dx


def func40(x):
    return (np.sin(8*x)/x) + 1


# Obliczanie całek
result1, _ = quad(func10, 0, 2)
result2, _ = quad(func20, 0, 4)
result3, _ = quad(func30, 0, np.pi)
result4, _ = quad(func40, 1, 4)

# Wyświetlanie wyników
print(f"∫ 0 to 2 x^3 dx = {result1}")
print(f"∫ 0 to 4 (x^3 − 6x^2 + 9x + 2) dx = {result2}")
print(f"∫ 0 to π (sin(2x) + 1) dx = {result3}")
print(f"∫ 1 to 4 [(sin(8x)/x) + 1] dx ≈ {result4}")
