from pynput import keyboard


class KeyHandler():
	def __init__(self):
		self.pressed = list()
		self.keyset = ""
		self.isEnter = False
		self.isWorking = False

	def on_press(self, key):
		if key == keyboard.Key.esc:
			self.isWorking = False
			return False
		if key == keyboard.Key.enter:
			self.isWorking = False
			self.isEnter = True
			return False
		tmp = str(key).replace("'","")
		if tmp not in self.pressed:
			self.pressed.append(tmp)
		self.keyset = self.getKeySet()

	def on_release(self, key):
		tmp = str(key).replace("'","")
		if tmp in self.pressed:
			self.pressed.remove(tmp)

	def startListener(self):
		self.listener = keyboard.Listener(
			on_press=self.on_press,
			on_release=self.on_release)
		self.listener.start()

	def endListener(self):
		self.listener.stop()

	def getKeySet(self):
		keyset  = ""
		for key in self.pressed:
			if len(key) == 1:
				keyset += key.lower()
			elif len(key) > 2 and 'Key.' in key:
				keyset += '<'+key[4:].lower()+'>'
			if key != self.pressed[-1]:
				keyset += '+'
		return keyset
