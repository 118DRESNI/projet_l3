import adcReado as adc
import writeCsvo as csv
import dhtReado as dht
import time

#un fichier csv temporaire qui contient un nombre fixe d'échantillons
tempPath = "test.csv"

#un autre fichier csv qui contient des données issues d'une acquisition
recPath = "rectest.csv"
gaz = []
CO2 = 0
CO = 0
TempHumi=[]
Temp = 0		
Humi = 0


#création d'un fichier de stockage temporaire des échantillons 
csv.create(tempPath)

while(1):
	Gaz = adc.lireAdc()
	CO2 = Gaz[0]
	CO = Gaz[1]
	TempHumi = dht.lireDHT22()
	Temp=TempHumi[0]
	Humi=TempHumi[1]
	
	csv.newLine(tempPath,TempHumi ,Gaz)
	
	print("tension CO2 : " + str(CO2) + "V" + " | " + "tension CO : " + str(CO) + "V" + " | " + "temperature:" + str(Temp) + "°" + " | " + " humidité" + str(Humi) + " % ")
	#print("temps=",current_time)
    #print("temp={0:0.1f}*C  humidity={1:0.1f}%".format(temperature, humidity))
    
    

	time.sleep(0.1) 
