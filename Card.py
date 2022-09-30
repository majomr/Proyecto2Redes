class Card(object):
	"""
		Class object for card

		Each card has a name and a privacy config
	"""
	def __init__(self, name, value):
		super(Card, self).__init__()
		self.name = name
		self.public = False
		self.value = value
	
	def __str__ (self):
		return (" Name:" + self.name + " \tValue:" + str(self.value))