import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# =====================================================================
# (a) Wczytaj zbiór danych California Housing z biblioteki scikit-learn
# =====================================================================
cal_housing = fetch_california_housing(
    as_frame=True)  # Pobieramy dane jako DataFrame

# Konwersja na DataFrame
# Ten zbiór zawiera cechy opisujące nieruchomości oraz medianę cen domów w tysiącach USD
df = cal_housing.frame

# Podział danych na zmienną zależną (y - cel predykcji) oraz cechy (X - dane wejściowe)
y = df["MedHouseVal"]  # kolumna z medianą cen domów
# usuwamy kolumnę z cenami, by pozostały tylko cechy
X = df.drop(columns=["MedHouseVal"])

# =====================================================================
# (b) Tworzenie katalogów na wykresy (jeśli jeszcze ich nie ma)
# =====================================================================
# katalog na wykresy wszystkich cech
os.makedirs("charts_all_features", exist_ok=True)
# katalog na wykresy pojedynczych cech
os.makedirs("charts_single_feature", exist_ok=True)

# =====================================================================
# (c) Podział danych na zbiór uczący i testowy (70% train, 30% test)
# =====================================================================
# Dzięki temu model będzie się uczył na 70% danych, a 30% wykorzystamy do sprawdzenia jakości predykcji
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Lista na wyniki do Excela
results = []

# =====================================================================
# (d) Tworzenie wykresów punktowych dla każdej cechy względem MedHouseVal
# =====================================================================
# Każdy wykres pokaże, jak zmiana danej cechy wpływa na wartość domów
for col in X.columns:
    plt.figure()
    plt.scatter(X[col], y, alpha=0.5)
    plt.xlabel(col)
    plt.ylabel("MedHouseVal")
    plt.title(f"Zależność {col} vs MedHouseVal")
    # zapis wykresu do pliku
    plt.savefig(f"charts_all_features/{col}_vs_MedHouseVal.png")
    plt.close()

# =====================================================================
# (e) Model regresji liniowej wykorzystujący wszystkie cechy naraz (wielowymiarowy)
# =====================================================================
model_multi = LinearRegression()  # Tworzymy model regresji liniowej
model_multi.fit(X_train, y_train)  # Trenujemy model na zbiorze uczącym

# Predykcja wartości domów dla danych treningowych i testowych
y_train_pred_multi = model_multi.predict(X_train)
y_test_pred_multi = model_multi.predict(X_test)

# Obliczenie błędów predykcji
mae_train_multi = mean_absolute_error(
    y_train, y_train_pred_multi)  # Średni błąd bezwzględny
mse_train_multi = mean_squared_error(
    y_train, y_train_pred_multi)  # Średni błąd kwadratowy
mae_test_multi = mean_absolute_error(y_test, y_test_pred_multi)
mse_test_multi = mean_squared_error(y_test, y_test_pred_multi)

# Dodanie wyników do listy, która trafi do Excela
results.append(["Wielowymiarowy", mae_train_multi,
               mse_train_multi, mae_test_multi, mse_test_multi])

# =====================================================================
# (f) Regresja liniowa dla każdej pojedynczej cechy osobno
# =====================================================================
# Sprawdzamy, jak dobrze pojedyncze cechy przewidują cenę domów
for col in X.columns:
    X_train_single = X_train[[col]]
    X_test_single = X_test[[col]]

    model_single = LinearRegression()
    model_single.fit(X_train_single, y_train)

    y_train_pred_single = model_single.predict(X_train_single)
    y_test_pred_single = model_single.predict(X_test_single)

    mae_train_single = mean_absolute_error(y_train, y_train_pred_single)
    mse_train_single = mean_squared_error(y_train, y_train_pred_single)
    mae_test_single = mean_absolute_error(y_test, y_test_pred_single)
    mse_test_single = mean_squared_error(y_test, y_test_pred_single)

    # Dodajemy wyniki modelu jednowymiarowego do tabeli wyników
    results.append([col, mae_train_single, mse_train_single,
                   mae_test_single, mse_test_single])

    # Tworzymy wykres regresji dla pojedynczej cechy
    plt.figure()
    plt.scatter(X_train_single, y_train, alpha=0.5, label="dane treningowe")

    x_vals = np.linspace(X_train_single.min(), X_train_single.max(), 100)
    x_vals_df = pd.DataFrame(x_vals, columns=[col])
    y_vals = model_single.predict(x_vals_df)

    plt.plot(x_vals, y_vals, label="linia regresji", color='orange')
    plt.xlabel(col)
    plt.ylabel("MedHouseVal")
    plt.title(f"Regresja liniowa (1D) dla cechy {col}")
    plt.legend()
    # Zapisujemy wykres
    plt.savefig(f"charts_single_feature/{col}_regression.png")
    # plt.close()
    plt.show()

# =====================================================================
# (g) Zapis wyników do Excela
# =====================================================================
columns = ["Model", "MAE_train", "MSE_train", "MAE_test", "MSE_test"]
df_results = pd.DataFrame(results, columns=columns)
df_results.to_excel("wyniki_modeli.xlsx", index=False)

print("Analiza zakończona, wyniki zapisano do wyniki_modeli.xlsx i wykresy do charts_all_features.")
