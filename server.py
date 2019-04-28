import socket
import catfeeder

class CatFeederServer(object):
	'''
	Janky server for grabbing a feed message from a tcp socket.
	SSH didn't work with docker containers so next best thing was spin up a remote server
	then connect to it from my appdaemon automation to say "feed the fuckin cats"
	Probably overkill but it does the job. Running as a systemd service is even better
	'''
	def __init__(self, host="127.0.0.1", port=9999):
		self.host = host
		self.port = port
		self.sock = None

	# ------------------------------------------------------
	def open(method):
		def create_socket(self, *args, **kwargs):
			if not self.sock:
				self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				self.sock.bind((self.host, self.port))
				self.sock.listen(1)
			return method(self, *args, **kwargs)
		return create_socket

	# ------------------------------------------------------
	@open
	def run(self):
		while True:
			self.attempt_connection()

	# -----------------------------------------------------
	def attempt_connection(self):
		connection, client_address = self.sock.accept()
		try:
			print('connection from', client_address)
			while True:
				data = connection.recv(1024)
				if data:
					if "feed" in str(data):
						CatFeeder.feed()
					print ("Data: %s" % data)
				else:
					print ("no more data.")
					break
		finally:
			connection.close()

server = CatFeederServer("192.168.1.175")
server.run()
