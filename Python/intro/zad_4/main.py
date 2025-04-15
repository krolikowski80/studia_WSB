"""
Lab 4 - MCDM z użyciem biblioteki pymcdm
Autor: Tomasz Królikowski
Cel: Porównanie metod TOPSIS i SPOTIS na przykładowym zbiorze danych
"""

import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.normalizations import MinMax
from pymcdm.helpers import rankdata
import matplotlib.pyplot as plt

# --- Dane wejściowe ---

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

# Normalizacja danych
normalizer = MinMax()

# --- Metoda TOPSIS ---
topsis = TOPSIS(normalizer)
topsis_scores = topsis(decision_matrix, weights, types)
topsis_ranking = rankdata(topsis_scores, descending=True)

# --- Metoda SPOTIS ---
spotis = SPOTIS()
spotis_scores = spotis(decision_matrix, weights, types)
spotis_ranking = rankdata(spotis_scores, descending=False)

# --- Wyniki ---
df = pd.DataFrame({
    'Alternatywa': ['A', 'B', 'C', 'D'],
    'TOPSIS Score': topsis_scores,
    'TOPSIS Ranking': topsis_ranking,
    'SPOTIS Score': spotis_scores,
    'SPOTIS Ranking': spotis_ranking
})

print(df)

# Zapisz wyniki do pliku
df.to_excel("wyniki/wyniki_topsis_spotis.xlsx", index=False)

# Tworzymy wykres słupkowy porównujący wyniki TOPSIS i SPOTIS
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

# Zapisujemy wykres do pliku
plt.savefig('wyniki/wykres.png')
plt.close()
