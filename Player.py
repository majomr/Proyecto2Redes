class Player(object):
	"""
		Each player has a curret card
		Each player has used cards
		Each player has a wins counter
	"""

	def __init__(self, name, client):
		super(Player, self).__init__()
		self.name = name
		self.used_cards = []
		self.current_card = None
		self.wins_counter = 0
		self.client = client
		self.room = None
		self.protection = False					#When you play a handmaid this value is setted to true
		self.isChating = False

	def reset(self):
		self.protection = False
		self.wins_counter = 0
		self.current_card = None
		self.used_cards = []

	def play(self, current_card):
		picked = None
		while(picked != self.current_card.name or picked != current_card.name):
			
			# Show the player the cards from where he can choose one
			self.client.send("\n\nChoose which card do you want to keep, the other will be played on the table\n\n\t1: {} \n\t2: {}\n\:".format(current_card, self.current_card).encode('ascii'))
			
			# This is the card that the player whants to keep
			picked = self.client.recv(1024).decode('ascii')

			if(picked == self.current_card.name):
				self.used_cards.append(current_card) # Player does not whant this card any more
				return (self.current_card)
			else:
				self.used_cards.append(self.current_card) # Player does not whant this card any more
				new_card = current_card
				self.current_card = current_card
				current_card = new_card
				return(current_card)

	def __str__ (self):
		return (self.name)