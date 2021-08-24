import Adafruit_DHT
while(True):
	h,t=Adafruit_DHT.read_retry(11,21)
	print("Temp is: ",t)
	print("Humidity is: ",h)
