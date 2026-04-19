import numpy as np
import matplotlib.pyplot as plt

# Quick test for NumPy
arr = np.array([1, 2, 3, 4, 5])
print("NumPy array:", arr)
print("Mean:", np.mean(arr))

# Quick test for Matplotlib
plt.plot(arr, arr**2)   # x vs x^2
plt.title("Test Graph")
plt.xlabel("x values")
plt.ylabel("x squared")
plt.show()
