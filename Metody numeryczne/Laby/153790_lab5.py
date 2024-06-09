# Omport dla całego laba
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit


# 2.1 Interpolacja 1
# Dokonaj interpolacji danych umieszczonych w poniższej tabeli. Użyj do tego celu funkcji scipy.interpolate.interp1d(),
# zgodnie z informacją przedstawioną na wykładzie. Użyj trzy rodzaje interpolacji: linear, nearest oraz cubic.
# Na wykresie przedstaw dane oryginalne (punkty z tabeli), oraz 3 różne typy interpolacji. Który typ interpolacji
# najlepiej pasuje do tych danych?

# Tabela 1: Dane do Zadania 1
# x  |   y
# --------
# 0  |  -1
# 1  |   2
# 2  |   5
# 3  |   8
# 4  |   11


def interpolacja1():
    """
    Funkcja wykonuje interpolację danych za pomocą trzech metod: liniowej, najbliższego sąsiada i kubicznej.
    Następnie rysuje wykres danych oryginalnych oraz wyników interpolacji.
    """
    # Dane
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([-1, 2, 5, 8, 11])

    # Interpolacje
    linear_interp = interp1d(x, y, kind='linear')  # Interpolacja liniowa
    # Interpolacja najbliższego sąsiada
    nearest_interp = interp1d(x, y, kind='nearest')
    cubic_interp = interp1d(x, y, kind='cubic')  # Interpolacja kubiczna

    # Generowanie nowych punktów
    x_new = np.linspace(0, 4, 100)
    y_linear = linear_interp(x_new)
    y_nearest = nearest_interp(x_new)
    y_cubic = cubic_interp(x_new)

    # Rysowanie wykresu
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'o', label='Oryginalne dane')
    plt.plot(x_new, y_linear, label='Interpolacja liniowa')
    plt.plot(x_new, y_nearest, label='Interpolacja najbliższego sąsiada')
    plt.plot(x_new, y_cubic, label='Interpolacja kubiczna')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolacja danych')
    plt.grid(True)
    plt.show()


interpolacja1()

# -------------------------------------------------------------------------
#  2.2 Interpolacja 2
# Dokonaj interpolacji danych umieszczonych w poniższej tabeli. Użyj do tego celu funkcji scipy.interpolate.interp1d(),
# zgodnie z informacją przedstawioną na wykładzie. Użyj trzy rodzaje interpolacji: linear, nearest oraz cubic.
# Na wykresie przedstaw dane oryginalne (punkty z tabeli), oraz 3 różne typy interpolacji. Który typ interpolacji
# najlepiej pasuje do tych danych?
# 1
# Tabela 2: Dane do Zadania 2
# x     |    y
# ----------------
# 0.0   |   0.0
# 0.5   |   0.84
# 1.0   |   0.91
# 1.5   |   0.14
# 2.0   |   -0.76
# 2.5   |   -0.96
# 3.0   |   -0.28


def interpolacja2():
    """
    Funkcja wykonuje interpolację danych za pomocą trzech metod: liniowej, najbliższego sąsiada i kubicznej.
    Następnie rysuje wykres danych oryginalnych oraz wyników interpolacji.
    """
    # Dane
    x = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
    y = np.array([0.0, 0.84, 0.91, 0.14, -0.76, -0.96, -0.28])

    # Interpolacje
    linear_interp = interp1d(x, y, kind='linear')  # Interpolacja liniowa
    # Interpolacja najbliższego sąsiada
    nearest_interp = interp1d(x, y, kind='nearest')
    cubic_interp = interp1d(x, y, kind='cubic')  # Interpolacja kubiczna

    # Generowanie nowych punktów
    x_new = np.linspace(0, 3, 100)
    y_linear = linear_interp(x_new)
    y_nearest = nearest_interp(x_new)
    y_cubic = cubic_interp(x_new)

    # Rysowanie wykresu
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'o', label='Oryginalne dane')
    plt.plot(x_new, y_linear, label='Interpolacja liniowa')
    plt.plot(x_new, y_nearest, label='Interpolacja najbliższego sąsiada')
    plt.plot(x_new, y_cubic, label='Interpolacja kubiczna')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolacja danych')
    plt.grid(True)
    plt.show()


interpolacja2()

# -------------------------------------------------------------------

# 2.3 Aproksymacja 1
# Wykonaj aproksymację danych przedstawionych w tabeli wielomianem N-tego stopnia. W przypadku poniższych
# danych można dokonać aproksymację wielomianami stopnia 1, 2, 3, 4. Przy tym, przy aproksymacji wielomianem
# stopnia 4 funkcja będzie przechodzić przez wszystkie punkty, czyli interpolować nasze dane. Aproksymację należy
# dokonać zgodnie z przykładami pokazanymi na wykładzie (funkcja scipy.optimize.curve_fit()).
# Na wykresie przedstaw dane oryginalne (punkty z tabeli), oraz kolejne aproksymacje wielomianowe. Wielomian
# którego stopnia w najlepszy sposób odwzorowuje trend danych?
# Tabela 3: Dane do Zadania 3
# x     |   y
# ---------------
# 0     |   1.55
# 1     |   4.71
# 2     |   5.99
# 3     |   9.47
# 4     |   13.18


def aproksymacja1():
    """
    Funkcja wykonuje aproksymację danych za pomocą wielomianów stopnia 1, 2, 3 i 4.
    Następnie rysuje wykres danych oryginalnych oraz wyników aproksymacji.
    """
    # Dane
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([1.55, 4.71, 5.99, 9.47, 13.18])

    # Funkcje wielomianowe
    def poly1(x, a, b):
        return a * x + b

    def poly2(x, a, b, c):
        return a * x**2 + b * x + c

    def poly3(x, a, b, c, d):
        return a * x**3 + b * x**2 + c * x + d

    def poly4(x, a, b, c, d, e):
        return a * x**4 + b * x**3 + c * x**2 + d * x + e

    # Dopasowanie wielomianów
    popt1, _ = curve_fit(poly1, x, y)
    popt2, _ = curve_fit(poly2, x, y)
    popt3, _ = curve_fit(poly3, x, y)
    popt4, _ = curve_fit(poly4, x, y)

    # Generowanie nowych punktów
    x_new = np.linspace(0, 4, 100)
    y_poly1 = poly1(x_new, *popt1)
    y_poly2 = poly2(x_new, *popt2)
    y_poly3 = poly3(x_new, *popt3)
    y_poly4 = poly4(x_new, *popt4)

    # Rysowanie wykresu
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'o', label='Oryginalne dane')
    plt.plot(x_new, y_poly1, label='Wielomian stopnia 1')
    plt.plot(x_new, y_poly2, label='Wielomian stopnia 2')
    plt.plot(x_new, y_poly3, label='Wielomian stopnia 3')
    plt.plot(x_new, y_poly4, label='Wielomian stopnia 4')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Aproksymacja danych wielomianami')
    plt.grid(True)
    plt.show()


aproksymacja1()

# -----------------------------------------------------------------------------------------------------

# 2.4 Aproksymacja 4
# Wykonaj aproksymację danych przedstawionych w tabeli wielomianem N-tego stopnia. W przypadku poniższych
# danych można dokonać aproksymację wielomianami stopnia 1, 2, 3, 4, 5, 6. Przy tym, przy aproksymacji wielomianem
# stopnia 6 funkcja będzie przechodzić przez wszystkie punkty, czyli interpolować nasze dane. Aproksymację
# należy dokonać zgodnie z przykładami pokazanymi na wykładzie (funkcja scipy.optimize.curve_fit()).
# Na wykresie przedstaw dane oryginalne (punkty z tabeli), oraz kolejne aproksymacje wielomianowe. Wielomian
# którego stopnia w najlepszy sposób odwzorowuje trend danych?
# Tabela 4: Dane do Zadania 4
# x     |   y
# ----------------
# 0.0   |   1.0
# 0.5   |   0.92
# 1.0   |   0.63
# 1.5   |   -0.41
# 2.0   |   -0.94
# 2.5   |   0.27
# 3.0   |   0.89


def aproksymacja4():
    """
    Funkcja wykonuje aproksymację danych za pomocą wielomianów stopnia 1, 2, 3, 4, 5 i 6.
    Następnie rysuje wykres danych oryginalnych oraz wyników aproksymacji.
    """
    # Dane
    x = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
    y = np.array([1.0, 0.92, 0.63, -0.41, -0.94, 0.27, 0.89])

    # Funkcje wielomianowe
    def poly1(x, a, b):
        return a * x + b

    def poly2(x, a, b, c):
        return a * x**2 + b * x + c

    def poly3(x, a, b, c, d):
        return a * x**3 + b * x**2 + c * x + d

    def poly4(x, a, b, c, d, e):
        return a * x**4 + b * x**3 + c * x**2 + d * x + e

    def poly5(x, a, b, c, d, e, f):
        return a * x**5 + b * x**4 + c * x**3 + d * x**2 + e * x + f

    def poly6(x, a, b, c, d, e, f, g):
        return a * x**6 + b * x**5 + c * x**4 + d * x**3 + e * x**2 + f * x + g

    # Dopasowanie wielomianów
    popt1, _ = curve_fit(poly1, x, y)
    popt2, _ = curve_fit(poly2, x, y)
    popt3, _ = curve_fit(poly3, x, y)
    popt4, _ = curve_fit(poly4, x, y)
    popt5, _ = curve_fit(poly5, x, y)
    popt6, _ = curve_fit(poly6, x, y)

    # Generowanie nowych punktów
    x_new = np.linspace(0, 3, 100)
    y_poly1 = poly1(x_new, *popt1)
    y_poly2 = poly2(x_new, *popt2)
    y_poly3 = poly3(x_new, *popt3)
    y_poly4 = poly4(x_new, *popt4)
    y_poly5 = poly5(x_new, *popt5)
    y_poly6 = poly6(x_new, *popt6)

    # Rysowanie wykresu
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'o', label='Oryginalne dane')
    plt.plot(x_new, y_poly1, label='Wielomian stopnia 1')
    plt.plot(x_new, y_poly2, label='Wielomian stopnia 2')
    plt.plot(x_new, y_poly3, label='Wielomian stopnia 3')
    plt.plot(x_new, y_poly4, label='Wielomian stopnia 4')
    plt.plot(x_new, y_poly5, label='Wielomian stopnia 5')
    plt.plot(x_new, y_poly6, label='Wielomian stopnia 6')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Aproksymacja danych wielomianami')
    plt.grid(True)
    plt.show()


aproksymacja4()
