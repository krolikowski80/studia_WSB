# --------------------------------------------------------------
# Importy potrzebnych funkcji i bibliotek.
# --------------------------------------------------------------
# Umożliwia pobieranie gotowych zbiorów danych
from sklearn import datasets
# Służy do podziału danych na zbior uczący i testowy
from sklearn.model_selection import train_test_split
# Klasyfikator SVC (Support Vector Classifier)
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, precision_score, recall_score, f1_score
import numpy as np                       # Obsługa operacji numerycznych
import matplotlib.pyplot as plt          # Biblioteka do tworzenia wykresów
import os                                # Operacje na plikach i katalogach
import pandas as pd                      # Do zapisu wyników do Excela

# --------------------------------------------------------------
# (a) Wczytaj zbór danych.
# --------------------------------------------------------------
breast_cancer_data = datasets.load_breast_cancer()

# Tworzymy zmienne X i y, które będą zawierać odpowiednio:
#  - X = dane (cechy) próbek,
#  - y = etykiety (klasy) każdej próbki.
X = breast_cancer_data.data   # cechy (atrybuty) opisujące każdą próbkę
y = breast_cancer_data.target  # etykiety (np. 0 = malignant, 1 = benign)

# --------------------------------------------------------------
# (b) Podziel dane na zbior uczący i testujący
# --------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    shuffle=True
)

print("Rozmiar X_train:", X_train.shape)
print("Rozmiar X_test: ", X_test.shape)
print("Rozmiar y_train:", y_train.shape)
print("Rozmiar y_test: ", y_test.shape)

# --------------------------------------------------------------
# (c) Naucz klasyfikator SVC na danych uczących
# --------------------------------------------------------------
svc_clf = SVC()
svc_clf.fit(X_train, y_train)
print("\nModel SVC został wytrenowany na zbiorze uczącym (domyślne parametry).")

# --------------------------------------------------------------
# (d) Oblicz dokładność klasyfikacji (accuracy)
# --------------------------------------------------------------
y_pred_default = svc_clf.predict(X_test)
accuracy_default = accuracy_score(y_test, y_pred_default)
print("Dokładność klasyfikacji dla domyślnego SVC:", accuracy_default)

# --------------------------------------------------------------
# (e) Szukanie najlepszego parametru C dla linear i rbf
# --------------------------------------------------------------
C_values = [0.1, 1, 10, 100]
best_params = {}

for kernel in ['linear', 'rbf']:
    best_accuracy = 0
    best_C = None
    for C in C_values:
        clf = SVC(kernel=kernel, C=C)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"Kernel: {kernel}, C: {C}, Dokładność: {acc:.4f}")
        if acc > best_accuracy:
            best_accuracy = acc
            best_C = C
    best_params[kernel] = best_C
    print(
        f"Najlepsze C dla jądra '{kernel}': {best_C} z dokładnością {best_accuracy:.4f}\n")

# --------------------------------------------------------------
# (f) Naucz modele, zapisz wykresy i wyniki
# --------------------------------------------------------------
output_dir = "lab2_wyniki"
os.makedirs(output_dir, exist_ok=True)

results = []
classifiers = {}

for kernel in ['linear', 'rbf']:
    clf = SVC(kernel=kernel, C=best_params[kernel])
    clf.fit(X_train, y_train)
    classifiers[kernel] = clf

    y_pred = clf.predict(X_test)

    # Metryki
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()

    results.append({
        "Kernel": kernel,
        "Best C": best_params[kernel],
        "Accuracy": acc,
        "Precision": prec,
        "Recall": rec,
        "F1-score": f1,
        "True Positives (TP)": tp,
        "True Negatives (TN)": tn,
        "False Positives (FP)": fp,
        "False Negatives (FN)": fn
    })

    # Wykres: macierz konfuzji
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm, display_labels=breast_cancer_data.target_names)
    disp.plot(cmap=plt.cm.Blues)
    plt.title(
        f"Macierz konfuzji dla SVC (kernel='{kernel}', C={best_params[kernel]})")
    plt.savefig(os.path.join(output_dir, f"macierz_konfuzji_{kernel}.png"))
    plt.show()

    # Wykres: scatter rzeczywisty
    feature_idx = [0, 1]
    X_two = X[:, feature_idx]

    plt.figure()
    plt.scatter(X_two[:, 0], X_two[:, 1], c=y,
                cmap='viridis', edgecolor='k', s=50)
    plt.xlabel(breast_cancer_data.feature_names[0])
    plt.ylabel(breast_cancer_data.feature_names[1])
    plt.title(f"Rzeczywisty podział klas - {kernel} kernel")
    plt.savefig(os.path.join(output_dir, f"rzeczywisty_podzial_{kernel}.png"))
    plt.show()

    # Wykres: scatter predykcja
    y_pred_all = clf.predict(X)
    plt.figure()
    plt.scatter(X_two[:, 0], X_two[:, 1], c=y_pred_all,
                cmap='viridis', edgecolor='k', s=50)
    plt.xlabel(breast_cancer_data.feature_names[0])
    plt.ylabel(breast_cancer_data.feature_names[1])
    plt.title(
        f"Predykcje klasyfikatora (kernel='{kernel}', C={best_params[kernel]})")
    plt.savefig(os.path.join(output_dir, f"predykcja_{kernel}.png"))
    plt.show()

# Zapis do Excela
excel_path = os.path.join(output_dir, "rozszerzone_wyniki_klasyfikacji.xlsx")
df = pd.DataFrame(results)
df.to_excel(excel_path, index=False)
print("\n Wyniki i wykresy zapisane w katalogu 'lab2_wyniki'")
