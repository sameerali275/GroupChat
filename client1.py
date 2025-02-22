from socket import *
import threading

# Functions

def recieveMessages():
    while 1:
        messageFromServer = tcpClientSocket.recv(2048).decode()
        if messageFromServer:
            print(messageFromServer)
    return

def sendMessage():
    messageToSend = str(input())
    messageToSend = myAlias + ": " + messageToSend
    tcpClientSocket.send(messageToSend.encode())
    return


# Main Client Code
serverIP = "localhost"
serverPort = 35433
tcpClientSocket = socket(AF_INET, SOCK_STREAM)
try:
    tcpClientSocket.connect((serverIP, serverPort))
except ConnectionRefusedError:
    print("The server has refused connection.\n\n")
    quit()


myAlias = input("Choose an Alias: ")

recieveMessageThread = threading.Thread(target=recieveMessages)
recieveMessageThread.start()

while 1:
    sendMessage()