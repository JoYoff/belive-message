import socket
import threading
from get_ip_system import get_ip
import json

get_ip()

fileObject = open("ip_keep.json", "r")
jsonContent = fileObject.read()
obj_python = json.loads(jsonContent)

HOST = obj_python['ip']
PORT = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
usernames = []

def broadcast(message):
	for client in clients:
		client.send(message)

def receive():
	while True:
		client, address = server.accept()
		print(f'Connecter avec {str(address)} !')

		client.send("NICK".encode('utf-8'))
		username = client.recv(1024)

		usernames.append(username)
		clients.append(client)

		print(f'Le pseudo du client est {username}')
		broadcast(f"{username} vient de se connecter !".encode("utf-8"))
		client.send("Tu as bien été connecté au serveur !".encode('utf-8'))

		thread = threading.Thread(target=handle, args=(client,))
		thread.start()

def handle(client):
	
	while True:
		try:
			message = client.recv(1024)
			print(f"{usernames[clients.index(client)]} : {message}")
			broadcast(message)
		except:
			index = clients.index(client)
			clients.remove(client)
			client.close()
			username = usernames[index]
			usernames.remove(username)

print("Server running...")
receive()