import RPi.GPIO as GPIO
import time
from Server import Server

SENSOR1 = 29	#Send 1,2
SENSOR2 = 31	#Send 3,4
SENSOR3 = 33	#Send 5,6
SENSOR4 = 35	#Send 7,8

class Touch():

	def __init__(self):
		self.pushtime = [0,0,0,0]
		self.releasetime = [0,0,0,0]
		self.server = Server()
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup([SENSOR1,SENSOR2,SENSOR3,SENSOR4], GPIO.IN)
		self.add_events()

	def touch_callback(self, pinNum):
		index = int((pinNum-29)/2)
		if (GPIO.input(pinNum)):
			self.pushtime[index] = time.time()
		else:
			self.releasetime[index] = time.time()
			pressedtime = self.releasetime[index] - self.pushtime[index]
			if (0 < pressedtime < 0.4):
				self.server.send(str(pinNum-28))
			elif (pressedtime < 3):
				self.server.send(str(pinNum-27))

	def add_events(self):
		GPIO.add_event_detect(SENSOR1, GPIO.BOTH, callback = self.touch_callback)
		GPIO.add_event_detect(SENSOR2, GPIO.BOTH, callback = self.touch_callback)
		GPIO.add_event_detect(SENSOR3, GPIO.BOTH, callback = self.touch_callback)
		GPIO.add_event_detect(SENSOR4, GPIO.BOTH, callback = self.touch_callback)

	def __del__(self):
		GPIO.cleanup()
