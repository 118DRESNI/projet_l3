
import pandas as pd


x_vals = []
y_vals = []


index = 101

x_len = 100

x_cur   = 0
x_prev  = 0

data = pd.read_csv('data.csv')
x = data['x_value']
y1 = data['total_1']


# on encadre les valeurs en x du graphe
x_first = x[index]
if index - x_len < 0 :
    x_last = x[0]
else :
    x_last = x[index - x_len]
print(x_first)
print(x_last)

for k in range(x_last, x_first + 1):
    