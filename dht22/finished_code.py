
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('dark_background')

x_vals = []
y_vals = []

x_len   = 100 # combien de valeurs je veux sur le graphe a un temps donné
x_first = 0 # la valeur en x du début
x_last  = 0 # valeur en x de fin

x_encadre   = []
y1_encadre  = []
y2_encadre  = []

index = count()
    

def animate(index):
    data = pd.read_csv('data.csv')
    x = data['temps']
    y1 = data['temperature']
    y2 = data['humidite']

    if index < len(x) :
        # on encadre les valeurs en x du graphe
        x_first = x[index]
        if index - x_len < 0 :
            x_last = x[0]
        else :
            x_last = x[index - x_len]

        x_encadre   = x[x_last : x_first]
        y1_encadre  = y1[x_last : x_first]
        y2_encadre  = y1[x_last : x_first]
    else :
        x_encadre   = x[x_last : x_first]
        y1_encadre  = y1[x_last : x_first]
        y2_encadre  = y1[x_last : x_first]

    plt.cla() #effacement du plot

    plt.plot(x_encadre, y1_encadre,'r', label='Channel 1')
    plt.plot(x_encadre, y2_encadre,'b', label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=500)


plt.tight_layout()
plt.grid(True)
plt.show()
