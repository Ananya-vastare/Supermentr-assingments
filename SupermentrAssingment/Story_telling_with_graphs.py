import matplotlib.pyplot as plt

data = [10, 20, 30, 40]

# Bar Chart
plt.bar(['A','B','C','D'], data)
plt.title("Bar Chart")
plt.show()

# Pie Chart
plt.pie(data, labels=['A','B','C','D'], autopct='%1.1f%%')
plt.show()

# Histogram
plt.hist(data)
plt.show()