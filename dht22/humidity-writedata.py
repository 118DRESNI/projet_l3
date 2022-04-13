import Adafruit_DHT
import csv
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
x_value = 0
#nom des colonnes
fieldnames = ["temps", "temperature", "humidite"]


#ouvrir le fichier csv pour append les nouvelles valeurs
def ecrireLigne(humidity, temperature, x_value):
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        info = {
            "temps": x_value,
            "temperature": temperature,
            "humidite": humidity
        }
        csv_writer.writerow(info)
 
#creer un fichier csv sil nexiste pas et l'ouvrir pour ecrire les fieldnames
with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensor") 

    ecrireLigne(humidity, temperature, x_value)

    x_value += 1 
    
    time.sleep(100)
