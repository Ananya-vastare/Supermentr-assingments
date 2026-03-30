import time
import numpy as np

# Python list
start = time.time()
lst = [i*2 for i in range(1000000)]
print("List Time:", time.time() - start)

# NumPy array
start = time.time()
arr = np.arange(1000000) * 2
print("NumPy Time:", time.time() - start)