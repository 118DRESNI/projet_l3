import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
      
def lireDHT22():
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	if humidity is not None and temperature is not None:
		Temp = (temperature)
		Humi = (humidity)
		TempHumi = [Temp,Humi]
		return TempHumi
	else:
		print("Failed to retrieve data from humidity sensor")
		TempHumi = [0,0]
		return TempHumi


