import random
from Card import *

class Deck(object):
	"""docstring for Deck

		This is instatiation of the deck
		each one has:

			5 Guards
			2 Priest
			2 Baron
			2 Handmaid
			2 Prince
			1 King
			1 Countess
			1 Princess
	
	"""
	def __init__(self):
		super(Deck, self).__init__()
		self.deck = [
			Card('Guard', 1),
			Card('Guard', 1),
			Card('Guard', 1),
			Card('Guard', 1),
			Card('Guard', 1),
			Card('Priest', 2),
			Card('Priest', 2),
			Card('Baron', 3),
			Card('Baron', 3),
			Card('Handmaid', 4),
			Card('Handmaid', 4),
			Card('Prince', 5),
			Card('Prince', 5),
			Card('King', 6),
			Card('Countess', 7),
			Card('Princess', 8),
		]

	def state(self):
		return (len(self.deck))

	def pull(self):
		index = random.randint(0, len(self.deck) - 1)
		return (self.deck.pop(index))