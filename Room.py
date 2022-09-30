from Game import *
import socket
import threading

class Room(object):
    """docstring for Room"""

    def __init__(self, _id):
        super(Room, self).__init__()
        self._id = _id
        self.isPlaying = False
        self.players = []
        self.admin = None
        self.threads = []

    def join(self, player):
        if (len(self.players) == 4):
            player.client.send("The room is full".encode('ascii'))
            return (0)
        player.room = self
        self.players.append(player)
        if (not self.admin):
            self.admin = player
        for player_ in self.players:
            if (player_ == player):
                player_.client.send("--  You are in the room with id {} now  --".format(self._id).encode('ascii'))
            else:
                player_.client.send("--  {} joined the room  --".format(player).encode('ascii'))

    def remove(self, player):
        self.players.pop(self.players.index(player))
        player_.client.send("--  {} left the room  --".format(player).encode('ascii'))

    # def broadcast(self, message, client):
    #     '''Broadcast Messages'''
    #     for player_ in self.players:
    #         if player_.client == client:
    #             name = player_.name
    #     for player_ in self.players:
    #         if player_.client != client:
    #             player_.client.send("[{}]: {}".format(name, message).encode('ascii'))
        
    # def handle(self, client):
    #     while True:
    #         try:
    #             message = client.recv(1024).decode('ascii')
    #             if message == "exit" and client == self.admin.client:
    #                 for thread_ in self.threads:
    #                     thread_.join()
    #             else:
    #                 self.broadcast(message, client)
    #         except:

    #             # self.players.remove(client)
    #             client.close()
    #             break

    def play(self):
        
        self.admin.client.send("_________________________________________\n"
							   "\tYou are the admin of the room\n"
							   "\t\tPress 's' to start the game\n"
							   "\t\tPress 'x' to kill the room\n"
							   "_________________________________________".encode('ascii'))
        
        start = False
        
        while (not start):
            
            # The admin has control of these things
            # S: Start the game
            # X: Kill the room
            # C: Group Chat

            admin_choice = self.admin.client.recv(1024).decode('ascii')

            if (admin_choice == "s"):
                '''Start the game'''
                if (len(self.players) >= 2 and len(self.players) <= 4):
                    for player_ in self.players:
                        player_.client.send("############################\n  {} started the game\n############################\n ".format(self.admin).encode('ascii'))
                    game = Game(self.players)
                    self.isPlaying = True
                    game.play()
                    return (self.players)
                else:
                    self.admin.client.send("Wait for more players to join the room... ".encode('ascii'))
            
            if (admin_choice == "x"):
                '''Kill the game'''
                for player_ in self.players:
                    player_.room = None
                self.players = []
                player_.client.send("XXX {} destroyed the room  XXX".format(self.admin).encode('ascii'))
                return ([])
            
            # if(admin_choice == "c"):
            #     '''Group chat'''
            #     if (len(self.players) >= 2 and len(self.players) <= 4):
            #         # Notify every one that they enter superchat mode
            #         for player_ in self.players:
            #             player_.client.send("\n\n__________________________________________________________________\n\n\t                      CHAT ROOM                      \n__________________________________________________________________\n\n>>".encode('ascii'))
                        
            #             # Launch Chat Room to evreyone
            #             # Create threads
                        
            #             thread = threading.Thread(target=self.handle, args=(player_.client,))
            #             self.threads.append(thread)
            #             thread.start()


            #     else:
            #         self.admin.client.send("Wait for more players to join the room... ".encode('ascii'))
        
        for player_ in self.players:
            player_.client.send('\n+++++++++++++++++++++++++++++++\n'
								'++++++++++ GAME OVER ++++++++++\n'
								'+++++++++++++++++++++++++++++++\n'.encode('ascii'))
        return (self.players)
