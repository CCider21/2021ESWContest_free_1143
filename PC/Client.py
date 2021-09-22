import socket
import threading
from pynput import keyboard
from UI import UI
from DB import DB

IP = '192.168.137.128'
PORT = 9999

class Client(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.setDaemon(True)
		self.socket = None
		self.connect()

	def run(self):
		self.recieve()

	def connect(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.socket.connect((IP,PORT))
			print('Client has connected')
		except:
			print('Connect fail')

	def recieve(self):
		while True:
			try:
				d = self.socket.recv(1024)
				data = d.decode()
				if data is not "":
					db = DB(UI.curdb)
					key = db.getkey(int(data)-1)
					self.pressKeySet(key)
			except socket.error:
				self.connect()

	def pressKeySet(keyset):
		parsed = keyboard.HotKey.parse(keyset)
		kbcontrol = keyboard.Controller()

		def loop(i):
			if parsed[i] is not parsed[-1]:
				with kbcontrol.pressed(parsed[i]):
					loop(i+1)
			else:
				kbcontrol.press(parsed[-1])
				kbcontrol.release(parsed[-1])
		loop(0)


