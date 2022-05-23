import time
import numpy as np



#donnees = [0,1,2,3,4]
#numligne = 10
#indice = 0

#ctr = 0

def creerTab(numligne, donnees):
    numcol = len(donnees)
    tab = np.zeros((numligne, numcol))
    return tab

def ajoutLigne(tab, numligne, donnees,indice):
    if indice < numligne:
        tab[indice] = donnees
        indice = indice + 1
    else:
        tab = np.roll(tab, -1, axis = 0)
        tab[numligne - 1] = donnees
    return tab, indice

# test
#tab = creerTab(numligne, donnees)
#print (tab)

#while 1:
#    tab, indice = ajoutLigne(tab, numligne, donnees,indice)
#    print (tab)
#    print (indice)
#    print (ctr)
#    donnees = np.roll(donnees,1)
#    
#    if ctr == 20:
#        donnees = [5,6,7,8,9]
#    
#    ctr = ctr + 1
#     
#    time.sleep(1)
    
