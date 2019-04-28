import socket
'''
Simple test script for verifying connection to server
'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_hostname = socket.gethostname()
ip_address = socket.gethostbyname(local_hostname)

server_address = ("127.0.0.1", 9999)
sock.connect(server_address)
sock.sendall(b"feed the cats")
sock.close()

