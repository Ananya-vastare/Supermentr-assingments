#13th feb
import numpy as np

# 1. Create a list of temperatures
temp_list = [28, 32, 30, 37, 36, 38]

# 2. Convert the list into a numpy array
temp_array = np.array(temp_list)

# 3. Print maximum and minimum temp
max_temp = np.max(temp_array)
min_temp = np.min(temp_array)

print(f"Maximum Temperature: {max_temp}°C")
print(f"Minimum Temperature: {min_temp}°C")

# 4. Calculate average temp
# We use .mean() for average
avg_temp = np.mean(temp_array)
print(f"Average Temperature: {avg_temp:.2f}°C")

# 5. Display last 3 days temp
# Using slicing [-3:] starts from the 3rd element from the end to the very end
last_three_days = temp_array[-3:]
print(f"Last 3 days temperatures: {last_three_days}")