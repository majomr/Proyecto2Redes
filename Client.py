from helpers import enter_to_continue, screen_clear
import socket
import threading
from argparse import ArgumentParser 
from Player import *
from config import *
from Art import *

nickname = None
isChating = False
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #socket initialization
client.connect((host, port))                             

def receive():
    while True:                                                 
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            elif message == 'ROOM':
                print(mainMenu())
            else:
                if(message):
                    msg = message.split("|")
                    if msg[0] == 'chating' and isChating:
                        print(msg[1])
                    else:
                        print(message)
        except Exception as e:                                            #case on wrong ip/port details
            print(e,"An error occured!")

def write():

    global isChating

    while True:                                                 
        message = "{}".format(input('\n'))

        if (message == 'rul' and not isChating):
            screen_clear()
            print(rules())
            enter_to_continue()
            print(mainMenu())
        elif (message == 'card' and not isChating):
            screen_clear()
            print(card())
            enter_to_continue()
            print(mainMenu())
        elif(message == 'chat' and not isChating):
            screen_clear()
            print(welcome_to_super_chat())
            isChating = True
            client.send('CHATING'.encode('ascii'))
        elif(message == 'exit' and isChating):
            client.send('chating|exit'.encode('ascii'))
            screen_clear()
            print(mainMenu())
            isChating = False
        elif (message == 'm' and not isChating):
            screen_clear()
            print(mainMenu())
        else:
            
            if isChating:
                message = "chating|" + message # Is a flag so the server knows this is a superchat message\
            
            client.send(message.encode('ascii'))

if __name__ == '__main__':

    parser = ArgumentParser(description=Player.__doc__)
    parser.add_argument("-n", "--name", dest="name",
                        help="Name on server")
    args = parser.parse_args()

    if args.name is None:
        args.name = input("Username: ")    

    nickname = args.name   
    receive_thread = threading.Thread(target=receive)               #receiving multiple messages
    receive_thread.start()
    write_thread = threading.Thread(target=write)                   #sending messages 
    write_thread.start()