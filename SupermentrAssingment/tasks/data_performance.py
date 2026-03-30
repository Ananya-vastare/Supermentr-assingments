#16th feb

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# 1. Create the messy dataset
data = {
    'age': [25, 30, np.nan, 35, 40, 30],
    'salary': [50000, 60000, 55000, np.nan, 80000, 60000],
    'city': ['hyderabad', 'HYDERABAD', 'Hyderabad', 'Bangalore', 'bangalore', 'HYDERABAD'],
    'experience': [2, 5, 3, 8, 10, 5]  # Row 1 and 5 (index 1 & 5) are duplicates
}

df = pd.DataFrame(data)
print("--- Original Messy Data ---")
print(df)

# 2. Remove duplicates
# Keep the first occurrence and drop the rest
df = df.drop_duplicates().reset_index(drop=True)

# 3. Handle missing values
# Common practice: Fill Age with Mean and Salary with Median
df['age'] = df['age'].fillna(df['age'].mean())
df['salary'] = df['salary'].fillna(df['salary'].median())

# 4. Standardize city names
# Converting all to Title Case (e.g., 'Hyderabad') so they are categorized correctly
df['city'] = df['city'].str.title()

# 5. Apply MinMax Scaling on age and salary
# This scales values to a range between 0 and 1
scaler = MinMaxScaler()
df[['age', 'salary']] = scaler.fit_transform(df[['age', 'salary']])

# 6. Show final cleaned data
print("\n--- Final Cleaned & Scaled Data ---")
print(df)