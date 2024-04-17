
def binarne(zestaw, szukana):
    lewa = 0
    prawa = len(zestaw)-1
    srodek = 0
    while lewa < prawa:
        srodek = (lewa + prawa) // 2
        if zestaw[srodek] == szukana:
            return srodek
        else:
            if zestaw[srodek] < szukana:
                lewa = srodek + 1
            else:
                prawa = srodek
    print(f"Nie znalazłem cyfry {szukana}")


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
A = 15
print(binarne(L, A))
