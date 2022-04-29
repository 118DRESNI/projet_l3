import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

ads = ADS.ADS1115(i2c)

chan = AnalogIn(ads, ADS.P0, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2, ADS.P3)

import time
arrays = []

t_end = time.time() + 1
while time.time() < t_end:
   arrays.append((chan.value, chan.voltage))

for x in arrays:
   print(x)


print(len(arrays))
