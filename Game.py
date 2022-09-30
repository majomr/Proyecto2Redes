from Round import *

class Game(object):
	"""

       Each game has many round until one player wins

       2 players -> 7 tokens to win
       3 players -> 5 tokens to win
       4 players -> 4 tokens to win

	"""
	def __init__(self, players):
		'''Constructor'''
		super(Game, self).__init__()
		self.players = players
		
	def evaluate(self):
		'''Evaluate rounds needed to win'''

		for player in self.players:
			
			if(len(self.players)==2):
				if(player.wins_counter==1):
					return player
			elif(len(self.players)==3):
				if(player.wins_counter==1):
					return player
			elif(len(self.players)==4):
				if(player.wins_counter==4):
					return player
		return False

	def state(self):
		state = "TABLE AFTER THE ROUND:\n"
		for player in self.players:
			state += "\tPlayer: " + player.name + " Tokens: " + str(player.wins_counter) + "\n"

		return state

	def play(self):
		round_counter = 1
		while(not self.evaluate()):
			for player_ in self.players:
				player_.client.send('\n----------------Round #{}----------------'.format(round_counter).encode('ascii'))
			players = self.players
			current = Round(players)
			self.players = current.play()
			for player_ in self.players:
				player_.client.send('\n{}'.format(self.state()).encode('ascii'))
			round_counter += 1
		for player_ in self.players:
			player_.client.send('\n{}'.format(self.state()).encode('ascii'))
			player_.client.send('\n~~~~~~~~~~~~ WINNER IS {} ~~~~~~~~~~~~ '.format(self.evaluate()).encode('ascii'))
			player_.client.send('\n\n\n ++++++++++++ GAME OVER  ++++++++++++'.format(self.evaluate()).encode('ascii'))
			player_.client.close()





