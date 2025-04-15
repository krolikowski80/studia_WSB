# Lab 3 - Tworzenie własnej biblioteki programistycznej w Pythonie

## 👤 Autor
### Tomasz Królikowski, numer albumu: 153790


# 📦 my_awesome_lib

**my_awesome_lib** to przykładowa biblioteka programistyczna w Pythonie, stworzona w ramach ćwiczeń. Zawiera moduły do przetwarzania danych, operacji matematycznych oraz pracy z tekstem.

## 🔧 Instalacja

Aby zainstalować bibliotekę lokalnie w trybie deweloperskim, użyj polecenia:

```
pip install -r requirements.txt
pip install -e .
```

## 📁 Struktura katalogów

```
my_awesome_lib/
├── __init__.py
├── data_utils.py
├── math_tools.py
└── text_processing.py
tests/
├── __init__.py
├── test_data_utils.py
├── test_math_tools.py
└── test_text_processing.py
```

## 📚 Moduły

### `data_utils.py`
- `load_csv(filepath: str) -> List[List[str]]`: Ładuje dane CSV jako listę wierszy.
- `filter_data(data: list, predicate: Callable) -> list`: Filtruje dane według funkcji.

### `math_tools.py`
- `factorial(n: int) -> int`: Oblicza silnię.
- `mean(numbers: list) -> float`: Oblicza średnią arytmetyczną.
- `is_prime(n: int) -> bool`: Sprawdza, czy liczba jest pierwsza.

### `text_processing.py`
- `count_words(text: str) -> int`: Zlicza słowa w tekście.
- `reverse_string(text: str) -> str`: Odwraca tekst.
- `is_palindrome(text: str) -> bool`: Sprawdza, czy tekst to palindrom.

## ✅ Testowanie

Testy jednostkowe znajdują się w katalogu `tests/`. Uruchom je za pomocą:

```
python -m unittest discover tests
```

## 🐍 Wymagana wersja Pythona
Python 3.8 lub wyższy

## 📄 Licencja
Projekt udostępniony na licencji MIT.

## 📋 Przykład użycia

```python
from my_awesome_lib.math_tools import factorial

print(factorial(5))  # wynik: 120
```
