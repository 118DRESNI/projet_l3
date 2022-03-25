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

chan = AnalogIn(ads, ADS.P0, ADS.P1) #creation d'un canal differentiel  

#pour lire la tension -> chan.voltage
#pour lire la valeur  -> chan.value
#ajuster le gain pour precision max (0.256V pleine echelle) -> ads.gain = 16

#effectuer un mesure simple     -> ads.mode = Mode.SINGLE
#effectuer un mesure continue   -> ads.mode = Mode.CONTINUOUS

while 1:
    wait(3)
