import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
      
def lireDHT22():
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	if humidity is not None and temperature is not None:
		temp = (temperature)
		humi = (humidity)
		temphumi = [temp,humi]
		return temphumi 
	else:
		print("Failed to retrieve data from humidity sensor")
		temphumi = [0,0]
		return temphumi 


