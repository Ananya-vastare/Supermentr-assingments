#15 feb

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# 1. Create the messy dataset
data = {
    'age': [25, 30, np.nan, 35, 40, 30],
    'salary': [50000, 60000, 55000, np.nan, 80000, 60000],
    'city': ['hyderabad', 'HYDERABAD', 'Hyderabad', 'Bangalore', 'bangalore', 'HYDERABAD'],
    'experience': [2, 5, 3, 8, 10, 5]  # Row 1 and 5 are duplicates
}

df = pd.DataFrame(data)
print("--- Original Messy Data ---")
print(df)

# 2. Remove duplicates
df = df.drop_duplicates().reset_index(drop=True)

# 3. Handle missing values
# Filling Age with Mean and Salary with Median
df['age'] = df['age'].fillna(df['age'].mean())
df['salary'] = df['salary'].fillna(df['salary'].median())

# 4. Standardize city names
# Convert all to Title Case (e.g., 'Hyderabad')
df['city'] = df['city'].str.title()

# 5. Apply MinMax Scaling on age and salary
# MinMax Scaling formula: (x - min) / (max - min)
scaler = MinMaxScaler()
df[['age', 'salary']] = scaler.fit_transform(df[['age', 'salary']])

# 6. Show final cleaned data
print("\n--- Final Cleaned & Scaled Data ---")
print(df)