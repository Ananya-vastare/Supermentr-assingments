#4th march

import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. Load/Create Dataset
# Replace 'your_data.csv' with your actual filename
try:
    df = pd.read_csv('loan_data.csv')
except FileNotFoundError:
    # Creating synthetic data for demonstration
    data = {
        'Income': np.random.randint(30000, 150000, 100),
        'Credit Score': np.random.randint(300, 850, 100),
        'Age': np.random.randint(21, 65, 100),
        'Loan Amount': np.random.randint(5000, 50000, 100),
        'Employment Years': np.random.randint(0, 40, 100),
        'Loan_Status': np.random.choice([0, 1], 100) # Target: 1 for Approved, 0 for Rejected
    }
    df = pd.DataFrame(data)

# Splitting Features and Target
X = df.drop('Loan_Status', axis=1)
y = df['Loan_Status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Train Decision Tree
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
dt_preds = dt_model.predict(X_test)

# 3. Train Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)

# 4. Compare Accuracy
dt_acc = accuracy_score(y_test, dt_preds)
rf_acc = accuracy_score(y_test, rf_preds)

print(f"--- Model Comparison ---")
print(f"Decision Tree Accuracy: {dt_acc:.2%}")
print(f"Random Forest Accuracy: {rf_acc:.2%}")

# 5. Show Feature Importance (Random Forest)
importances = rf_model.feature_importances_
feature_names = X.columns
indices = np.argsort(importances)

plt.figure(figsize=(10, 5))
plt.title('Feature Importances (Random Forest)')
plt.barh(range(len(indices)), importances[indices], align='center')
plt.yticks(range(len(indices)), [feature_names[i] for i in indices])
plt.xlabel('Relative Importance')
plt.show()

# 6. Save model using pickle
# We'll save the Random Forest model as it usually performs better
with open('loan_model.pkl', 'wb') as f:
    pickle.dump(rf_model, f)

print("\nModel saved as 'loan_model.pkl'")