#25th feb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score

# --- TASK 1: BASIC PROGRAMMING ---
def basic_tasks():
    # Odd/Even Check
    num = 7
    print(f"{num} is {'Even' if num % 2 == 0 else 'Odd'}")
    
    # Numbers 10 to 1
    print("Countdown:", [i for i in range(10, 0, -1)])

# --- TASK 2: NUMPY TEMPERATURE ANALYSIS ---
def numpy_task():
    temp_list = [28, 32, 30, 37, 36, 38]
    temp_array = np.array(temp_list)
    
    print(f"\nMax Temp: {np.max(temp_array)}°C")
    print(f"Avg Temp: {np.mean(temp_array):.2f}°C")
    print(f"Last 3 Days: {temp_array[-3:]}")

# --- TASK 3: PANDAS STUDENT ANALYSIS ---
def pandas_task():
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'maths': [85, 70, 95, np.nan],
        'science': [90, 80, 85, 75],
        'english': [78, 82, 88, 80],
        'dept': ['CS', 'EC', 'CS', 'EC']
    }
    df = pd.DataFrame(data)
    
    # Handle missing values & calculations
    df['maths'] = df['maths'].fillna(df['maths'].mean())
    df['total'] = df[['maths', 'science', 'english']].sum(axis=1)
    df['average'] = df[['maths', 'science', 'english']].mean(axis=1)
    
    print("\n--- Student Top 3 ---")
    print(df.sort_values(by='total', ascending=False).head(3))

# --- TASK 4: DATA CLEANING & SCALING ---
def cleaning_task():
    data = {
        'age': [25, 30, np.nan, 35, 30],
        'salary': [50000, 60000, 55000, np.nan, 60000],
        'city': ['hyderabad', 'HYDERABAD', 'Hyderabad', 'Bangalore', 'HYDERABAD']
    }
    df = pd.DataFrame(data)
    
    # Processing
    df = df.drop_duplicates()
    df['city'] = df['city'].str.title()
    df['age'] = df['age'].fillna(df['age'].mean())
    df['salary'] = df['salary'].fillna(df['salary'].median())
    
    scaler = MinMaxScaler()
    df[['age', 'salary']] = scaler.fit_transform(df[['age', 'salary']])
    
    print("\n--- Cleaned & Scaled Data ---")
    print(df)

# --- TASK 5: THRESHOLD EXPERIMENT (CANCER DETECTION) ---
def threshold_experiment():
    # Simulating model probabilities and actual outcomes
    y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    y_probs = [0.85, 0.1, 0.4, 0.75, 0.2, 0.35, 0.6, 0.05, 0.9, 0.45]
    
    thresholds = [0.3, 0.5, 0.7]
    print("\n--- Threshold Experiment ---")
    for t in thresholds:
        y_pred = [1 if p >= t else 0 for p in y_probs]
        print(f"Threshold {t} | Acc: {accuracy_score(y_true, y_pred)} | "
              f"Prec: {precision_score(y_true, y_pred):.2f} | "
              f"Recall: {recall_score(y_true, y_pred):.2f}")

# Execute all
basic_tasks()
numpy_task()
pandas_task()
cleaning_task()
threshold_experiment()