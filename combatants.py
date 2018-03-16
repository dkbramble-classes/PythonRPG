import random #for the chance aspect of the game
from observer import Observer
from observable import Observable
"""***************************************************************
	Classes of NPC's that will fight or help Player
		Monsters that die turn into a "Person", which heals Player 
		Characteristics:
			hp - Hit Points
			attack_val - how much they hurt Player
	@author Dane Bramble
	@version March 16, 2018
***************************************************************"""
class Person:
	"""********************************************
	Hit Points and Attack Value for the Person NPC
	********************************************"""
	def __init__(self):
		self.hp = 100
		self.attack_val = -1

	"""*************************************************
	get/set methods to return/set values of the npc
	*************************************************"""

	def getHp(self):
		return self.hp

	#@param value = value to set npc hp to
	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val

class Zombie(Observable):
	"""********************************************
	Hit Points and Attack Value for the Zombie NPC
	**********************************************"""
	def __init__(self):
		super(Zombie, self).__init__()
		self.hp = random.randint(50,101)
		self.attack_val = random.randint(0,11)

	"""*************************************************
	get/set methods to return/set values of the npc
	*************************************************"""

	def getHp(self):
		return self.hp

	#@param value = value to set npc hp to
	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val

class Vampire(Observable):
	"""*********************************************
	Hit Points and Attack Value for the Vampire NPC
	************************************************"""
	def __init__(self):
		super(Vampire, self).__init__()
		self.hp = random.randint(100,201)
		self.attack_val = random.randint(10,21)

	"""*************************************************
	get/set methods to return/set values of the npc
	*************************************************"""

	def getHp(self):
		return self.hp

	#@param value = value to set npc hp to
	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val

class Ghoul(Observable):
	"""******************************************
	Hit Points and Attack Value for the Ghoul NPC
	*********************************************"""
	def __init__(self):
		super(Ghoul, self).__init__()
		self.hp = random.randint(40,81)
		self.attack_val = random.randint(15,31)

	"""*************************************************
	get/set methods to return/set values of the npc
	*************************************************"""

	def getHp(self):
		return self.hp

	#@param value = value to set npc hp to
	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val

class Werewolf(Observable):
	"""*******************************************
	Hit Points and Attack Value for the Person NPC
	*******************************************"""
	def __init__(self):
		super(Werewolf, self).__init__()
		self.hp = 200
		self.attack_val = random.randint(0,41)

	"""*************************************************
	get/set methods to return/set values of the npc
	*************************************************"""

	def getHp(self):
		return self.hp

	#@param value = value to set npc hp to
	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val