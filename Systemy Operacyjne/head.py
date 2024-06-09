#!/Users/tomasz/.pyenv/versions/3.12.0/bin/python

# # Zadanie 1
# # # Zapoznaj się z poniższym kodem, który przedstawia uproszczoną wersję polecenia head, zaimplementowaną w
# # Python. Implementacja ta używa modułu argparse w celu obsługi argumentów wiersza poleceń.
# # Więcej o tym modułu można poczytać w dokumentacji: https://docs.python.org/3/library/argparse.html,
# # oraz https://docs.python.org/3/howto/argparse.html.
# # Przepisz i uruchom ten program, sprawdź czy działa poprawnie, zbadaj działanie przełączników -n, --lines,
# # -v, --verbose, --help. Sprawdź co będzie jeżeli podać plik który nie istnieje.

# import sys
# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument("-n", "--lines",
#                     default=[10],
#                     type=int,
#                     nargs=1,
#                     help="Number of lines to show.")
# parser.add_argument("file", type=str, help="File which should be displayed.")
# parser.add_argument("-v", "--verbose", action="store_true",
#                     default=False, help="Explain what is done.")
# args = parser.parse_args()

# if args.verbose:
#     print(f"Program is running with name {sys.argv[0]}")
#     print(f"It will print {args.lines[0]} lines from {
#           args.file} and terminate.")
#     print("="*50)

# with open(args.file) as f:
#     for i in range(args.lines[0]):
#         print(f.readline().strip())

# if args.verbose:
#     print("="*50)

# ## TESTY ##
# #
# # (podstawy) ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-05-20 - 21:34:13
# # ╰─(podstawy) ⠠⠵ ./head.py -v head.py
# # Program is running with name ./head.py
# # It will print 10 lines from head.py and terminate.
# # ==================================================
# # #!/Users/tomasz/.pyenv/versions/3.12.0/bin/python
# # import sys
# # import argparse

# # parser = argparse.ArgumentParser()

# # parser.add_argument("-n", "--lines",
# # default=[10],
# # type=int,
# # nargs=1,
# # ==================================================
# #
# # ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-05-20 - 21:37:45
# # ╰─(podstawy) ⠠⠵ ./head.py --verbose head.py
# # Program is running with name ./head.py
# # It will print 10 lines from head.py and terminate.
# # ==================================================
# # #!/Users/tomasz/.pyenv/versions/3.12.0/bin/python
# # import sys
# # import argparse

# # parser = argparse.ArgumentParser()

# # parser.add_argument("-n", "--lines",
# # default=[10],
# # type=int,
# # nargs=1,
# # ==================================================
# #
# # ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-05-20 - 21:37:54
# # ╰─(podstawy) ⠠⠵ ./head.py -n 15 head.py
# # #!/Users/tomasz/.pyenv/versions/3.12.0/bin/python
# # import sys
# # import argparse

# # parser = argparse.ArgumentParser()

# # parser.add_argument("-n", "--lines",
# # default=[10],
# # type=int,
# # nargs=1,
# # help="Number of lines to show.")
# # parser.add_argument("file", type=str, help="File which should be displayed.")
# # parser.add_argument("-v", "--verbose", action="store_true",
# # default=False, help="Explain what is done.")
# # args = parser.parse_args()
# #
# # Listing pierwszych 15 linii pliku.
# #
# #
# # ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-05-20 - 21:40:24
# # ╰─(podstawy) ⠠⠵ ./head.py --help
# # usage: head.py [-h] [-n LINES] [-v] file

# # positional arguments:
# #   file                  File which should be displayed.

# # options:
# #   -h, --help            show this help message and exit
# #   -n LINES, --lines LINES
# #                         Number of lines to show.
# #   -v, --verbose         Explain what is done.
# #
# #
# # ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-05-20 - 21:40:28
# # ╰─(podstawy) ⠠⠵ ./head.py -n 5 niema.txt
# # Traceback (most recent call last):
# #   File "/Users/tomasz/local_repo/studia_WSB/Systemy Operacyjne/./head.py", line 32, in <module>
# #     with open(args.file) as f:
# #          ^^^^^^^^^^^^^^^
# # FileNotFoundError: [Errno 2] No such file or directory: 'niema.txt'


# # ---------------------------------------------------------------------------------
# # Zadanie 2
# # Zmień kod podany w Zadaniu 1 tak, by przy podaniu pliku nieistniejącego, zamiast kończyć się wyjątkiem program
# # tłumaczył że należy podać istniejący plik tekstowy.

# import sys
# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument("-n", "--lines",
#                     default=[10],
#                     type=int,
#                     nargs=1,
#                     help="Number of lines to show.")
# parser.add_argument("file", type=str, help="File which should be displayed.")
# parser.add_argument("-v", "--verbose", action="store_true",
#                     default=False, help="Explain what is done.")
# args = parser.parse_args()

# if args.verbose:
#     print(f"Program is running with name {sys.argv[0]}")
#     print(f"It will print {args.lines[0]} lines from {
#           args.file} and terminate.")
#     print("="*50)

# try:
#     with open(args.file) as f:
#         for i in range(args.lines[0]):
#             print(f.readline().strip())
# except FileNotFoundError:
#     print(f"Error: The file '{
#           args.file}' does not exist. Please provide an existing text file.")

# if args.verbose:
#     print("="*50)

# # TEST #
# # ╭─tomasz at iMac (Tomasz) in ~/local_repo/studia_WSB/Systemy Operacyjne on main✘✘✘ 24-05-20 - 21:41:56
# # ╰─(podstawy) ⠠⠵ ./head.py -n 5 niema.txt
# # Error: The file 'niema.txt' does not exist. Please provide an existing text file.