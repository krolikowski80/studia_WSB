# Zadania do wykonania na zajęciach

# zad 1. Napisz funkcję, sprawdzającą czy wszystkie otwarte nawiasy okrągłe w napisie zostały zamknięte prawidłowo.
# Funkcja ma wykorzystywać do tego celu stos.
# isvalid('(())')
# True
# isvalid('((2 + 5) * (2 + 3)) / 2')
# True
# isvalid('(()')
# False
# isvalid('))((')
# False


def isvalid(s):
    """sprawdza czy wszystkie otwarte nawiasy okrągłe w napisie zostały zamknięte prawidłowo"""
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        else:
            continue
    if len(stack) == 0:
        return True
    else:
        return False


# testowanie funkcji
print(isvalid("(())"))
print(isvalid("((2 + 5) * (2 + 3)) / 2"))
print(isvalid("(()"))
print(isvalid("))(("))

# ---------------------------------------------------------------------
# Zad 2.

# Napisz funkcję która obliczy wartość wyrażenia matematycznego zapisanego
# w postfiksowej postaci (odwrotna notacja polska). Do obliczeń należy wykorzystać stos.
# calculate('2 3 + 5 *')
# 25
# calculate('2 7 + 3 / 14 3 - 4 * + 2 /')
# 23.5


def calculate(s):
    """obliczy wartość wyrażenia matematycznego zapisanego w postfiksowej postaci (odwrotna notacja polska)"""
    stack = []
    tokens = s.split()

    for i in tokens:
        if i in ["+", "-", "*", "/"]:
            a = stack.pop()
            b = stack.pop()
            if i == "+":
                stack.append(a + b)
            elif i == "-":
                stack.append(b - a)
            elif i == "*":
                stack.append(a * b)
            elif i == "/":
                stack.append(b / a)
        else:
            stack.append(float(i))
    return stack.pop()


# Testowanie funkcji
print(calculate("2 3 + 5 *"))
print(calculate("2 7 + 3 / 14 3 - 4 * + 2 /"))

# ---------------------------------------------------------------------

# Zad 3.
# Napisać funkcję symulującą działanie oprogramowania „planisty” w systemie operacyjnym. W
# rzeczywistych systemach operacyjnych program ten przydziela poszczególnym procesom w systemie
# zasoby procesora tak, by dla użytkownika wyglądało to tak, jakby wszystkie procesy działały
# naraz.
# Implementowana funkcja powinna przyjmować listę krotek, gdzie każda krotka określa nazwę
# procesu oraz liczbę nanosekund potrzebnych do zakończenia procesu, a także ile nanosekund
# pracy procesora powinno być przydzielano (zmienna n). Lista procesów powinna być następnie
# potraktowana jako kolejka procesów do wykonania, z którą należy postępować następująco:
# (a) Pobierz proces z kolejki.
# (b) Zmniejsz czas który pozostał mu do zakończenia o n.
# (c) Jeżeli proces się zakończył (w wyniku dostaliśmy czas 0 lub poniżej), to zapisujemy jego
# nazwę na listę procesów zakończonych.
# (d) Jeżeli procesowi jeszcze pozostał jakiś czas pracy, to z prawdopodobieństwem p dodaj do
# pozostałego czasu wykonania losową liczbę z zakresu [0, 100]. I dopisz ten proces na koniec
# kolejki
# Jako wynik działania funkcji proszę zwrócić listę zakończonych procesów w takiej kolejności w
# jakiej one były kończone, a także nazwy procesów którym zabrakło czasu (nie wykonały się w
# czasie max_time) - będą to procesy pozostałe w kolejce gdy skończy nam się czas.
# Przykładowe uruchomienie programu i przykładowe wyniki.
# processes = [
# ('git status', 25),
# ('python calculations.p', 534),
# ('gcc main.c', 1348),
# ('screenshot', 105)
# ]
# print(scheduler(processes, n=4, p=0.2, max_time=1000))
# ([’git status’, ’screenshot’, ’python calculations.py’], [’gcc main.c’])
import random
from collections import deque


def scheduler(processes, n, p, max_time):
    queue = deque(processes)
    finished = []
    remaining_time = max_time

    while queue and remaining_time > 0:
        process_name, process_time = queue.popleft()
        process_time -= n
        remaining_time -= n

        if process_time <= 0:
            finished.append(process_name)
        else:
            if random.random() < p:
                process_time += random.randint(0, 100)
            queue.append((process_name, process_time))

    return finished, [process[0] for process in queue]


# Przykładowe wywołanie funkcji
processes = [
    ("git status", 25),
    ("python calculations.py", 534),
    ("gcc main.c", 1348),
    ("screenshot", 105),
]
print(scheduler(processes, n=4, p=0.2, max_time=1000))


# -----------------------------------------------------------------------------

# Zad 4.
# Napisać funkcje, symulującą działanie placówki „Poczta Polska”. Funkcja ta ma otrzymać na
# wejściu listę krotek, zawierających po kolei imię klienta oraz czy po spędzeniu tego czasu będzie
# musiał wrócić do okienka (by np. wypełnić potwierdzenie nadania i wrócić wysłać list). Funkcja
# powinna używać kolejki.
# Kolejka powinna być obsługiwana następująco:
# (a) Pobierz osobę na początku kolejki.
# (b) Sprawdź czy osoba musi coś wysłać.
# (c) Jeżeli tak to dopisz na koniec kolejki.
# (d) Jeżeli nie to dopisz do listy osób wychodzących z poczty.

from collections import deque


def postoffice(customers):
    line = deque(customers)
    left_postoffice = []

    while line:
        name, must_back = line.popleft()

        if must_back:
            line.append((name, False))
        else:
            left_postoffice.append(name)

    return left_postoffice


klienci = [("Jan", True), ("Anna", False), ("Paweł", True), ("Kasia", False)]
print(postoffice(klienci))
