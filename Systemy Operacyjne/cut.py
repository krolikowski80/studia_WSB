#!/Users/tomasz/.pyenv/versions/3.12.0/bin/python
# Wykonał : Tomasz KRÓLIKOWSKI
# Numer albumu : 153790
# W tym opliku wykonano zadania 1 - 3
# import dla całego laba
import sys
import argparse
import os


# Zadanie 4
# Zaimplementuj uproszczoną wersję polecenia cut w postaci skryptu w Python. Program musi wczytać plik FILE i
# wyświetlić wybrane kolumny z tego pliku. Sygnatura polecenia ma wyglądać mniej-więcej następująco:
# python cut.py OPTIONS FILE
# Program musi obsługiwać następujące przełączniki:
# • -d / --delimiter=DELIM - Umożliwia wskazanie który znak ma być traktowany jako separator kolumn. Domyślnie
# ustawiamy sybmol \t, czyli symbol TAB. Argument nieobowiązkowy.
# • -f / --fields=LIST - Umożliwia wskazanie która kolumna/które kolumny mają zostać wyświetlone. Wystarczy,
# że program będzie akceptował następujące formaty danych dla tego przełącznika: 3, 1,2,3 (nie robimy
# rzeczy w stylu 1-4,7,8, jak pozwala program oryginalny. Proszę zwrócić uwagę, że w przypadku gdy podane
# są kilka kolumn, mają one zostać połączone separatorem jak w programie oryginalnym (w razie wątpliwości
# proszę sprawdzić działanie programu oryginalnego). Argument obowiązkowy.


def main():
    """
    Główna funkcja programu.
    Parsuje argumenty wiersza poleceń i wyświetla wybrane kolumny z pliku.
    """
    # Tworzenie parsera argumentów
    parser = argparse.ArgumentParser(
        description="Uproszczona wersja polecenia cut")

    # Dodawanie argumentów do parsera
    parser.add_argument('-d', '--delimiter',
                        default='\t',
                        # Separator kolumn
                        help='Delimiter used in the file (default: TAB)')
    parser.add_argument('-f', '--fields',
                        required=True,
                        # Kolumny do wyświetlenia
                        help='Comma separated list of fields to display (e.g., 1,2,3)')
    parser.add_argument('--output-delimiter',
                        help='Delimiter used to separate output fields')  # Separator kolumn wyjściowych
    parser.add_argument('file',
                        type=str,
                        help='File to be processed')  # Plik do przetworzenia

    # Parsowanie argumentów
    args = parser.parse_args()

    # Parsowanie listy kolumn do wyświetlenia
    fields = list(map(int, args.fields.split(',')))

    # Używanie oryginalnego separatora jeśli nie podano separatora wyjściowego
    output_delimiter = args.output_delimiter if args.output_delimiter else args.delimiter

    # Próba otwarcia i odczytu pliku
    try:
        with open(args.file) as f:
            for line in f:
                columns = line.strip().split(args.delimiter)
                selected_columns = [columns[int(i) - 1] for i in fields]
                print(output_delimiter.join(selected_columns))
    except FileNotFoundError:
        print(f"Error: File '{
              args.file}' not found. Please provide an existing text file.")
        return


if __name__ == "__main__":
    main()

# TESTY
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-06-09 - 9:37:57
# ╰─(podstawy) ⠠⠵ cat file.csv
# Name, Age, City
# John, 25, New York
# Alice, 30, Los Angeles
# Bob, 22, Chicago
#
# Testowanie standardowego separatora (TAB) i wybranych kolumn:
# file.csv jest z przecinkami a file2.csv z TABami
#
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-06-09 - 9:59:55
# ╰─(podstawy) ⠠⠵ cat file.csv
# Name, Age, City
# John, 25, New York
# Alice, 30, Los Angeles
# Bob, 22, Chicago
# Abdul, 26, Kozo-jebca
# Ernest, 56, London
#
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-06-09 - 10:01:48
# ╰─(podstawy) ⠠⠵ cat file2.csv
# Name    Age     City
# John    25      New York
# Alice   30      Los Angeles
# Bob     22      Chicago
# Abdul   26      Kozo-jebca
# Ernest  56      London
#
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-06-09 - 10:02:47
# ╰─(podstawy) ⠠⠵ ./cut.py -f 1,3 file2.csv
# Name    City
# John    New York
# Alice   Los Angeles
# Bob     Chicago
# Abdul   Kozo-jebca
# Ernest  London
#
# Testowanie przecinka, jako separatora  i wybranych kolumn:
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-06-09 - 10:03:26
# ╰─(podstawy) ⠠⠵ ./cut.py -f 2,3 -d ',' file.csv

#  Age, City
#  25, New York
#  30, Los Angeles
#  22, Chicago
#  26, Kozo-jebca
#  56, London
#
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-06-09 - 10:04:41
# ╰─(podstawy) ⠠⠵ ./cut.py -f 1,3 -d ',' file.csv
# Name, City
# John, New York
# Alice, Los Angeles
# Bob, Chicago
# Abdul, Kozo-jebca
# Ernest, London
