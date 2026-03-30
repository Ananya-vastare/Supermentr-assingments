import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset (Area vs Price)
X = np.array([[500], [1000], [1500], [2000], [2500]])
y = np.array([10000, 20000, 30000, 40000, 50000])

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction
new_area = np.array([[1800]])
predicted_price = model.predict(new_area)

print("Predicted Price:", predicted_price[0])