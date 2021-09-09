import socket

#IP = '192.168.137.128'
IP = '127.0.0.1'
PORT = 9999

class Server():
	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		try:
			self.socket.bind((IP, PORT))
		except socket.error:
			print ('Bind failed')
		self.socket.listen()
		print('Socket awaiting messages')
		self.conn, self.addr = self.socket.accept()
		print('Connected')

	def send(self, msg):
		try:
				self.conn.send(msg.encode())
				print('Send message: {}'.format(msg))
		except:
				print('Send Error')
