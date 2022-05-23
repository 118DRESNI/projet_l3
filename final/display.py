import numpy as np
import matplotlib.pyplot as plt

#	CO2 	= ADC[0]
#	CO 	    = ADC[1]
#	NTC  	= ADC[2]
#	QEPAS	= ADC[3]

def initGraph():
    fig = plt.figure()
    return fig


def affMes(ADC, fig):
    
    fig.clear()
    
    CO2 	= ADC[0]
    CO 	    = ADC[1]
    NTC  	= ADC[2]
    QEPAS	= ADC[3]
    
    taille = len(CO2)
    
    AxeX = np.linspace(0, taille-1, taille)
    
    plt.plot(AxeX, CO2)
    plt.draw()
    plt.grid(True)
