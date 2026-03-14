import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.connect((HOST_NAME, PORT))

message = "Hello Server"
s.send(message.encode())

reply = s.recv(1024)
print("Server says:", reply.decode())

s.close()