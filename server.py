import socket
from threading import Thread

SERVER = None
IP_ADDRESS = '127.0.0.1'
PORT = 6000

CLIENTS = {} # stores all player details

def setup():
    print("\n\t\t\t\t\t*** Welcome to The Game of Tambola ***\n")

    global SERVER
    global IP_ADDRESS
    global PORT

    # creating a server and binding it w/ ip addr and port
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10) # making server ONLY listen to 10 connections/requests

    print("\t\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...\n")
    
    acceptConnections()

# accept incoming connections from clients continously
def acceptConnections():
    global CLIENTS
    global SERVER
    while True:
        player_socket, addr = SERVER.accept()
        player_name = player_socket.recv(1024).decode().strip()
        print('player name:', player_name)

        if(len(CLIENTS.keys()) == 0):
            CLIENTS[player_name] = {'player_type': 'player1'}
        else:
            CLIENTS[player_name] = {'player_type': 'player2'}
        
        # storing player data in CLIENTS{}
        CLIENTS[player_name]['player_socket'] = player_socket
        CLIENTS[player_name]['address'] = addr
        CLIENTS[player_name]['player_name'] = player_name
        CLIENTS[player_name]['turn'] = False

        print(f'Connection established with {player_name}: {addr}')

setup()