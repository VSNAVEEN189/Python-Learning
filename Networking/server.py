import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #For communication

HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))

s.listen(4)

while True:
    client, address = s.accept()
    client.send(bytes("Hey there, whats up? I am learning to code, I am feeling good", "utf-8"))
    print(address)
    client.close()