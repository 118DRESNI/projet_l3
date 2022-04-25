import pandas as pd
import matplotlib.pyplot as plt

# rappel sur les fieldnames : 
# fieldnames = ["temps", "temperature", "humidite", "CO2", "CO"]

tempPath = "data.csv"

def afficher (tempPath):
    
    plt.style.use('dark_background')

    data = pd.read_csv(tempPath)
    x = data['temps']
    temp = data['temperature']
    humid = data['humidite']
    co2 = data['CO2']
    co = data['CO']

    plt.cla() #effacement du plot

    plt.plot(x, temp,'r', label='temperature')
    plt.plot(x, humid,'g', label='humidité')
    plt.plot(x, co2,'b', label='co2')
    plt.plot(x, co,'m', label='co')

    plt.legend(loc='upper left')
    plt.tight_layout()

    plt.tight_layout()
    plt.grid(True)
    plt.show()


afficher(tempPath)