import matplotlib.pyplot as plt

# Dane
dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Ndz"]
temperatury = [22, 24, 19, 23, 25, 27, 26]

# Tworzenie wykresu
plt.plot(dni, temperatury)

# Dodanie tytułu i etykiet osi
plt.title("Średnie temperatury w ciągu tygodnia")
plt.xlabel("Dni tygodnia")
plt.ylabel("Temperatura (°C)")

# Wyświetlenie wykresu
plt.show()
