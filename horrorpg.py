from __future__ import print_function #allows input() function for earlier python versions
import random #for the chance aspect of the game
#for the Observer Pattern
from observer import Observer
from observable import Observable
from weapons import *
from combatants import *
from locations import *
"""**********************************************************
Creates an RPG where a player goes through a neighborhood 
saving people from monsters. The game ends when a person is 
out of hp or if all the monsters are people again.

Sources: 
	Observer Pattern code from Professor Woodring
	Input Scanner/'from __future__' import and
		__class__.__name__ from Stack Overflow

@author Dane Bramble
@version March 16, 2018

*************************************************************"""

#The main character fighting to save his/her neighborhood
class Player:
	"""**********************************
	A class to store Player information
	**********************************"""
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

	"""*************************************************
	get/set methods to return/set values of the player
	*************************************************"""

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

	"""************************************************
	@param width = the width of the Neighborhood grid
	@param height = the height of the Neighborhood grid
	************************************************"""
	def setLocation(self, width, height):
		self.location = [width, height]


#The Collection of houses the player must move through to kill the monsters. Houses the game's rules
class Neighborhood(Observer):
	"""***************************************************************************
	A class to store Neighborhood information, print function and the Game's Rules
	******************************************************************************"""

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

	"""***********************************************************************
	Displays Neighborhood map on terminal, allows Player to move to any house
	@param player the player moving through the neighborhood 
	***********************************************************************"""

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


	"""********************************************************************
	Turn based fighting of the game, Player uses all weapons on all enemies, 
		then all the the monsters/people fight/heal Player
	@param player the Player that is fighting the monsters
	@param house the Home in which the monsters reside
	***********************************************************************"""
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

	"""****************************************************************************************************
	When a monster dies, it notifies the Neighborhood to decrement the amount of total monsters it contains, 
	also tracks how many monsters are defeated
	*******************************************************************************************************"""
	def update(self):
		Neighborhood.total_monsters = Neighborhood.total_monsters - 1
		Neighborhood.monsters_defeated = Neighborhood.monsters_defeated + 1

if __name__ == "__main__":
	p = Player()
	n = Neighborhood(5,5) #set grid size
	n.display_map(p) #start game
