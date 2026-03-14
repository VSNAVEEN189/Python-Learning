import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))

s.listen(4)

print("Server started... Waiting for connection")

while True:
    # print("Waiting...")
    client, address = s.accept()
    print("Connected with:", address)

    msg = client.recv(1024)
    print("Client says:", msg.decode())

    client.send("Message received".encode())

    client.close()