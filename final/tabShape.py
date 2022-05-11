import time
import numpy as np

taille = 12
numcol = 4
index = 0
DHT = [1, 2]
gaz = [3, 4]

def creerTab(numcol, taille):
    tab = np.zeros((taille, numcol), int)

    return tab

def ajoutLigne(tab, DHT,gaz,taille,index):
    if index < taille:
        tab[index] = [DHT[0], DHT[1], gaz[0], gaz[1]]
        index = index + 1
    else:
        index = 0
    return tab, index
tab = creerTab(numcol, taille)
print (tab)
while index < taille:
    tab = ajoutLigne(tab, DHT,gaz,taille,index)
    print (tab)
