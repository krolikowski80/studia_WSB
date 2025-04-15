# Funkcja obliczająca silnię liczby n
def factorial(n: int) -> int:
    """
    Oblicza silnię liczby n.

    :param n: liczba całkowita, której silnię chcemy obliczyć
    :return: wynik obliczonej silni
    """
    # Sprawdzamy, czy podano liczbę nieujemną
    if n < 0:
        raise ValueError("Liczba musi być nieujemna.")
    # Zwracamy 1 dla 0, w przeciwnym razie rekurencyjnie obliczamy silnię
    return 1 if n == 0 else n * factorial(n - 1)


# Funkcja obliczająca średnią arytmetyczną z listy liczb
def mean(numbers: list) -> float:
    """
    Oblicza średnią arytmetyczną z listy liczb.

    :param numbers: lista liczb (int lub float)
    :return: średnia arytmetyczna
    """
    # Sprawdzamy, czy lista nie jest pusta
    if not numbers:
        raise ValueError("Lista nie może być pusta.")
    # Obliczamy sumę liczb i dzielimy przez ich ilość
    return sum(numbers) / len(numbers)


# Funkcja sprawdzająca, czy liczba n jest liczbą pierwszą
def is_prime(n: int) -> bool:
    """
    Sprawdza, czy liczba n jest liczbą pierwszą.

    :param n: liczba całkowita
    :return: True jeśli liczba pierwsza, False w przeciwnym razie
    """
    # Liczby mniejsze niż 2 nie są pierwsze
    if n < 2:
        return False
    # Sprawdzamy podzielność liczby n przez kolejne liczby
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    # Jeśli nie znaleziono dzielnika, liczba jest pierwsza
    return True