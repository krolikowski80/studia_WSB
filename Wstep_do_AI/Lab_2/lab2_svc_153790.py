# --------------------------------------------------------------
# Importy potrzebnych funkcji i bibliotek.
# --------------------------------------------------------------
from sklearn import datasets             # Umożliwia pobieranie gotowych zbiorów danych
from sklearn.model_selection import train_test_split  # Służy do podziału danych na zbiór uczący i testowy
from sklearn.svm import SVC              # Klasyfikator SVC (Support Vector Classifier)
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay  # Metryki oceny modelu
import numpy as np                       # Obsługa operacji numerycznych
import matplotlib.pyplot as plt          # Biblioteka do tworzenia wykresów

# --------------------------------------------------------------
# (a) Wczytaj zbiór danych.
# --------------------------------------------------------------
breast_cancer_data = datasets.load_breast_cancer()

# Tworzymy zmienne X i y, które będą zawierać odpowiednio:
#  - X = dane (cechy) próbek,
#  - y = etykiety (klasy) każdej próbki.
X = breast_cancer_data.data   # cechy (atrybuty) opisujące każdą próbkę
y = breast_cancer_data.target # etykiety (np. 0 = malignant, 1 = benign)

# --------------------------------------------------------------
# (b) Podziel dane na zbiór uczący i testujący za pomocą funkcji train_test_split w proporcji
# 0.7 danych uczących i 0.3 testowych: 
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
#
# 1. Funkcja train_test_split losowo dzieli dane na część uczącą (70%) i testową (30%).
# 2. test_size=0.3 oznacza, że 30% danych trafia do zbioru testowego, a 70% do zbioru uczącego.
# 3. random_state=42 ustala ziarno losowości, co pozwala uzyskać powtarzalny podział.
# 4. shuffle=True powoduje, że dane są mieszane przed podziałem.
# --------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    shuffle=True
)

# Sprawdzamy rozmiary powstałych zbiorów, aby upewnić się, że podział przebiegł poprawnie.
print("Rozmiar X_train:", X_train.shape)
print("Rozmiar X_test: ", X_test.shape)
print("Rozmiar y_train:", y_train.shape)
print("Rozmiar y_test: ", y_test.shape)

# --------------------------------------------------------------
# (c) Naucz klasyfikatory SVC na danych uczących.
#
# 1. Tworzymy obiekt klasyfikatora SVC z domyślnymi parametrami (kernel='rbf', C=1.0).
# 2. Metoda fit(X_train, y_train) trenuje model na zbiorze uczącym.
# --------------------------------------------------------------
svc_clf = SVC()
svc_clf.fit(X_train, y_train)
print("\nModel SVC został wytrenowany na zbiorze uczącym (domyślne parametry).")

# --------------------------------------------------------------
# (d) Oblicz dokładność klasyfikacji (accuracy) na zbiorze danych testowych.
#
# Używamy funkcji accuracy_score, aby porównać etykiety prawdziwe (y_test)
# z predykcjami uzyskanymi za pomocą metody predict.
# --------------------------------------------------------------
y_pred_default = svc_clf.predict(X_test)
accuracy_default = accuracy_score(y_test, y_pred_default)
print("Dokładność klasyfikacji dla domyślnego SVC:", accuracy_default)

# --------------------------------------------------------------
# (e) Powtórz punkty (c) i (d) w celu znalezienia optymalnego parametru C
#     oraz przebadania wpływu argumentu kernel ('linear' oraz 'rbf').
#
# Dla obu rodzajów jądra (kernel) sprawdzamy, jak zmienia się dokładność modelu dla różnych wartości C.
# --------------------------------------------------------------
C_values = [0.1, 1, 10, 100]  # Lista wartości parametru C do przetestowania
best_params = {}              # Słownik do zapamiętania najlepszego C dla każdego typu jądra

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
    print(f"Najlepsze C dla jądra '{kernel}': {best_C} z dokładnością {best_accuracy:.4f}\n")

# --------------------------------------------------------------
# (f) Naucz dwa klasyfikatory: jeden z kernel='linear' oraz drugi z kernel='rbf',
#     przy użyciu optymalnych wartości C znalezionych w punkcie (e). 
#
# Dla każdego z nich wykonaj:
# 1. Stwórz macierz konfuzji pokazującą dokładność klasyfikacji na danych testowych.
#    Użyjemy ConfusionMatrixDisplay do wizualizacji macierzy.
# 2. Wykonaj wizualizację danych na wykresie punktowym (scatter):
#    - Pierwszy wykres: rzeczywisty podział klas (prawdziwe etykiety) dla dwóch wybranych cech.
#    - Drugi wykres: podział klas według predykcji klasyfikatora (uzyskanych przez predict) dla tych samych cech.
#    Dla uproszczenia wybieramy pierwsze dwie cechy z danych.
# --------------------------------------------------------------
# Słownik, w którym przechowamy wytrenowane klasyfikatory dla każdego typu jądra
classifiers = {}

for kernel in ['linear', 'rbf']:
    # Trenowanie klasyfikatora z optymalnym parametrem C dla danego jądra
    clf = SVC(kernel=kernel, C=best_params[kernel])
    clf.fit(X_train, y_train)
    classifiers[kernel] = clf
    
    # Predykcje na zbiorze testowym
    y_pred = clf.predict(X_test)
    
    # 1. Tworzenie i wyświetlanie macierzy konfuzji
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=breast_cancer_data.target_names)
    disp.plot(cmap=plt.cm.Blues)
    plt.title(f"Macierz konfuzji dla SVC (kernel='{kernel}', C={best_params[kernel]})")
    plt.show()
    
    # 2. Wizualizacja danych na wykresach scatter
    # Wybieramy dwie pierwsze cechy do wizualizacji (np. 'mean radius' i 'mean texture')
    feature_idx = [0, 1]
    X_two = X[:, feature_idx]
    
    # Wykres z rzeczywistym podziałem klas (prawdziwe etykiety)
    plt.figure()
    plt.scatter(X_two[:, 0], X_two[:, 1], c=y, cmap='viridis', edgecolor='k', s=50)
    plt.xlabel(breast_cancer_data.feature_names[0])
    plt.ylabel(breast_cancer_data.feature_names[1])
    plt.title(f"Rzeczywisty podział klas - {kernel} kernel")
    plt.show()
    
    # Wykres z podziałem klas według predykcji klasyfikatora
    # Predykcje uzyskujemy dla całego zbioru (X) – choć klasyfikator został trenowany na pełnych danych,
    # do wizualizacji używamy tylko dwóch wybranych cech.
    y_pred_all = clf.predict(X)
    plt.figure()
    plt.scatter(X_two[:, 0], X_two[:, 1], c=y_pred_all, cmap='viridis', edgecolor='k', s=50)
    plt.xlabel(breast_cancer_data.feature_names[0])
    plt.ylabel(breast_cancer_data.feature_names[1])
    plt.title(f"Predykcje klasyfikatora (kernel='{kernel}', C={best_params[kernel]})")
    plt.show()
