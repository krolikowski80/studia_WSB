# Raport z zadania laboratoryjnego
## Klasyfikacja danych breast_cancer za pomocą SVC

### 1. Wprowadzenie
Celem zadania było zbadanie klasyfikacji danych dotyczących raka piersi z wykorzystaniem klasyfikatora SVC (Support Vector Classifier) z biblioteki scikit-learn. W eksperymencie:
- Wczytano dane (zbór `breast_cancer`).
- Podzielono dane na zbiór uczący (70%) i testowy (30%).
- Wytrenowano klasyfikator SVC z domyślnymi parametrami.
- Obliczono dokładność klasyfikacji na zbiorze testowym.
- Przeanalizowano wpływ parametru C oraz rodzaju jądra (kernel) na działanie modelu.
- Wizualizowano wyniki przy pomocy macierzy konfuzji oraz wykresów scatter dla wybranych cech.

### 2. Wczytanie i eksploracja danych
Poniższy fragment kodu wczytuje zbór danych `breast_cancer` oraz wyświetla podstawowe informacje o nim.

```python
from sklearn import datasets  
breast_cancer_data = datasets.load_breast_cancer()

X = breast_cancer_data.data   
y = breast_cancer_data.target

print("Klucze dostępne w zbiorze:", breast_cancer_data.keys())
print("Rozmiar danych (próbki, cechy):", breast_cancer_data.data.shape)
print("Nazwy cech:", breast_cancer_data.feature_names)
print("Nazwy klas:", breast_cancer_data.target_names)
```

*Wyniki powyższego fragmentu kodu (np. wypis kluczy, kształt danych i nazwy cech) zostały dołączone jako zrzuty ekranu.*

### 3. Podział danych na zbior uczący i testowy

```python
from sklearn.model_selection import train_test_split

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
```

### 4. Trenowanie klasyfikatora SVC (domyślne parametry)

```python
from sklearn.svm import SVC
svc_clf = SVC()
svc_clf.fit(X_train, y_train)
print("\nModel SVC został wytrenowany na zbiorze uczącym.")
```

### 5. Obliczanie dokładności klasyfikacji

```python
from sklearn.metrics import accuracy_score
y_pred_default = svc_clf.predict(X_test)
accuracy_default = accuracy_score(y_test, y_pred_default)
print("Dokładność klasyfikacji dla domyślnego SVC:", accuracy_default)
```

### 6. Optymalizacja parametrów

```python
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
        if acc > best_accuracy:
            best_accuracy = acc
            best_C = C
    best_params[kernel] = best_C
    print(f"Najlepsze C dla jądra '{kernel}': {best_C} z dokładnością {best_accuracy:.4f}\n")
```

### 7. Wizualizacja wyników

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

for kernel in ['linear', 'rbf']:
    clf = SVC(kernel=kernel, C=best_params[kernel])
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=breast_cancer_data.target_names)
    disp.plot(cmap=plt.cm.Blues)
    plt.title(f"Macierz konfuzji dla SVC (kernel='{kernel}', C={best_params[kernel]})")
    plt.show()
```

### 8. Wnioski

- Optymalny parametr C dla `linear` i `rbf` został znaleziony poprzez testowanie kilku wartości.
- Jądro `rbf` okazało się lepsze dla naszego zbioru danych.
- Wizualizacja wykazała, że klasyfikator dobrze rozróżnia klasy, ale mogą pojawiać się błędy klasyfikacyjne.
- Macierz konfuzji pokazuje poprawnie sklasyfikowane przypadki oraz błędy modelu.

### 9. Dołączenie kodu Żródłowego

Do raportu załączony jest pełen kod w pliku `lab2_svc.py` oraz notebook Jupyter.

### 10. Generowanie PDF

Raport można wyeksportować do PDF poprzez opcję w Jupyter Notebook: `File -> Download as -> PDF via LaTeX` lub w Google Colab poprzez `File -> Print`.
```

