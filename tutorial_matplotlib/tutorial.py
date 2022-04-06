import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('dark_background')

xMax = 10
dev = 5 
x_vals          = [i for i in range(xMax)]
print(len(x_vals))
print(x_vals)
y_vals = x_vals
y_vals_rand     = [random.randint(-dev,dev) for i in range(xMax)]
y_vals_square   = [i ** 2 for i in range(xMax)]

for i in range(xMax) :
    y_vals[i] = y_vals_square[i] +  i * y_vals_rand[i]

print(len(y_vals))
print(y_vals)

plt.plot(y_vals)
plt.show()