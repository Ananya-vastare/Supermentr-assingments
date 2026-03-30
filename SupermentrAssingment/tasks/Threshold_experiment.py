#25th feb

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.datasets import make_classification

# 1. Generate a synthetic cancer dataset (1 = Malignant, 0 = Benign)
X, y = make_classification(n_samples=1000, n_features=5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Train Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)

# 3. Get predicted probabilities for the positive class (Cancer)
# [:, 1] gives the probability of being '1'
probabilities = model.predict_proba(X_test)[:, 1]

# 4. Run the experiment for different thresholds
thresholds = [0.3, 0.5, 0.7]
results = []

for t in thresholds:
    # If probability > threshold, classify as 1, else 0
    y_pred = (probabilities >= t).astype(int)
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    
    results.append({
        'Threshold': t,
        'Accuracy': round(acc, 3),
        'Precision': round(prec, 3),
        'Recall': round(rec, 3)
    })

# 5. Compare results in a table
df_results = pd.DataFrame(results)
print("--- Threshold Experiment Results ---")
print(df_results)