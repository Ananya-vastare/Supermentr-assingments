#18th feb
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Create your own dataset
data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'revenue': [2000, 2500, 2300, 3100, 3800, 3600, 4500, 4800, 5200, 5500, 6100, 7000],
    'marketing_spend': [300, 450, 400, 550, 700, 680, 850, 900, 1000, 1100, 1250, 1500],
    'profit': [500, 650, 600, 800, 1100, 1000, 1300, 1400, 1550, 1700, 1900, 2300]
}

df = pd.DataFrame(data)
sns.set_theme(style="darkgrid") # Sets a clean, professional aesthetic

# 2. Task: Create Line Plot for Revenue Trend
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='month', y='revenue', marker='o', color='teal', linewidth=2)
plt.title('Monthly Revenue Growth Trend', fontsize=14)
plt.ylabel('Revenue ($)')
plt.show()

# 3. Task: Create Scatter Plot between Marketing and Profit
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x='marketing_spend', y='profit', s=100, color='orange')
plt.title('Correlation: Marketing Spend vs Net Profit', fontsize=14)
plt.xlabel('Marketing Spend ($)')
plt.ylabel('Profit ($)')
plt.show()

# 4. Task: Create Correlation Map (Heatmap)
plt.figure(figsize=(8, 6))
# Calculate correlation matrix for numeric columns
corr_matrix = df[['revenue', 'marketing_spend', 'profit']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Feature Correlation Map', fontsize=14)
plt.show()