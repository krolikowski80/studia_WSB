import csv
from typing import List, Callable

# Funkcja load_csv ładuje plik CSV i zwraca dane jako listę wierszy (każdy wiersz to lista stringów)
def load_csv(filepath: str) -> List[List[str]]:
    """
    Ładuje plik CSV i zwraca jego zawartość jako listę wierszy.

    :param filepath: ścieżka do pliku CSV
    :return: lista wierszy z pliku CSV
    """
    # Otwieramy plik w trybie odczytu (r) z kodowaniem utf-8
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)  # Tworzymy obiekt do odczytu pliku CSV
        return list(reader)        # Zwracamy wszystkie wiersze jako listę list


# Funkcja filter_data filtruje listę danych na podstawie predykatu (funkcji warunku)
def filter_data(data: List, predicate: Callable) -> List:
    """
    Filtruje dane na podstawie funkcji predykatu.

    :param data: lista danych do przefiltrowania
    :param predicate: funkcja warunku, np. lambda x: x > 3
    :return: nowa lista zawierająca tylko elementy spełniające warunek
    """
    # Zwracamy nową listę zawierającą tylko elementy, które spełniają predykat
    return [row for row in data if predicate(row)]