#21 feb 

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Create dataset manually
data = {
    'Hours_Studied': [2, 5, 8, 1, 4, 7, 3, 9, 6, 2],
    'Sleep_Hours': [7, 8, 6, 5, 7, 7, 8, 5, 6, 7],
    'Previous_Score': [60, 80, 85, 40, 70, 90, 65, 95, 75, 55],
    'Final_Score': [65, 82, 90, 45, 72, 95, 68, 98, 80, 58]
}

df = pd.DataFrame(data)

# 2. Identify feature & label
# Features (X) are the inputs; Label (y) is what we want to predict
X = df[['Hours_Studied', 'Sleep_Hours', 'Previous_Score']]
y = df['Final_Score']

# 3. Split into train-test (70-30)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# 4. Train Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Make predictions and print metrics
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared Score (R2): {r2:.4f}")

# 6. Comment on model performance
if r2 > 0.8:
    print("\nConclusion: The model is GOOD. A high R2 indicates it explains most of the variance.")
elif r2 > 0.5:
    print("\nConclusion: The model is DECENT. It has some predictive power but could be improved.")
else:
    print("\nConclusion: The model is BAD. It is not capturing the relationship between features effectively.")