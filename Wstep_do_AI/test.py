from sklearn.datasets import fetch_california_housing
import pandas as pd

# Wczytanie zbioru danych
cal_housing = fetch_california_housing(as_frame=True)
df_head = cal_housing.frame.head()

# Zapisanie pierwszych wierszy do pliku CSV (opcjonalnie)
df_head.to_csv("pierwsze_wiersze.csv", index=False)

# Wyświetlenie pierwszych wierszy
print(df_head)