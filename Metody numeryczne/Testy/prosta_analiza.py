import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych
df = pd.read_csv("sales_data.csv", parse_dates=["Data"])

# Podsumowanie danych (z pominięciem daty)
print(df[["Ilość", "Cena"]].describe())

# Dodanie kolumny 'Miesiąc' w formacie odpowiednim do grupowania
df["Miesiąc"] = df["Data"].dt.to_period("M")

# Analiza sprzedaży w czasie (sumowanie 'Cena' dla każdego miesiąca)
monthly_sales = df.groupby("Miesiąc")["Cena"].sum()
plt.figure(figsize=(10, 6))
monthly_sales.plot()
plt.title("Całkowita sprzedaż miesięczna")
plt.xlabel("Miesiąc")
plt.ylabel("Całkowita sprzedaż")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Porównanie produktów (sumowanie 'Ilość' dla każdego produktu)
product_sales = df.groupby("Produkt")["Ilość"].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
product_sales.plot(kind="bar")
plt.title("Całkowita ilość sprzedanych jednostek dla każdego produktu")
plt.xlabel("Produkt")
plt.ylabel("Ilość")
plt.tight_layout()
plt.show()

# Analiza cenowa (histogram cen jednostkowych)
plt.figure(figsize=(10, 6))
plt.hist(df["Cena"], bins=20, edgecolor="black")
plt.title("Histogram cen jednostkowych produktów")
plt.xlabel("Cena")
plt.ylabel("Liczba produktów")
plt.tight_layout()
plt.show()

# Zależność między ceną a ilością sprzedanych produktów (wykres punktowy)
plt.figure(figsize=(10, 6))
plt.scatter(df["Cena"], df["Ilość"], alpha=0.5)
plt.title("Zależność między ceną a ilością sprzedanych produktów")
plt.xlabel("Cena")
plt.ylabel("Ilość")
plt.tight_layout()
plt.show()
