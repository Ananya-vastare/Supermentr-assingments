#27th feb

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. Load Dataset
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# 2. Split into train-test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Try different K values and Distance Metrics
k_values = range(1, 16)
euclidean_acc = []
manhattan_acc = []

for k in k_values:
    # Euclidean Distance (p=2)
    knn_e = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    knn_e.fit(X_train, y_train)
    euclidean_acc.append(accuracy_score(y_test, knn_e.predict(X_test)))
    
    # Manhattan Distance (p=1)
    knn_m = KNeighborsClassifier(n_neighbors=k, metric='manhattan')
    knn_m.fit(X_train, y_train)
    manhattan_acc.append(accuracy_score(y_test, knn_m.predict(X_test)))

# 4. Plot Accuracy vs K
plt.figure(figsize=(10, 6))
plt.plot(k_values, euclidean_acc, marker='o', label='Euclidean')
plt.plot(k_values, manhattan_acc, marker='s', label='Manhattan')
plt.title('KNN: Accuracy vs K Value')
plt.xlabel('Number of Neighbors (K)')
plt.ylabel('Test Accuracy')
plt.xticks(k_values)
plt.legend()
plt.grid(True)
plt.show()

# Compare Results
best_k_e = k_values[euclidean_acc.index(max(euclidean_acc))]
print(f"Best Accuracy (Euclidean): {max(euclidean_acc):.4f} at K={best_k_e}")
print(f"Best Accuracy (Manhattan): {max(manhattan_acc):.4f} at K={k_values[manhattan_acc.index(max(manhattan_acc))]}")