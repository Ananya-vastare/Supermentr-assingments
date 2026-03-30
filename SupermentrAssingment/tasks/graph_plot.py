#18th feb
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Create a sample dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Revenue': [100, 120, 110, 150, 170, 160, 200, 210, 230, 250, 280, 300],
    'Marketing_Spend': [20, 25, 22, 30, 35, 33, 40, 42, 45, 50, 55, 60],
    'Profit': [30, 35, 32, 45, 50, 48, 60, 62, 70, 75, 85, 90]
}
df = pd.DataFrame(data)

# Set the visual style
sns.set_theme(style="whitegrid")

# Task 1: Create a line plot for revenue trend
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Month', y='Revenue', marker='o', color='royalblue', linewidth=2.5)
plt.title('Monthly Revenue Trend', fontsize=14)
plt.ylabel('Revenue (in $1000s)')
plt.savefig('revenue_trend.png')  # Save the plot
plt.show()

# Task 2: Create a scatterplot between marketing and profit
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x='Marketing_Spend', y='Profit', s=100, color='crimson')
plt.title('Impact of Marketing Spend on Profit', fontsize=14)
plt.xlabel('Marketing Expenditure')
plt.ylabel('Net Profit')
plt.savefig('marketing_vs_profit.png')
plt.show()

# Task 3: Create a co-relational map (Heatmap)
plt.figure(figsize=(8, 6))
# Calculate correlation only for numeric columns
corr_matrix = df[['Revenue', 'Marketing_Spend', 'Profit']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu', fmt=".2f")
plt.title('Feature Correlation Heatmap', fontsize=14)
plt.savefig('correlation_heatmap.png')
plt.show()