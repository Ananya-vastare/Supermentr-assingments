#14th feb

import pandas as pd
import numpy as np

# --- STEP 0: Creating a dummy CSV for demonstration ---
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'maths': [85, 70, 95, np.nan, 88, 60],
    'science': [90, 80, 85, 75, 92, 65],
    'english': [78, 82, 88, 80, 95, 70],
    'dept': ['CS', 'EC', 'CS', 'EC', 'CS', 'EC']
}
df_dummy = pd.DataFrame(data)
df_dummy.to_csv('students.csv', index=False)

df = pd.read_csv('students.csv')

# --- STEP 2: Handle missing values ---
# We'll fill missing marks with the mean of that column
df['maths'] = df['maths'].fillna(df['maths'].mean())

# --- STEP 3: Add new columns 'total' and 'average' ---
subjects = ['maths', 'science', 'english']
df['total'] = df[subjects].sum(axis=1)
df['average'] = df[subjects].mean(axis=1)

# --- STEP 4: Find top 3 students based on total ---
top_3 = df.sort_values(by='total', ascending=False).head(3)

# --- STEP 5: Dept wise average marks ---
# This calculates the average of all numeric columns per department
dept_avg = df.groupby('dept')[subjects].mean()

# --- STEP 6: Students scoring above 75 in ALL subjects ---
high_achievers = df[(df['maths'] > 75) & (df['science'] > 75) & (df['english'] > 75)]

# --- Printing Results ---
print("--- Processed Data ---")
print(df)
print("\n--- Top 3 Students ---")
print(top_3[['name', 'total']])
print("\n--- Department Wise Average ---")
print(dept_avg)
print("\n--- Students with >75 in all subjects ---")
print(high_achievers['name'].tolist())