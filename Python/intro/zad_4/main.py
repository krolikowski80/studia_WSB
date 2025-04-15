"""
Lab 4 - MCDM z użyciem biblioteki pymcdm
Autor: Tomasz Królikowski
Cel: Porównanie metod TOPSIS i SPOTIS na przykładowym zbiorze danych
"""

# --- Import niezbędnych bibliotek ---
# numpy - operacje na macierzach i danych numerycznych
# pandas - tworzenie i zapisywanie tabel z wynikami
# pymcdm - biblioteka do metod wielokryterialnego podejmowania decyzji (MCDM)
# matplotlib - tworzenie wykresów

import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.normalizations import minmax_normalization
from pymcdm.helpers import rankdata
import matplotlib.pyplot as plt

# --- Dane wejściowe ---
# Przygotowujemy macierz decyzyjną (alternatywy i kryteria)
# Definiujemy wagi kryteriów oraz typy (maksymalizuj lub minimalizuj)

# Macierz decyzyjna: wiersze = alternatywy, kolumny = kryteria
decision_matrix = np.array([
    [25000, 7.5, 5],   # Auto A
    [22000, 8.0, 6],   # Auto B
    [27000, 6.5, 4],   # Auto C
    [24000, 7.0, 7]    # Auto D
])

# Wagi kryteriów (suma = 1)
weights = np.array([0.5, 0.3, 0.2])

# Typy kryteriów: 1 = maksymalizuj, -1 = minimalizuj
types = np.array([-1, 1, 1])  # Koszt minimalizowany, reszta maksymalizowana

# --- Zastosowanie metody TOPSIS ---
# Normalizacja danych i wyznaczenie wyników metodą TOPSIS
# Obliczamy ranking na podstawie wyników (im wyższy wynik, tym lepsza alternatywa)

topsis = TOPSIS(normalization_function=minmax_normalization)
topsis_scores = topsis(decision_matrix, weights, types)
topsis_ranking = rankdata(-topsis_scores)

# --- Zastosowanie metody SPOTIS ---
# Wyznaczenie zakresów wartości (bounds) dla każdego kryterium
# Obliczenie wyników metodą SPOTIS i przypisanie rankingów (niższy wynik = lepsza alternatywa)

# Wyznaczenie bounds: [min, max] dla każdego kryterium
min_ = decision_matrix.min(axis=0)
max_ = decision_matrix.max(axis=0)
bounds = np.array([[min_[i], max_[i]] for i in range(decision_matrix.shape[1])])

spotis = SPOTIS(bounds)
spotis_scores = spotis(decision_matrix, weights, types)
spotis_ranking = rankdata(spotis_scores)

# --- Przygotowanie wyników do analizy ---
# Tworzymy DataFrame z wynikami obu metod i rankingami

df = pd.DataFrame({
    'Alternatywa': ['A', 'B', 'C', 'D'],
    'TOPSIS Score': topsis_scores,
    'TOPSIS Ranking': topsis_ranking,
    'SPOTIS Score': spotis_scores,
    'SPOTIS Ranking': spotis_ranking
})

# --- Zapis wyników do pliku Excel ---
# Eksportujemy wyniki do pliku Excel w folderze 'wyniki'

print(df)
df.to_excel("wyniki/wyniki_topsis_spotis.xlsx", index=False)

# --- Tworzenie wykresu porównawczego ---
# Wykres słupkowy porównujący wyniki TOPSIS i SPOTIS dla każdej alternatywy

labels = ['A', 'B', 'C', 'D']
x = np.arange(len(labels))  # lokalizacje słupków
width = 0.35  # szerokość słupka

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, topsis_scores, width, label='TOPSIS')
rects2 = ax.bar(x + width/2, spotis_scores, width, label='SPOTIS')

# Opis wykresu
ax.set_ylabel('Scores')
ax.set_title('Porównanie wyników metod TOPSIS i SPOTIS')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

# --- Zapis wykresu do pliku ---
# Zapisujemy wykres jako plik PNG w folderze 'wyniki'

plt.savefig('wyniki/wykres.png')
plt.close()
