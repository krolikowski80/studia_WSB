#!/Users/tomasz/.pyenv/versions/3.12.0/bin/python
# import dla całego laba
import sys
import argparse
import os

# Zadanie 1
# Zapoznaj się z poniższym kodem, który przedstawia uproszczoną wersję polecenia head, zaimplementowaną w
# Python. Implementacja ta używa modułu argparse w celu obsługi argumentów wiersza poleceń.
# Więcej o tym modułu można poczytać w dokumentacji: https://docs.python.org/3/library/argparse.html,
# oraz https://docs.python.org/3/howto/argparse.html.
# Przepisz i uruchom ten program, sprawdź czy działa poprawnie, zbadaj działanie przełączników -n, --lines,
# -v, --verbose, --help. Sprawdź co będzie jeżeli podać plik który nie istnieje.


parser = argparse.ArgumentParser()

parser.add_argument("-n", "--lines",
                    default=[10],
                    type=int,
                    nargs=1,
                    help="Number of lines to show.")
parser.add_argument("file", type=str, help="File which should be displayed.")
parser.add_argument("-v", "--verbose", action="store_true",
                    default=False, help="Explain what is done.")
args = parser.parse_args()

if args.verbose:
    print(f"Program is running with name {sys.argv[0]}")
    print(f"It will print {args.lines[0]} lines from {
          args.file} and terminate.")
    print("="*50)

with open(args.file) as f:
    for i in range(args.lines[0]):
        print(f.readline().strip())

if args.verbose:
    print("="*50)

## TESTY ##
#
# (podstawy) ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-05-20 - 21:34:13
# ╰─(podstawy) ⠠⠵ ./head.py -v head.py
# Program is running with name ./head.py
# It will print 10 lines from head.py and terminate.
# ==================================================
# #!/Users/tomasz/.pyenv/versions/3.12.0/bin/python
# import sys
# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument("-n", "--lines",
# default=[10],
# type=int,
# nargs=1,
# ==================================================
#
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-05-20 - 21:37:45
# ╰─(podstawy) ⠠⠵ ./head.py --verbose head.py
# Program is running with name ./head.py
# It will print 10 lines from head.py and terminate.
# ==================================================
# #!/Users/tomasz/.pyenv/versions/3.12.0/bin/python
# import sys
# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument("-n", "--lines",
# default=[10],
# type=int,
# nargs=1,
# ==================================================
#
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-05-20 - 21:37:54
# ╰─(podstawy) ⠠⠵ ./head.py -n 15 head.py
# #!/Users/tomasz/.pyenv/versions/3.12.0/bin/python
# import sys
# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument("-n", "--lines",
# default=[10],
# type=int,
# nargs=1,
# help="Number of lines to show.")
# parser.add_argument("file", type=str, help="File which should be displayed.")
# parser.add_argument("-v", "--verbose", action="store_true",
# default=False, help="Explain what is done.")
# args = parser.parse_args()
#
# Listing pierwszych 15 linii pliku.
#
#
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-05-20 - 21:40:24
# ╰─(podstawy) ⠠⠵ ./head.py --help
# usage: head.py [-h] [-n LINES] [-v] file

# positional arguments:
#   file                  File which should be displayed.

# options:
#   -h, --help            show this help message and exit
#   -n LINES, --lines LINES
#                         Number of lines to show.
#   -v, --verbose         Explain what is done.
#
#
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-05-20 - 21:40:28
# ╰─(podstawy) ⠠⠵ ./head.py -n 5 niema.txt
# Traceback (most recent call last):
#   File "/Users/tomasz/local_repo/studia_WSB/Systemy Operacyjne/./head.py", line 32, in <module>
#     with open(args.file) as f:
#          ^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'niema.txt'


# ---------------------------------------------------------------------------------
# Zadanie 2
# Zmień kod podany w Zadaniu 1 tak, by przy podaniu pliku nieistniejącego, zamiast kończyć się wyjątkiem program
# tłumaczył że należy podać istniejący plik tekstowy.

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--lines",
                    default=[10],
                    type=int,
                    nargs=1,
                    help="Number of lines to show.")
parser.add_argument("file", type=str, help="File which should be displayed.")
parser.add_argument("-v", "--verbose", action="store_true",
                    default=False, help="Explain what is done.")
args = parser.parse_args()

if args.verbose:
    print(f"Program is running with name {sys.argv[0]}")
    print(f"It will print {args.lines[0]} lines from {
          args.file} and terminate.")
    print("="*50)

try:
    with open(args.file) as f:
        for i in range(args.lines[0]):
            print(f.readline().strip())
except FileNotFoundError:
    print(f"Error: The file '{
          args.file}' does not exist. Please provide an existing text file.")

if args.verbose:
    print("="*50)

# TEST #
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-05-20 - 22:35:56
# ╰─(podstawy) ⠠⠵ ./head.py -n 5 niema.txt
# Error: The file 'niema.txt' does not exist. Please provide an existing text file.

# ------------------------------------------------------------------------------------------------------------
#
# Zadanie 3
# Utwórz link symboliczny do skryptu head.py, który będzie nosił nazwę tail.py. Uruchom skrypt tail.py z przełącznikiem
# --verbose. Co się zmieniło w wypisywanych przez skrypt treściach?
# Zmodyfikuj kod z Zadania 1 (lub Zadania 2) tak, żeby przy uruchomieniu tego skryptu z nazwą tail.py (np.
# przez link symboliczny) wyświetlone zostały n wierszy od końca pliku podanego jako argument. Zachowano ma być
# także domyślne działanie programu: przy uruchomieniu skryptu z nazwą head.py wiersze muszą być wyświetlane
# od początku pliku.
# W przypadku używania systemu Windows w celu stworzenia linku symbolicznego powinno zadziałać poniższe
# polecenie wykonane w konsoli Windows: - zamieniłem to na macOS i powłokę zsh
# mklink /d tail.py head.py

# Modyfikacja kodu z zadania 1, aby wyświetlać wiersze od końca pliku, jeśli skrypt jest uruchamiany pod nazwą tail.py.
# włożyłem to w MAIN, bo tak jest po prostu ładniej.


def main2():
    """
    Główna funkcja programu.
    Parsuje argumenty wiersza poleceń i wyświetla odpowiednią liczbę wierszy z pliku.
    Jeśli skrypt jest uruchamiany pod nazwą 'tail.py', wyświetla wiersze od końca pliku.
    """
    # Tworzenie parsera argumentów
    parser = argparse.ArgumentParser()

    # Dodawanie argumentów do parsera
    parser.add_argument('-n', '--lines',
                        default=[10],
                        type=int,
                        nargs=1,
                        help='Number of lines to show.')  # Liczba wierszy do wyświetlenia
    parser.add_argument('file',
                        type=str,
                        help='File which should be displayed.')  # Plik do wyświetlenia
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        default=False,
                        help='Explain what is done.')  # Tryb szczegółowy

    # Parsowanie argumentów
    args = parser.parse_args()

    # Jeśli tryb szczegółowy jest włączony, wyświetlanie szczegółowych informacji
    if args.verbose:
        print(f'Program is running with name {sys.argv[0]}')
        print(f'It will print {args.lines[0]} lines from {
              args.file} and terminate.')
        print('='*50)

    # Próba otwarcia i odczytu pliku
    try:
        with open(args.file) as f:
            lines = f.readlines()
            if os.path.basename(sys.argv[0]) == 'tail.py':
                # Jeśli nazwa skryptu to 'tail.py', wyświetl wiersze od końca
                lines_to_print = lines[-args.lines[0]:]
            else:
                # W przeciwnym razie wyświetl wiersze od początku
                lines_to_print = lines[:args.lines[0]]
            for line in lines_to_print:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{
              args.file}' not found. Please provide an existing text file.")
        return

    # Jeśli tryb szczegółowy jest włączony, wyświetlanie informacji końcowych
    if args.verbose:
        print('='*50)


if __name__ == "__main__":
    main2()


# TESTY
# Twozę symlinka
# ln -s head.py tail.py
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB on main✘✘✘ 24-06-09 - 9:04:17
# ╰─(podstawy) ⠠⠵ ln -s ~/local_repo/studia_WSB/Systemy\ Operacyjne/head.py ~/local_repo/studia_WSB/Systemy\ Operacyjne/tail.py
#
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB on main✘✘✘ 24-06-09 - 9:07:30
# ╰─(podstawy) ⠠⠵ ls -al Systemy\ Operacyjne
# total 24
# drwxr-xr-x   4 tomasz  staff   128  9 cze 09:10 .
# drwxr-xr-x  12 tomasz  staff   384  9 cze 09:08 ..
# -rwxr--r--   1 tomasz  staff  9450  9 cze 09:10 head.py
# lrwxr-xr-x   1 tomasz  staff    62  9 cze 09:10 tail.py -> /Users/tomasz/local_repo/studia_WSB/Systemy Operacyjne/head.py
#
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB on main✘✘✘ 24-06-09 - 9:10:59
# ╰─(podstawy) ⠠⠵ ./Systemy\ Operacyjne/tail.py --verbose
# usage: tail.py [-h] [-n LINES] [-v] file
# tail.py: error: the following arguments are required: file
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB on main✘✘✘ 24-06-09 - 9:11:49
# ╰─(podstawy) ⠠⠵
#
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB on main✘✘✘ 24-06-09 - 9:15:35
# ╰─(podstawy) ⠠⠵ ./Systemy\ Operacyjne/tail.py --help
# usage: tail.py [-h] [-n LINES] [-v] file

# positional arguments:
#   file                  File which should be displayed.

# options:
#   -h, --help            show this help message and exit
#   -n LINES, --lines LINES
#                         Number of lines to show.
#   -v, --verbose         Explain what is done.
#
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB on main✘✘✘ 24-06-09 - 9:17:17
# ╰─(podstawy) ⠠⠵ ./Systemy\ Operacyjne/tail.py --verbose Systemy\ Operacyjne/head.py
# Program is running with name ./Systemy Operacyjne/tail.py
# It will print 10 lines from Systemy Operacyjne/head.py and terminate.
# ==================================================

# # positional arguments:
# #   file                  File which should be displayed.

# # options:
# #   -h, --help            show this help message and exit
# #   -n LINES, --lines LINES
# #                         Number of lines to show.
# #   -v, --verbose         Explain what is done.

# ==================================================
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB on main✘✘✘ 24-06-09 - 9:17:34
# ╰─(podstawy) ⠠⠵ cd Systemy\ Operacyjne
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-06-09 - 9:18:30
# ╰─(podstawy) ⠠⠵ ls -al
# total 24
# drwxr-xr-x   4 tomasz  staff    128  9 cze 09:10 .
# drwxr-xr-x  12 tomasz  staff    384  9 cze 09:08 ..
# -rwxr--r--   1 tomasz  staff  11364  9 cze 09:18 head.py
# lrwxr-xr-x   1 tomasz  staff     62  9 cze 09:10 tail.py -> /Users/tomasz/local_repo/studia_WSB/Systemy Operacyjne/head.py
#
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-06-09 - 9:18:32
# ╰─(podstawy) ⠠⠵ ./tail.py -n 5 head.py
# -rwxr--r--   1 tomasz  staff  11364  9 cze 09:18 head.py
# lrwxr-xr-x   1 tomasz  staff     62  9 cze 09:10 tail.py -> /Users/tomasz/local_repo/studia_WSB/Systemy Operacyjne/head.py
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-06-09 - 9:18:32
# ╰─(podstawy) ⠠⠵
#
# Napisałem coś dla testu
# ╰─(podstawy) ⠠⠵ ./tail.py -n 15 head.py
# ╰─(podstawy) ⠠⠵ ls -al
# total 24
# drwxr-xr-x   4 tomasz  staff    128  9 cze 09:10 .
# drwxr-xr-x  12 tomasz  staff    384  9 cze 09:08 ..
# -rwxr--r--   1 tomasz  staff  11364  9 cze 09:18 head.py
# lrwxr-xr-x   1 tomasz  staff     62  9 cze 09:10 tail.py -> /Users/tomasz/local_repo/studia_WSB/Systemy Operacyjne/head.py
#
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-06-09 - 9:18:32
# ╰─(podstawy) ⠠⠵ ./tail.py -n 5 head.py
# -rwxr--r--   1 tomasz  staff  11364  9 cze 09:18 head.py
# lrwxr-xr-x   1 tomasz  staff     62  9 cze 09:10 tail.py -> /Users/tomasz/local_repo/studia_WSB/Systemy Operacyjne/head.py
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-06-09 - 9:18:32
# ╰─(podstawy) ⠠⠵
#
# Napisałem coś dla testu
# (podstawy) ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-06-09 - 9:22:42
# ╰─(podstawy) ⠠⠵

# ------------------------------------------------------------------------------------------------
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


def main3():
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
    main3()

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
# ╰─(podstawy) ⠠⠵ ./head.py -f 1,3 file2.csv
# Name    City
# John    New York
# Alice   Los Angeles
# Bob     Chicago
# Abdul   Kozo-jebca
# Ernest  London
#
# Testowanie przecinka, jako separatora  i wybranych kolumn:
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-06-09 - 10:03:26
# ╰─(podstawy) ⠠⠵ ./head.py -f 2,3 -d ',' file.csv

#  Age, City
#  25, New York
#  30, Los Angeles
#  22, Chicago
#  26, Kozo-jebca
#  56, London
#
# ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-06-09 - 10:04:41
# ╰─(podstawy) ⠠⠵ ./head.py -f 1,3 -d ',' file.csv
# Name, City
# John, New York
# Alice, Los Angeles
# Bob, Chicago
# Abdul, Kozo-jebca
# Ernest, London
