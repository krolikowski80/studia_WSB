
def proste(n):
    x = 0
    for i in n:
        x += 1
        if i == 9:
            print(f"Znalazłem cyfrę 9 w {x} operacji")
            return
    print("Nie znalazłem cyfry 9")


L = [1, 4, 6, 3, 9, 0]
proste(L)