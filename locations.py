import random #for the chance aspect of the game
from observer import Observer
from observable import Observable
from combatants import *
"""***************************************************************
	Classes of locations that Player can enter, can either help 
	Player stats or host monsters of which to fight

	@author Dane Bramble
	@version March 16, 2018
***************************************************************"""

class CareCenter:
	"""******************************************************
	A class to store Care Center information.
	Any Player that enters will have they're hp boosted to 200. 
	Can only be used once
	******************************************************"""
	def __init__(self):
		self.uses = 1
	"""*********************************************
	Boosts Player hp to 200. Can only be used once.
	@param player = Player to have health boosted
	*********************************************"""
	def healin_time(self, player):
		if self.uses <> 0:
			player.setHp(200)
			self.uses = self.uses - 1
		else:
			print("Insurance only covers one visit...")

	"""*************************************************
	get/set methods to return/set values of the location
	*************************************************"""

	#return the map symbol that the grid will use
	def getSymbol(self):
		self.symbol = '+'
		return self.symbol

	def getUses(self):
		return self.uses

class SupplyShop:
	"""********************************************************************************
	A Class to store Supply Shop information, which refills weapon usages when entered. 
	Can only be used once
	***********************************************************************************"""

	def __init__(self):
		self.uses = 1 #how many times it can be used

	"""**************************************************************
	return all weapons to original usage count, can only be done once
	@param player = Player to have weapons renewed
	**************************************************************"""
	def restockin_time(self, player):
		if self.uses <> 0:
			for i in player.weapons:
				if i.getUses() == 0:
					i.setUses(i.getStock())
			self.uses = self.uses - 1
		else:
			print("Out of Money!")

	"""*************************************************
	get/set methods to return/set values of the location
	*************************************************"""

	#return the map symbol that the grid will use
	def getSymbol(self):
		self.symbol = '$'
		return self.symbol

	def getUses(self):
		return self.uses

"""****************************************************************
	A Class for Homes that can be filled with monsters to fight
	This is updated by the Monsters to replace them with a Person, 
	and to decrement the # of monsters by one
****************************************************************"""
class Home(Observer):
	"""******************************
	A class to store Home information
	******************************"""
	def __init__(self):
		self.monsters = []
		#Populate the Home with 0-10 random monsters
		while len(self.monsters) < random.randint(0, 11):
			rand = random.randint(1,5)
			if rand == 1:
				w = Zombie()
				self.monsters.append(w)
				w.add_observer(self) #registers this home with the monster so it can be updated
			elif rand == 2:
				w = Vampire()
				self.monsters.append(w)
				w.add_observer(self) #registers this home with the monster so it can be updated
			elif rand == 3:
				w = Ghoul() 
				self.monsters.append(w)
				w.add_observer(self) #registers this home with the monster so it can be updated
			elif rand == 4:
				w = Werewolf()
				self.monsters.append(w)
				w.add_observer(self) #registers this home with the monster so it can be updated
		#number of monsters in this specific home
		self.num_monsters = len(self.monsters)

	"""*************************************************
	get/set methods to return/set values of the home
	*************************************************"""

	def getMonsters(self):
		return self.monsters

	def getNumMonsters(self):
		return self.num_monsters

	#updates for observer class

	def update(self):
		index = 0 #tracker of which monster needs to be replaced
		for i in self.monsters:
			if i.getHp() <= 0:
				self.monsters[index] = Person() #replace monster with Person
				break #only one monster should be replaced at a time
			index = index + 1
		self.num_monsters = self.num_monsters - 1 #decrement the number of monsters