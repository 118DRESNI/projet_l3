import adcRead as adc
import writeCsv as csv
import time

#un fichier csv temporaire qui contient un nombre fixe d'échantillons
tempPath = "test.csv"

#un autre fichier csv qui contient des données issues d'une acquisition
recPath = "rectest.csv"
gaz = []
CO2 = 0
CO = 0
temphumi=[]
temperature=0
humidite=0


#création d'un fichier de stockage temporaire des échantillons 
csv.create(tempPath)

while(1):
	Gaz = adc.lireAdc()
	CO2 = Gaz[0]
	CO = Gaz[1]
	
	DHT = [69,420]
	csv.newLine(tempPath,DHT, Gaz)
	
	print("tension CO2 : " + str(CO2) + "V" + " | " + "tension CO : " + str(CO) + "V"  )
	#print("temps=",current_time)
    #print("temp={0:0.1f}*C  humidity={1:0.1f}%".format(temperature, humidity))
    
    
	time.sleep(0.1)
while(2):
	temphumi = lireDHT22()
	temperature=temphumi[0]
	humidite=temphumi[1]
	csv.newLine(tempPath, temphumi)
	
	print("température : " + str(temperature) + "°" + " | " + "humidité: " + str(humidite) + "%"  )
	
