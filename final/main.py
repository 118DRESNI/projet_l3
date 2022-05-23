import adcRead as adc
#import writeCsv as csv
import time
import tabShape as ts
import display as dp
import conversion as cv


#un fichier csv qui contient des données issues d'une acquisition
recPath = "rec.csv"

#declarations du vecteur contenant les mesures de l'ADC
CO2 	= 0
CO 	= 0
NTC	= 0
QEPAS	= 0
ADC 	= [CO2, CO, NTC, QEPAS]



#choix des channels à lire sur l'ADC:
EnCO2	= True
EnCO	= True
EnNTC	= True
EnQEPAS	= True

#choix d'un nombre d'echantillons a afficher
numligne = 20

#init du tableau
tab = ts.creerTab(numligne, ADC)



#declaration d'un compteur
indice = 0

#intialisation du graphe
graphe = dp.initGraph()

while(1):
	#lecture de l'ADC:
	ADC = adc.lireAdc(EnCO2, EnCO, EnNTC, EnQEPAS)
	CO2 	= ADC[0]
	CO 	= ADC[1]
	NTC  	= ADC[2]
	QEPAS	= ADC[3]
	
	#lecture du DHT (à éviter)
	#DHT = [69,420]
	
	#csv.newLine(tempPath, DHT, Gaz)
	
	#print("tension CO2 : " + str(CO2) + "V" + " | " + "tension CO : " + str(CO) + "V")
	#print("temps=",current_time)
	#print("temp={0:0.1f}*C  humidity={1:0.1f}%".format(temperature, humidity))
	
	tab, indice = ts.ajoutLigne(tab, numligne, ADC,indice)
	
	dp.affMes(tab, graphe)
	
	print (tab)
	time.sleep(0.1)

