import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap

# Tworzenie katalogu wyniki/
os.makedirs('wyniki', exist_ok=True)

# Wczytanie danych Iris
iris = load_iris()
X, y = iris.data, iris.target

# Podział na zbiory
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# Szukanie najlepszego N
accuracy_scores = []
for n in range(1, 21):
    knn = KNeighborsClassifier(n_neighbors=n)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracy_scores.append({'N': n, 'Accuracy': acc})

# Zapisywanie wyników accuracy
df_accuracy = pd.DataFrame(accuracy_scores)
df_accuracy.to_excel('wyniki/accuracy_scores.xlsx', index=False)

# Wykres Accuracy vs N
plt.plot(df_accuracy['N'], df_accuracy['Accuracy'], marker='o')
plt.title('Accuracy vs Liczba sąsiadów')
plt.xlabel('Liczba sąsiadów (N)')
plt.ylabel('Accuracy')
plt.grid()
plt.savefig('wyniki/accuracy_vs_n.png')
plt.close()

# Najlepsze N
best_n = df_accuracy.loc[df_accuracy['Accuracy'].idxmax(), 'N']

# Zapis best_n do pliku txt
with open('wyniki/best_n.txt', 'w') as f:
    f.write(f'Najlepsza liczba sąsiadów to: {int(best_n)}\n')

# Finalny model
knn_final = KNeighborsClassifier(n_neighbors=int(best_n))
knn_final.fit(X_train, y_train)
y_pred_final = knn_final.predict(X_test)

# Macierz konfuzji
cm = confusion_matrix(y_test, y_pred_final)
df_cm = pd.DataFrame(cm, index=iris.target_names, columns=iris.target_names)
df_cm.to_excel('wyniki/confusion_matrix.xlsx')

plt.matshow(cm, cmap=plt.cm.Blues)
plt.title('Macierz konfuzji')
plt.colorbar()
plt.savefig('wyniki/confusion_matrix.png')
plt.close()

# Wykres 2D - rzeczywiste klasy
plt.scatter(X_test[:, 0], X_test[:, 1],
            c=y_test, cmap='viridis', edgecolor='k')
plt.title("Rzeczywisty podział klas")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.savefig('wyniki/scatter_real.png')
plt.close()

# Wykres 2D - predykcje
plt.scatter(X_test[:, 0], X_test[:, 1],
            c=y_pred_final, cmap='viridis', edgecolor='k')
plt.title("Predykcja modelu KNN")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.savefig('wyniki/scatter_predicted.png')
plt.close()

# Wykres 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_test[:, 0], X_test[:, 1], X_test[:, 2],
           c=y_test, cmap='viridis', edgecolor='k')
ax.set_title("Wizualizacja 3D - rzeczywiste klasy")
ax.set_xlabel(iris.feature_names[0])
ax.set_ylabel(iris.feature_names[1])
ax.set_zlabel(iris.feature_names[2])
plt.savefig('wyniki/scatter3d_real.png')
plt.close()

# Granica decyzyjna
X_vis = X[:, :2]
X_train_vis, X_test_vis, y_train_vis, y_test_vis = train_test_split(
    X_vis, y, test_size=0.3, random_state=42)

knn_vis = KNeighborsClassifier(n_neighbors=int(best_n))
knn_vis.fit(X_train_vis, y_train_vis)

x_min, x_max = X_vis[:, 0].min() - 1, X_vis[:, 0].max() + 1
y_min, y_max = X_vis[:, 1].min() - 1, X_vis[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

Z = knn_vis.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.4, cmap='viridis')
plt.scatter(X_vis[:, 0], X_vis[:, 1], c=y, edgecolor='k', cmap='viridis')
plt.title(f"Granica decyzyjna dla N={int(best_n)}")
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.savefig('wyniki/decision_boundary.png')
plt.close()