# Funkcja zliczająca słowa w tekście
def count_words(text: str) -> int:
    """
    Zlicza liczbę słów w tekście.

    :param text: Tekst wejściowy, w którym chcemy policzyć słowa
    :return: Liczba słów w tekście
    """
    # Dzielimy tekst na wyrazy i liczymy ile ich jest
    return len(text.split())


# Funkcja odwracająca podany tekst
def reverse_string(text: str) -> str:
    """
    Odwraca podany tekst.

    :param text: Tekst wejściowy do odwrócenia
    :return: Odwrócony tekst
    """
    # Wykorzystujemy slice [::-1] do odwrócenia tekstu
    return text[::-1]


# Funkcja sprawdzająca czy tekst jest palindromem
def is_palindrome(text: str) -> bool:
    """
    Sprawdza, czy tekst jest palindromem.

    :param text: Tekst wejściowy
    :return: True jeśli tekst jest palindromem, False w przeciwnym razie
    """
    # Zamieniamy tekst na małe litery i usuwamy spacje
    cleaned = text.lower().replace(" ", "")
    # Porównujemy tekst z jego odwróconą wersją
    return cleaned == cleaned[::-1]