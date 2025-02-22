from socket import *
import threading
# FUNCTIONS

def broadcast(messageToBoradcast):
    for client in listOfClient:
        client.send(messageToBoradcast.encode())

def getMessagesFromClients(connectionToClient, clientAddress):
    messageFromClient = ""
    while 1:
        try:
            messageFromClient = connectionToClient.recv(2048).decode()
        except:
            print("The client", clientAddress, " has disconnected.")
            listOfClient.remove(connectionToClient)
        if not messageFromClient:
            continue
        print("Broadcasting message from :", clientAddress)
        broadcast(messageFromClient)

def handleClients():
    while 1:
        connectionToClient, clientAddress = tcpServerSocket.accept()
        print("The client", clientAddress, " has connected.")
        listOfClient.append(connectionToClient)
        recieveMessagesThread = threading.Thread(target=getMessagesFromClients, args=(connectionToClient,clientAddress,))
        recieveMessagesThread.start()




# MAIN SERVER CODE
serverPort = 35433
tcpServerSocket = socket(AF_INET, SOCK_STREAM)
tcpServerSocket.bind(("", serverPort))
tcpServerSocket.listen(100)
listOfClient = []
print("The chat server has been initialized successfully.\n")
handleClients()

