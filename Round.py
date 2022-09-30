from Deck import *

class Round(object):
    """
        
        Each round has a deck
        And a group of player from 2-4 they should come inherited 
            from Game
        Each player has a turn 

    """
    def __init__(self, players):
        super(Round, self).__init__()
        self.init_players = players
        self.players = players
        self.players_order = []
        self.protected = []
        self.deck = Deck()

    def sort(self):
        toReturn = self.players
        for player_ in self.players_order:
            toReturn.append(player_)
        return(toReturn)

    def state(self):
        state = "\n\nGAME STATE:\n\n"
        for player in self.players:
            state = state +  str(player.name) + " | Card: *****\t\n"
        state += "\n\n Cards on deck \t" + str(self.deck.state()) + "\n"
        return (state)

    def show(self):
        state = "\n\n\n\n"
        for player in self.players:
            state += str(player.name)
        return (state)

    def play(self):

        player_index = 0
        winner = None
        
        for player in self.players:
             player.current_card = self.deck.pull()
        
        while (self.deck.state()!=0):

             if(len(self.players)==1):
                 break
             for player_ in self.players:
                 player_.client.send("{}".format(self.state()).encode('ascii'))
                 player_.client.send("YOUR CARD IS {}\n".format(player_.current_card).encode('ascii'))

             current_card = self.deck.pull()
             current_player = self.players[player_index]

             for protected in self.protected:
                 if(protected==current_player):
                     protected.protection = False
            
             for player_ in self.players:
                player_.client.send("It is the turn of {}\n".format(current_player).encode('ascii'))

            # Let the current player in turn decide which card to keep. 
             picked_card = current_player.play(current_card)
            
             for player_ in self.players:
                 player_.client.send("{} put a {} on the table".format(current_player,picked_card.name).encode('ascii'))
            
             if(picked_card.name == 'Guard'):
                 for player_ in self.players:
                     player_.client.send("\n Guard allows you to discard one oponent if you guess right the card they have\n".encode('ascii'))
                 done = True
                 are_oponents = False
                 current_player.client.send("\n Oponents:\n".encode('ascii'))
                 for player2 in self.players:
                     if(not player2.protection and player2!=current_player):
                         are_oponents = True
                         current_player.client.send("\t {}".format(player2.name).encode('ascii'))
                 if(are_oponents):
                     current_player.client.send("\nPick the oponent:\t".encode('ascii'))
                     oponent = current_player.client.recv(1024).decode('ascii')
                 else:
                     done = False
                     current_player.client.send("\t There are not available oponents in this round".encode('ascii'))
                 while(done):
                     for player in self.players:
                         if(player.name == oponent):
                             current_player.client.send("Guess the card of {}:\t".format(player).encode('ascii'))
                             picked = current_player.client.recv(1024).decode('ascii')
                             if(picked=='Guard' or picked=='Priest' or picked=='Baron' or picked=='Handmaid' or picked=='Prince' or picked=='King' or picked=='Countess' or picked=='Princess'):
                                 done = False
                                 for player_ in self.players:
                                     player_.client.send("{} chose {} and says that the hidden card is a {}".format(current_player,player,picked).encode('ascii'))
                                 if(picked==player.current_card.name):
                                     self.players_order.append(self.players.pop(self.players.index(player)))
                                     for player_ in self.players:
                                         player_.client.send("{} guest the card correctly. {} is out!".format(current_player,player).encode('ascii'))
                                     player.client.send("You are out! Wait until the round is over".encode('ascii'))
                                 else:
                                     for player_ in self.players:
                                         player_.client.send("{} chose guest card incorrectly. {} is still on the game!".format(current_player,player).encode('ascii'))
                             else:
                                 current_player.client.send("Pick a valid card, options are:\n\t Guard\n\t Priest\n\t Baron\n\t Handmaid\n\t Prince\n\t King\n\t Countess\n\t Princess".encode('ascii'))
                     if(done):
                         current_player.client.send("PLEASE WRITE IT GOOD! YOU LOST A TURN".encode('ascii'))									 #This one works
                         done = False
             elif(picked_card.name == 'Priest'):										#This one works
                 for player_ in self.players:
                     player_.client.send("\n Priest allows you to see an oponent's card\n".encode('ascii'))
                 done = True
                 are_oponents = False
                 current_player.client.send("\n Oponents:\n".encode('ascii'))
                 for player2 in self.players:
                     if(not player2.protection and player2!=current_player):
                         are_oponents = True
                         current_player.client.send("\t {}".format(player2.name).encode('ascii'))
                 if(are_oponents):
                     current_player.client.send("\nPick the oponent:\t".encode('ascii'))
                     oponent = current_player.client.recv(1024).decode('ascii')
                 else:
                     done = False
                     current_player.client.send("\t There are not available oponents in this round".encode('ascii'))
                 while(done):
                     for player in self.players:
                         if(player.name == oponent and not player.protection and player!=current_player):
                             current_player.client.send("{} has a {} ".format(player, player.current_card).encode('ascii'))
                             for player_ in self.players:
                                 player_.client.send("{} saw {}'s card".format(current_player, player).encode('ascii'))
                             done = False
                     if(not done):
                         current_player.client.send("Choose a valid player".encode('ascii'))
            
             elif(picked_card.name == 'Baron'):
                 for player_ in self.players:
                     player_.client.send("\n Baron allows you to check secretly one's card and the lowest one will be out of the game\n".encode('ascii'))
                 done = True
                 are_oponents = False
                 current_player.client.send("\n Oponents:\n".encode('ascii'))
                 for player2 in self.players:
                     if(not player2.protection and player2!=current_player):
                         are_oponents = True
                         current_player.client.send("\t {}".format(player2.name).encode('ascii'))
                 if(are_oponents):
                     current_player.client.send("\nPick the oponent:\t".encode('ascii'))
                     oponent = current_player.client.recv(1024).decode('ascii')
                 else:
                     done = False
                     current_player.client.send("\t There are not available oponents in this round".encode('ascii'))
                 while(done):
                     for player in self.players:
                         if(player.name == oponent and not player.protection and player!=current_player):
                             for player_ in self.players:
                                 player_.client.send("{} chose {}".format(current_player, player).encode('ascii'))
                             current_player.client.send("{} has a {} ".format(player, player.current_card).encode('ascii'))
                             player.client.send("{} has a {} ".format(current_player, current_player.current_card).encode('ascii'))
                             if(player.current_card.value < current_player.current_card.value):
                                 for player_ in self.players:
                                     player_.client.send("{}'s card has a greater value, {} is out!".format(current_player, player).encode('ascii'))
                                 player.client.send("You are out! Wait until the round is over".encode('ascii'))
                                 self.players_order.append(self.players.pop(self.players.index(player)))
                             elif(current_player.current_card.value < player.current_card.value):
                                 for player_ in self.players:
                                     player_.client.send("{}'s card  had a greater value, {} is out!".format(player, current_player).encode('ascii'))
                                 current_player.client.send("You are out! Wait until the round is over".encode('ascii'))
                                 self.players_order.append(self.players.pop(self.players.index(current_player)))
                             else:
                                 for player_ in self.players:
                                     player_.client.send("{} and {} hav the same card's no one is out!".format(player, current_player).encode('ascii'))
                             done = False
                     if(done):
                         current_player.client.send("PLEASE WRITE IT GOOD! YOU LOST A TURN".encode('ascii'))									 #This one works
                         done = False
             elif(picked_card.name == 'Handmaid'):									#This one works
                 for player_ in self.players:
                     player_.client.send("\n Handmaid gives you protection from others cards until your next turn\n".encode('ascii'))	
                 current_player.protection = True
                 self.protected.append(current_player)
                 current_player.client.send("Your protection is now activated until next turn".encode('ascii'))
            
             elif(picked_card.name == 'Prince'):
                 for player_ in self.players:
                     player_.client.send("\n Prince allows you to make someone discard the card they have and pull a new one\n".encode('ascii'))
                 done = True
                 are_oponents = False
                 current_player.client.send("\n Oponents:\n".encode('ascii'))
                 for player2 in self.players:
                     if(not player2.protection and player2!=current_player):
                         are_oponents = True
                         current_player.client.send("\t {}".format(player2.name).encode('ascii'))
                 if(are_oponents):
                     current_player.client.send("\nPick the oponent:\t".encode('ascii'))
                     oponent = current_player.client.recv(1024).decode('ascii')
                 else:
                     done = False
                     current_player.client.send("\t There are not available oponents in this round".encode('ascii'))
                 while(done):
                     for player in self.players:
                         if(player.name == oponent and not player.protection):
                             for player_ in self.players:
                                 player_.client.send("{} chose ".format(current_player, player).encode('ascii'))	
                             player.used_cards.append(current_card)
                             player.current_card = self.deck.pull()
                             player.client.send("You have a new card now and is a {}".format(player.current_card).encode('ascii'))
                             for player_ in self.players:
                                 player_.client.send("{} has a new card ".format(player).encode('ascii'))	
                             done = False
                     if(done):
                         current_player.client.send("PLEASE WRITE IT GOOD! YOU LOST A TURN".encode('ascii'))									 #This one works
                         done = False
             elif(picked_card.name == 'King'):
                 for player_ in self.players:
                     player_.client.send("\n King allows you exchage your cards with an oponent\n".encode('ascii'))
                 current_player.client.send("\n Oponents:".encode('ascii'))
                 done = True
                 are_oponents = False
                 current_player.client.send("\n Oponents:\n".encode('ascii'))
                 for player2 in self.players:
                     if(not player2.protection and player2!=current_player):
                         are_oponents = True
                         current_player.client.send("\t {}".format(player2.name).encode('ascii'))
                 if(are_oponents):
                     current_player.client.send("\nPick the oponent:\t".encode('ascii'))
                     oponent = current_player.client.recv(1024).decode('ascii')
                 else:
                     done = False
                     current_player.client.send("\t There are not available oponents in this round".encode('ascii'))
                 while(done):
                     for player in self.players:
                         if(player.name == oponent and not player.protection and player!=current_player):
                             current_player.current_card, player.current_card = player.current_card, current_player.current_card
                             current_player.client.send("Your new card is  {}".format(player.current_card).encode('ascii'))
                             player.client.send("Your new card is  {}".format(current_player.current_card).encode('ascii'))
                             for player_ in self.players:
                                 player_.client.send("{} exchanged with {}".format(current_player, player).encode('ascii'))	
                             done = False
                     if(done):
                         current_player.client.send("PLEASE WRITE IT GOOD! YOU LOST A TURN".encode('ascii'))									 #This one works
                         done = False
             elif(picked_card.name == 'Countess'):									#This one works
                 for player_ in self.players:
                     player_.client.send("\n Countess has no action\n".encode('ascii'))									
             elif(picked_card.name == 'Princess'):
                 for player_ in self.players:
                     player_.client.send("\n If Princess is discarted to are out of the round".format(current_player, player).encode('ascii'))
                 self.players_order.append(self.players.pop(self.players.index(current_player)))
                 for player_ in self.players:
                     player_.client.send("{} has left the round ".format(current_player).encode('ascii'))
                 current_player.client.send("You are out! Wait until the round is over".encode('ascii'))							     #This one works
             player_index = (player_index+1)%len(self.players)
        for player_ in self.init_players:
             player_.client.send("{}".format(self.show()).encode('ascii'))

         #Evaluate who wins:
        for player in self.init_players:
             values = [player.current_card.value for player in self.players]
             winner_value = max(values)
             if(values.count(winner_value)==1):
                 winner = values.index(winner_value)
                 self.players[winner].wins_counter += 1
                 for player_ in self.players:
                     player_.client.send("Winner is {} ".format(self.players[winner]).encode('ascii'))
             else:
                 for player_ in self.players:
                     player_.client.send("Is a tie! No one wins".encode('ascii'))
        return (self.sort())
        