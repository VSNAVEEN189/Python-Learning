import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #For communication

HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))

s.listen(4)
client, address = s.accept()
while True:
    message = input('Server:')                        #Receiving message from server to client
    client.send(bytes(message, "utf-8"))
    message_from_client = client.recv(50)        
    print("Client"+ message_from_client.decode('utf-8'))
    #Receiving message from client to server

# This chat application is a single threaded application, This means action of receiving or sending messages from the client happens one at a time , Making sure server run first.