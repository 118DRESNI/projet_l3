# Conversion de la résistance mesurée  en une température
# thermistance NTCLE100E3102JB0 de Vishay
# datasheet : https://docs.rs-online.com/a8e8/0900766b8162bf79.pdf

import math as m 

# 2 set de constantes selon si la température est inférieure ou supérieure à 25°C:

#inférieur à 25°C
A1Inf25 = 3.354e-3
B1Inf25 = 2.909e-4
C1Inf25 = 1.632e-6
D1Inf25 = 7.192e-8

#supérieur à 25°C
A1Sup25 = 3.354e-3
B1Sup25 = 2.934e-4
C1Sup25 = 3.494e-6
D1Sup25 = -7.713e-7

#résistance théorique à 25°C
r25 = 1000

def convNTC (rMes):

    rRatio = m.log(rMes / r25)
    invNTCtemp = A1Inf25 + (B1Inf25 * rRatio) + (C1Inf25 * rRatio * rRatio) + (D1Inf25 * rRatio * rRatio * rRatio)

    NTCtempK = 1 / invNTCtemp
    NTCtempC = NTCtempK - 273.15
    print("(1)" + str(NTCtempC) + "°C")
    #si on trouve une température supérieure à 25°C alors on refait le calcul avec le set de parametres correspondant.
    if NTCtempC >= 25:
        invNTCtemp = A1Sup25 + (B1Sup25 * rRatio) + (C1Sup25 * rRatio * rRatio) + (D1Sup25 * rRatio * rRatio * rRatio)
        NTCtempK = 1 / invNTCtemp
        NTCtempC = NTCtempK - 273.15
        print("(2)" + str(NTCtempC) + "°C")

    NTCtemp = [NTCtempC, NTCtempK]
    return NTCtemp


test = convNTC(160)