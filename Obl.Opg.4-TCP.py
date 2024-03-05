from socket import *
import threading
import random


def handleClient(connectionSocket, address):
    print(address)
    while True:
        sentence = connectionSocket.recv(1024).decode()

        print(sentence)
        # connectionSocket.send((str(length) + capitalizedSentence).encode())


        if sentence.strip().lower() == 'close':
            connectionSocket.send("Connection Closed".encode())
            connectionSocket.close()

        # Første protokol
        if sentence.strip().lower() == 'random':
            connectionSocket.send("Input numbers \n".encode())
            numbers = connectionSocket.recv(1024).decode().strip()
            num1, num2 = map(int, numbers.split())
            print(f"Received numbers: {num1}, {num2}")
            random_number = random.randint(num1, num2)
            connectionSocket.send(f"{random_number}\n".encode())

        if sentence.strip().lower() == 'add':
            connectionSocket.send("Input numbers \n".encode())
            numbers = connectionSocket.recv(1024).decode()
            num1, num2 = map(int, numbers.split())
            print(f"Received numbers: {num1}, {num2}")
            result = num1 + num2
            connectionSocket.send(f"{result}\n".encode())

        if sentence.strip().lower() == 'subtract':
            connectionSocket.send("Input numbers \n".encode())
            numbers = connectionSocket.recv(1024).decode()
            num1, num2 = map(int, numbers.split())
            print(f"Received numbers: {num1}, {num2}")
            result = num1 - num2
            connectionSocket.send(f"{result}\n".encode())
            print(f"Sent result: {result}")
            

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target = handleClient,args = (connectionSocket, addr)).start()