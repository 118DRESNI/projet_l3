#modules a installer:
# sudo pip install adafruit-circuitpython-ads1x15
# sudo pip install board

# activer le bus I2C dans les parametres de la raspi

from multiprocessing.connection import wait
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA) #initialisation du bus I2C

import adafruit_ads1x15.ads1115 as ADS #import du module ADS1115 -> renommer ADS 
from adafruit_ads1x15.analog_in import AnalogIn #import de la version ADS1115 de la fonction AnalogIn

ads = ADS.ADS1115(i2c) #creation de l'objet ADC

chanCO2     = AnalogIn(ads, ADS.P0) #creation d'un canal canal de lecture CO2
chanCO      = AnalogIn(ads, ADS.P1) #creation d'un canal canal de lecture CO
chanNTC     = AnalogIn(ads, ADS.P2) #creation d'un canal canal de lecture température thermistance
chanQEPAS   = AnalogIn(ads, ADS.P3) #creation d'un canal canal de lecture QEPAS

#pour lire la tension -> chan.voltage
#pour lire la valeur  -> chan.value
#ajuster le gain pour precision max (0.256V pleine echelle) -> ads.gain = 1
ads.gain = 1

#effectuer un mesure simple     -> ads.mode = Mode.SINGLE
#effectuer un mesure continue   -> ads.mode = Mode.CONTINUOUS

ADC = [0,0,0,0]

def lireAdc(EnCO2, EnCO, EnNTC, EnQEPAS):
    if EnCO2 == True: 
        CO2     =   round(chanCO2.voltage,  3)
    else:
        CO2     =   0
    if EnCO == True: 
        CO      =   round(chanCO.voltage,   3)
    else:
        CO     =   0    
    if EnNTC == True: 
        NTC     =   round(chanNTC.voltage,  3)
    else:
        NTC     =   0    
    if EnQEPAS == True: 
        QEPAS   =   round(chanQEPAS.voltage,3)
    else:
        QEPAS     =   0  
          
    ADC[0]  = CO2
    ADC[1]  = CO
    ADC[2]  = NTC
    ADC[3]  = QEPAS
    return ADC 


