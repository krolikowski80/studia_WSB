# Zaimplementować wzór na obliczenie n-tego wyrazu ciągu Fibonacciego (wzór poniżej) w sposóbiteracyjny.
# 0, n = 0
# 1, n = 1
# an−2 + an−1, n > 1

def fibonacci(n):
    """Obliczanie Fibonacciego w sposób iteracyjny"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            c = a + b
            a, b = b, c
        return b


n = int(input("Podaj liczbę n: "))
print(f"Wartość {n}-tego wyrazu ciągu Fibonacciego: {fibonacci(n)}")
