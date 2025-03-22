import re
from datetime import datetime

# --------------------------------------------------
# 1. Sprawdzanie poprawności adresu e-mail
# --------------------------------------------------
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

# --------------------------------------------------
# 2. Sprawdzanie, czy tekst jest palindromem
# --------------------------------------------------
def is_palindrome(text):
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

# --------------------------------------------------
# 3. Obliczanie pola prostokąta
# --------------------------------------------------
def rectangle_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Wymiary muszą być nieujemne")
    return width * height

# --------------------------------------------------
# 4. Filtrowanie liczb parzystych z listy
# --------------------------------------------------
def filter_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

# --------------------------------------------------
# 5. Konwersja formatu daty YYYY-MM-DD → DD.MM.YYYY
# --------------------------------------------------
def convert_date_format(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Niepoprawny format daty. Oczekiwano YYYY-MM-DD")
