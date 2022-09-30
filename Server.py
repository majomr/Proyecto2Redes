import socket
import select
import sys
import threading
from config import *
from Player import *
from Room import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              
server.bind((host, port))                                               #binding host and port to socket
server.listen()

players = []
rooms = []

def broadcast(message):                                                 
    for player in players:
        player.client.send(message)

def broadcast_chat(message, name):
    '''Send a msg to super chat'''
    for player in players:
        if player.name != name:
            message = "chating|[{}]: {}".format(name, message).encode('ascii')
            player.client.send(message)


def handle(player):
    client = player.client  
    name = player.name                                       
    while True:
        try:
            if(not player.room):    
                client.send('ROOM'.encode('ascii'))   
                
                msg = client.recv(1024).decode('ascii') 

                if msg == "CHATING":
                    player.isChating = True
                    while player.isChating:
                        message = client.recv(1024).decode('ascii')
                        message = message.split("|")
                        print(message)
                        if message[0] == "chating" and message[1] == "exit":
                            player.isChating = False
                            break
                        else:
                            if len(players) > 1:
                                broadcast_chat(message[1], name)
                            else:
                                player.client.send("Wait for mor players to join.")
                
                msg = client.recv(1024).decode('ascii') 

                # Aqui muere
                room_id = msg
                room_id = int(room_id)
                room = None
                if(room_id==0):
                    room = Room(len(rooms)+1)
                    rooms.append(room)
                else:
                    for room_ in rooms:
                        if(room_._id==room_id):
                            room = room_
                room.join(player)

            elif(player.room and not player.room.isPlaying):
                players_ = player.room.play()
                for player_ in players_:            
                    players.remove(player_)
                    player_.client.close()
                    nickname = player.name
                break

            else:
                message = client.recv(1024).decode('ascii')
                # msg = message.split("|")
                
                # print(msg)

                # if len(msg) > 0:
                #     if msg[0] == "chating":
                #         broadcast_chat(msg[1], name)

                broadcast(message)
        except Exception as e:      
            print(e)                                               
            index = players.index(player)
            players.remove(player)
            client.close()
            nickname = player.name
            broadcast('{} left the server!'.format(nickname).encode('ascii'))
            break

def receive():                                                          
    while True:
        client, address = server.accept()     
        client.send('NICKNAME'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        player = Player(nickname, client)
        players.append(player)
        print("Connected with {} as {}".format(str(address), nickname))  
        broadcast("********************************\n"
                  "{} joined the server!\n"
                  "********************************".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(player,))
        thread.start()

receive()