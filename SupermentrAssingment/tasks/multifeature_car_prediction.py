#23rd feb

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Create a sample dataset
data = {
    'Year': [2015, 2017, 2018, 2020, 2016, 2019, 2021, 2014],
    'Horsepower': [120, 150, 170, 200, 140, 180, 250, 110],
    'Mileage': [50000, 35000, 30000, 15000, 45000, 20000, 5000, 60000],
    'Price': [12000, 18000, 22000, 30000, 15000, 25000, 40000, 10000]
}
df = pd.DataFrame(data)

# 2. Define Features (X) and Target (y)
X = df[['Year', 'Horsepower', 'Mileage']]
y = df['Price']

# 3. Split the data into Training and Testing sets (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize and Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Make Predictions
y_pred = model.predict(X_test)

# 6. Evaluate the Model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model Accuracy (R2 Score): {r2:.4f}")
print(f"Mean Squared Error: {mse:.2f}")

# 7. Predict for a specific new car
# [Year: 2022, Horsepower: 300, Mileage: 2000]
new_car = np.array([[2022, 300, 2000]])
predicted_price = model.predict(new_car)
print(f"\nPredicted price for a 2022 car with 300HP: ${predicted_price[0]:,.2f}")