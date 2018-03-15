from __future__ import print_function #allows input() function for earlier python versions
import random #for the chance aspect of the game
#for the Observer Pattern
from observer import Observer
from observable import Observable
"""
Creates an RPG where a player goes through a neighborhood 
saving people from monsters. The game ends when a person is 
out of hp or if all the monsters are people again.

Sources: 
	Observer Pattern code from Professor Woodring
	Input Scanner/'from __future__' import and
		__class__.__name__ from Stack Overflow

@author Dane Bramble
@version March 14, 2018

"""

"""Weapon Classes: 	
	Different Weapons Player can use:
		mod = attack multiplier to modify Player attack value
		uses = how many times a weapon can be used
"""
class HersheyKiss:
	"""Attack Multiplier and Uses for HersheyKiss"""
	def __init__(self):
		self.mod = 1
		self.uses = 1000 

	def getMod(self):
		return self.mod

	def getUses(self):
		return self.uses

	#sets uses to new value
	def setUses(self, value):
		self.uses = value

class SourStraw:
	"""Attack Multiplier, Uses, and Stock Uses for SourStraw"""
	def __init__(self):
		self.mod = random.uniform(1.0, 1.75)
		self.uses = 10 # was 2
		self.stock_val = self.uses #amount of times default weapon can be used

	def getMod(self):
		return self.mod

	def getUses(self):
		return self.uses

	def getStock(self):
		return self.stock_val

	#sets uses to new value
	def setUses(self, value):
		self.uses = value

class ChocolateBar:
	"""Attack Multiplier, Uses, and Stock Uses for ChocolateBar"""
	def __init__(self):
		self.mod = random.uniform(2.0, 2.4)
		self.uses = 12 # was 4
		self.stock_val = self.uses #amount of times default weapon can be used

	def getMod(self):
		return self.mod

	def getUses(self):
		return self.uses

	def getStock(self):
		return self.stock_val

	#sets uses to new value
	def setUses(self, value):
		self.uses = value

class NerdBomb:	
	"""Attack Multiplier, Uses, and Stock Uses for NerdBomb"""
	def __init__(self):
		self.mod = random.uniform(3.5, 5)
		self.uses = 5 # was 1
		self.stock_val = self.uses #amount of times default weapon can be used

	def getMod(self):
		return self.mod

	def getUses(self):
		return self.uses

	def getStock(self):
		return self.stock_val

	#sets uses to new value
	def setUses(self, value):
		self.uses = value

#The main character fighting to save his/her neighborhood
class Player:
	"""A class to store Player information"""
	def __init__(self):
		self.location = [0,0] #The Neighborhood grid location of the house the player is at
		self.hp = random.randint(100, 126) #hit points for the player
		self.attack_val = random.randint(10, 21) #default hit points without weapon multiplier
		self.weapons = [] #list of weapons the player has
		while len(self.weapons) < 10:
			#puts a random list of ten weapons in the player inventory
			rand = random.randint(1,5)
			if rand == 1:
				w = HersheyKiss()
				self.weapons.append(w)
			elif rand == 2:
				w = SourStraw()
				self.weapons.append(w)
			elif rand == 3:
				w = ChocolateBar() 
				self.weapons.append(w)
			elif rand == 4:
				w = NerdBomb()
				self.weapons.append(w)

	def getHp(self):
		return self.hp

	#@param value = value hp will be set to
	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val

	def getWeapons(self):
		return self.weapons

	def getLocation(self):
		return self.location

	#sets the location to a new grid position (width, height)
	def setLocation(self, width, height):
		self.location = [width, height]

"""Classes of NPC's that will fight or help Player
		Monsters that die turn into a "Person", which heals Player 
		Characteristics:
			hp - Hit Points
			attack_val - how much they hurt Player
"""
class Person:
	"""Hit Points and Attack Value for the Person NPC"""
	def __init__(self):
		self.hp = 100
		self.attack_val = -1

	def getHp(self):
		return self.hp

	#sets hp to new value
	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val

class Zombie(Observable):
	"""Hit Points and Attack Value for the Zombie NPC"""
	def __init__(self):
		super(Zombie, self).__init__()
		self.hp = random.randint(50,101)
		self.attack_val = random.randint(0,11)

	def getHp(self):
		return self.hp

	#sets hp to new value
	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val

class Vampire(Observable):
	"""Hit Points and Attack Value for the Vampire NPC"""
	def __init__(self):
		super(Vampire, self).__init__()
		self.hp = random.randint(100,201)
		self.attack_val = random.randint(10,21)

	def getHp(self):
		return self.hp

	#sets hp to new value
	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val

class Ghoul(Observable):
	"""Hit Points and Attack Value for the Ghoul NPC"""
	def __init__(self):
		super(Ghoul, self).__init__()
		self.hp = random.randint(40,81)
		self.attack_val = random.randint(15,31)

	def getHp(self):
		return self.hp

	#sets hp to new value
	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val

class Werewolf(Observable):
	"""Hit Points and Attack Value for the Person NPC"""
	def __init__(self):
		super(Werewolf, self).__init__()
		self.hp = 200
		self.attack_val = random.randint(0,41)

	def getHp(self):
		return self.hp

	#sets hp to new value
	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val

class CareCenter:
	"""A class to store Care Center information. Any Player that enters will have they're hp boosted to 200. Can only be used once"""
	def __init__(self):
		self.uses = 1
	"""
	Boosts Player hp to 200. Can only be used once.
	@param player = Player to have health boosted
	"""
	def healin_time(self, player):
		if self.uses <> 0:
			player.setHp(200)
			self.uses = self.uses - 1
		else:
			print("Insurance only covers one visit...")

	#return the map symbol that the grid will use
	def getSymbol(self):
		self.symbol = '+'
		return self.symbol

	def getUses(self):
		return self.uses

class SupplyShop:
	""" A Class to store Supply Shop information, which refills weapon usages when entered. Can only be used once"""

	def __init__(self):
		self.uses = 1 #how many times it can be used
	"""
	return all weapons to original usage count, can only be done once
	@param player = Player to have weapons renewed
	"""
	def restockin_time(self, player):
		if self.uses <> 0:
			for i in player.weapons:
				if i.getUses() == 0:
					i.setUses(i.getStock())
			self.uses = self.uses - 1
		else:
			print("Out of Money!")

	#return the map symbol that the grid will use
	def getSymbol(self):
		self.symbol = '$'
		return self.symbol

	def getUses(self):
		return self.uses

"""
	A Class for Homes that can be filled with monsters to fight
	This is updated by the Monsters to replace them with a Person, 
	and to decrement the # of monsters by one
"""
class Home(Observer):
	"""A class to store Home information"""
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

	def getMonsters(self):
		return self.monsters

	def getNumMonsters(self):
		return self.num_monsters

	def update(self):
		index = 0 #tracker of which monster needs to be replaced
		for i in self.monsters:
			if i.getHp() <= 0:
				self.monsters[index] = Person() #replace monster with Person
				break #only one monster should be replaced at a time
			index = index + 1
		self.num_monsters = self.num_monsters - 1 #decrement the number of monsters

#The Collection of houses the player must move through to kill the monsters
class Neighborhood(Observer):
	"""A class to store Neighborhood information, print function and the Game's Rules"""
	total_monsters = 0 #The grand total of all the monsters from all homes
	monsters_defeated = 0 #count of monsters defeated
	""" """
	def __init__(self, height, width):
		if (height > 0 and width > 0): 
		#Set the width and height of the grid in which the homes will reside
			self.height = height
			self.width = width
			self.grid = []
			for i in range(width): #populate the grid with homes
				self.grid.append([])
				for j in range(height):
					#change what the object is based on chance
					rand = random.randint(0,100)
					if rand < 10:
						#10% of the time
						h = CareCenter()
					elif rand < 25 and rand > 9:
						#15% of the time
						h = SupplyShop()
					else:
						#the rest of the time
						h = Home()
						for m in h.monsters: #register the Neighborhood with each monster in every house
							m.add_observer(self)
						Neighborhood.total_monsters = Neighborhood.total_monsters + h.getNumMonsters() #increment total number of monsters
					self.grid[i].append(h)
		else:
			print("A Neighborhood can't be that size!")
			self.grid = []#set grid to empty

	"""
	Displays Neighborhood map on terminal, allows Player to move to any house
	@param player the player moving through the neighborhood 
	"""
	def display_map(self, player):
		if len(self.grid) > 0: #if grid size is viable
			print("\033[H\033[J") #clears current screen
			if Neighborhood.total_monsters < 1: 
				print('The Neighborhood is saved! ' + str(Neighborhood.monsters_defeated) + " Monsters Defeated!") #No more monsters!
				return
			elif player.getHp() < 1:
				print("The Monsters have won..." + str(Neighborhood.monsters_defeated) + " Monsters Defeated") #You've been beaten
				return
			else: #only display board if the game isn't over
				print ("\nKey: * = player location, # = Monster count per house, $ = Restock Weapons, + = Health Boost \n\nNeighborhood:\n")
				count = 1 #Counter to help print grid correctly
				#prints the grid on the terminal
				for i in range(len(self.grid)): #width of grid 
					for j in range(len(self.grid[i])):#height of grid
						if self.grid[i][j].__class__.__name__ == "Home":
							mark = str(self.grid[i][j].getNumMonsters()) #if the grid entry is a home, label it as such
						else:
							mark = self.grid[i][j].getSymbol() #else, label it as its proper symbol
						if (i == player.getLocation()[0] and j == player.getLocation()[1]):
							current = self.grid[i][j] #Keeps track of the current grid instance
							mark = '*' #Player cursor
						if (count % len(self.grid[i]) == 0):
							print(mark + " ")
							if i < len(self.grid) - 1:
								for k in range(len(self.grid[i])):
									print("|   ", end='') #Street lines
								print("")
						else:
							print(mark + "---", end='') #Street lines
						count = count + 1
				#Game Stats
				if current.__class__.__name__ == "Home":
					print("\n# of Monsters in Current Home: " + str(current.getNumMonsters()))
				else:
					print("\n# of Visits Available: " + str(current.getUses()))
				print("Total # of Monsters in Neighborhood: " + str(Neighborhood.total_monsters))
				print("Your HP: " + str(player.getHp()))
				#User keyboard input to decide the next move
				x = raw_input("\nNext Move? \nOptions:\nEnter house (enter key), \nMove to next house ('w','a','s','d' for up, left, down, right respectively), \nor Quit ('quit')\n")
				if (x == ""):#if input is 'enter'
					if current.__class__.__name__ == "Home":
						self.fightin_time(player, current) #Start turn based combat in current house
					elif current.__class__.__name__ == "SupplyShop":
						current.restockin_time(player)
						self.display_map(player) #display options again
					else: #if Care Center
						current.healin_time(player)
						self.display_map(player) #display options again
				#Move in a direction on the grid
				elif(x == "w" or x == "W"):
					if (player.getLocation()[0]  > 0):
						player.setLocation(player.getLocation()[0] - 1, player.getLocation()[1])
					else:
						print("\nOutside the Neighborhood bounds!")
					self.display_map(player)
				elif(x == "a" or x == "A"):
					if (player.getLocation()[1]  > 0):
						player.setLocation(player.getLocation()[0], player.getLocation()[1] - 1)
					else:
						print("\nOutside the Neighborhood bounds!")
					self.display_map(player)
				elif(x == "s" or x == "S"):
					if (player.getLocation()[0] + 1 < self.width):
						player.setLocation(player.getLocation()[0] + 1, player.getLocation()[1])
					else:
						print("\nOutside the Neighborhood bounds!")
					self.display_map(player)
				elif(x == "d" or x == "D"):
					if (player.getLocation()[1] + 1 < self.height):
						player.setLocation(player.getLocation()[0], player.getLocation()[1] + 1)
					else:
						print("\nOutside the Neighborhood bounds!")
					self.display_map(player)
				elif(x == "quit" or x == "Quit"):
					print("\nGoodbye!")
				else: #if anything else
					self.display_map(player) #display options again


	"""
	Turn based fighting of the game, Player uses all weapons on all enemies, then all the the monsters/people fight/heal Player
	@param player the Player that is fighting the monsters
	@param house the Home in which the monsters reside
	"""
	def fightin_time(self, player, house):
		while house.getNumMonsters() > 0 and player.getHp() > 0: #Keep fighting until you or the monsters win
			for i in house.getMonsters():
				for j in player.getWeapons():
					if j.getUses() > 0 and i.getHp() > 0:
						attack = player.getAttack() * j.getMod() #sets amount you will hurt monsters
						#Rules for what hurts which monsters and how badly, checks to see if the class name matches a string
						if i.__class__.__name__ == "Zombie" and j.__class__.__name__ == "SourStraw":
							attack = attack * 2
						elif i.__class__.__name__ == "Vampire" and j.__class__.__name__ == "ChocolateBar":
							attack = 0
						elif i.__class__.__name__ == 'Ghoul' and j.__class__.__name__ == "NerdBomb":
							attack = attack * 5
						elif i.__class__.__name__ == "Werewolf" and (j.__class__.__name__ == "ChocolateBar" or j.__class__.__name__ == "SourStraw"):
							attack = 0
						elif i.__class__.__name__ == "Person":
							attack = 0
						i.setHp(i.getHp() - attack) #attack value lowers monster hp
						if i.getHp() <= 0: #if the monster dies
							i.update()#updates home and neighborhood to replace the monster with a person, lower monster count
						if j.__class__.__name__ <> "HersheyKiss":
							j.setUses(j.getUses() - 1) #decrement uses if not a HersheyKiss
			for i in house.getMonsters(): #monsters' turn, allow them to attack once per monster
				newHP = player.getHp() - i.getAttack()
				player.setHp(newHP) #monsters attack, sets lower hp
		self.display_map(player) #display map again

	"""
	When a monster dies, it notifies the Neighborhood to decrement the amount of total monsters it contains, 
	also tracks how many monsters are defeated
	"""
	def update(self):
		Neighborhood.total_monsters = Neighborhood.total_monsters - 1
		Neighborhood.monsters_defeated = Neighborhood.monsters_defeated + 1

if __name__ == "__main__":
	p = Player()
	n = Neighborhood(2,5) #set grid size
	n.display_map(p) #start game
