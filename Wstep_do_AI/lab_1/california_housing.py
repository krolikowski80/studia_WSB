import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# =====================================================================
# (a) Wczytaj zbiór danych California Housing
# =====================================================================

# Pobranie danych
california = fetch_california_housing()
X = pd.DataFrame(california.data, columns=california.feature_names)
y = california.target

# Zapisywanie pierwszych wierszy do pliku Excel
df = X.copy()
df["MedHouseVal"] = y
df.head().to_excel("pierwsze_wiersze.xlsx", index=False)

# =====================================================================
# (b) Wykonaj 8 wykresów pokazujących zależność zmiennej zależnej y od zmiennych X
# =====================================================================

# Tworzenie katalogu na wykresy
os.makedirs("charts_all_features", exist_ok=True)

# Generowanie wykresów dla każdej cechy
for column in X.columns:
    plt.figure(figsize=(6, 4))
    plt.scatter(X[column], y, alpha=0.5, edgecolors="k")
    plt.xlabel(column)
    plt.ylabel("MedHouseVal")
    plt.title(f"{column} vs MedHouseVal")
    plt.grid(True)
    
    # Zapisywanie wykresu
    plt.savefig(f"charts_all_features/{column}_vs_MedHouseVal.png")
    plt.close()

# =====================================================================
# (c) Podział na zbiór uczący i testowy
# =====================================================================

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Zapisanie rozmiarów zbiorów do pliku Excel
rozmiary_df = pd.DataFrame({
    "Zbiór": ["X_train", "X_test", "y_train", "y_test"],
    "Liczba próbek": [X_train.shape[0], X_test.shape[0], y_train.shape[0], y_test.shape[0]],
    "Liczba cech": [X_train.shape[1], X_test.shape[1], "-", "-"]
})
rozmiary_df.to_excel("rozmiary_zbiorow.xlsx", index=False)

# =====================================================================
# (d) Naucz model LinearRegression na danych uczących
# =====================================================================

model = LinearRegression()
model.fit(X_train, y_train)

# Zapisanie współczynników regresji do pliku Excel
coef_df = pd.DataFrame({"Cecha": X.columns, "Współczynnik": model.coef_})
coef_df.to_excel("wspolczynniki_regresji.xlsx", index=False)

# =====================================================================
# (e) Oblicz błędy MAE i MSE na danych uczących i testowych
# =====================================================================

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

mae_train = mean_absolute_error(y_train, y_train_pred)
mse_train = mean_squared_error(y_train, y_train_pred)

mae_test = mean_absolute_error(y_test, y_test_pred)
mse_test = mean_squared_error(y_test, y_test_pred)

# Zapisanie wyników modelu wielowymiarowego
wyniki_modelu_df = pd.DataFrame({
    "Zbiór": ["Train", "Test"],
    "MAE": [mae_train, mae_test],
    "MSE": [mse_train, mse_test]
})
wyniki_modelu_df.to_excel("wyniki_modelu.xlsx", index=False)

# =====================================================================
# (f) Regresja jednowymiarowa dla każdej cechy
# =====================================================================

os.makedirs("charts_single_feature", exist_ok=True)

wyniki_cech = []

for feature in X.columns:
    X_train_single = X_train[[feature]]
    X_test_single = X_test[[feature]]
    
    model_single = LinearRegression()
    model_single.fit(X_train_single, y_train)
    
    y_train_pred_single = model_single.predict(X_train_single)
    y_test_pred_single = model_single.predict(X_test_single)
    
    mae_train_single = mean_absolute_error(y_train, y_train_pred_single)
    mse_train_single = mean_squared_error(y_train, y_train_pred_single)
    
    mae_test_single = mean_absolute_error(y_test, y_test_pred_single)
    mse_test_single = mean_squared_error(y_test, y_test_pred_single)
    
    wyniki_cech.append([feature, mae_train_single, mse_train_single, mae_test_single, mse_test_single])

    # Tworzenie wykresu regresji dla pojedynczej cechy
    plt.figure(figsize=(6, 4))
    plt.scatter(X_test_single, y_test, alpha=0.5, edgecolors="k", label="Dane rzeczywiste")
    plt.plot(X_test_single, y_test_pred_single, color="red", label="Regresja")
    plt.xlabel(feature)
    plt.ylabel("MedHouseVal")
    plt.title(f"Regresja dla cechy {feature}")
    plt.legend()
    plt.grid(True)
    
    plt.savefig(f"charts_single_feature/{feature}_regression.png")
    plt.close()

# Zapisywanie wyników regresji dla poszczególnych cech
wyniki_cech_df = pd.DataFrame(wyniki_cech, columns=["Cecha", "MAE (train)", "MSE (train)", "MAE (test)", "MSE (test)"])
wyniki_cech_df.to_excel("wyniki_cech.xlsx", index=False)

# =====================================================================
# Wykres: Model Wielowymiarowy - rzeczywiste vs. przewidywane wartości
# =====================================================================

os.makedirs("charts_multifeature", exist_ok=True)

plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_test_pred, alpha=0.5, edgecolors="k", label="Predykcja modelu")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color="red", linestyle="--", label="Idealna linia")
plt.xlabel("Rzeczywiste wartości cen domów")
plt.ylabel("Przewidywane wartości cen domów")
plt.title("Wielowymiarowy model regresji: Rzeczywiste vs. Przewidywane")
plt.legend()
plt.grid(True)

plt.savefig("charts_multifeature/Wielowymiarowy_model.png")
plt.close()
