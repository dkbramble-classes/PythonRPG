import random
#Classes of weapons that the player can use
class HersheyKiss:
	"""Attack Multiplier and Uses for HersheyKiss"""
	def __init__(self):
		self.mod = 1
		self.uses = 1000

	def getMod(self):
		return self.mod

	def getUses(self):
		return self.uses

	def setUses(self, value):
		self.uses = value

class SourStraw:
	"""Attack Multiplier and Uses for SourStraw"""
	def __init__(self):
		self.mod = random.uniform(1.0, 1.75)
		self.uses = 10 # was 2

	def getMod(self):
		return self.mod

	def getUses(self):
		return self.uses

	def setUses(self, value):
		self.uses = value

class ChocolateBar:
	"""Attack Multiplier and Uses for ChocolateBar"""
	def __init__(self):
		self.mod = random.uniform(2.0, 2.4)
		self.uses = 12 # was 4

	def getMod(self):
		return self.mod

	def getUses(self):
		return self.uses

	def setUses(self, value):
		self.uses = value

class NerdBomb:	
	"""Attack Multiplier and Uses for NerdBomb"""
	def __init__(self):
		self.mod = random.uniform(3.5, 5)
		self.uses = 5 # was 1

	def getMod(self):
		return self.mod

	def getUses(self):
		return self.uses

	def setUses(self, value):
		self.uses = value

#The main character fighting to save his/her neighborhood
class Player:
	"""A class to store Player information"""
	def __init__(self):
		self.hp = random.randint(100, 126) #hit points for the player
		self.attack_val = random.randint(10, 21) #default hit points without weapon multiplier
		self.weapons = [] #list of weapons you have
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

	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val

	def getWeapons(self):
		return self.weapons

#Classes of NPC's that will fight or help the player
class Person:
	"""Hit Points and Attack Value for the Person NPC"""
	def __init__(self):
		self.hp = 100
		self.attack_val = -1

	def getHp(self):
		return self.hp

	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val

class Zombie:
	"""Hit Points and Attack Value for the Zombie NPC"""
	def __init__(self):
		self.hp = random.randint(50,101)
		self.attack_val = random.randint(0,11)

	def getHp(self):
		return self.hp

	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val

class Vampire:
	"""Hit Points and Attack Value for the Vampire NPC"""
	def __init__(self):
		self.hp = random.randint(100,201)
		self.attack_val = random.randint(10,21)

	def getHp(self):
		return self.hp

	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val

class Ghoul:
	"""Hit Points and Attack Value for the Ghoul NPC"""
	def __init__(self):
		self.hp = random.randint(40,81)
		self.attack_val = random.randint(15,31)

	def getHp(self):
		return self.hp

	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val

class Werewolf:
	"""Hit Points and Attack Value for the Person NPC"""
	def __init__(self):
		self.hp = 200
		self.attack_val = random.randint(0,41)

	def getHp(self):
		return self.hp

	def setHp(self, value):
		self.hp = value

	def getAttack(self):
		return self.attack_val

#A Class for Homes that can be filled with monsters to fight
class Home:
	"""A class to store Home information"""
	def __init__(self):
		self.monsters = []
		#Populate the Home with 0-4 random monsters
		while len(self.monsters) < random.randint(0, 11):
			rand = random.randint(1,5)
			if rand == 1:
				w = Zombie()
				self.monsters.append(w)
			elif rand == 2:
				w = Vampire()
				self.monsters.append(w)
			elif rand == 3:
				w = Ghoul() 
				self.monsters.append(w)
			elif rand == 4:
				w = Werewolf()
				self.monsters.append(w)
		#number of monsters in this specific home
		self.num_monsters = len(self.monsters)

	def getMonsters(self):
		return self.monsters

	def setMonsters(self, index, value):
		self.monsters[index] = value

	def getNumMonsters(self):
		return self.num_monsters

	def setNumMonsters(self, value):
		self.num_monsters = value

#The Collection of houses the player must move through to kill the monsters
class Neighborhood:
	"""A class to store Neighborhood information and the Game's Rules"""
	total_monsters = 0 #The grand total of all the monsters from all homes
	def __init__(self, height, width):
		if (height > 0 and width > 0): #Set the width and height of the grid in which the homes will reside
			self.height = height
			self.width = width
			self.grid = []
			for i in range(width): #populate the grid with homes
				self.grid.append([])
				for j in range(height):
					h = Home()
					self.grid[i].append(h)
					Neighborhood.total_monsters = Neighborhood.total_monsters + h.getNumMonsters() #increment total number of monsters
		else:
			print("A Neighborhood can't be that size!")
			self.grid = []

	def quest_time(self, player): #Moving through the Neighborhood to each home
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				if player.getHp() > 0 and Neighborhood.total_monsters > 0:
					self.fightin_time(player, self.grid[i][j]) #Start turn based combat in one house
				if Neighborhood.total_monsters < 1:
					print('The Neighborhood is saved!') #No more monsters!
					return
				elif player.getHp() < 1:
					print("The Monsters have won...") #You've been beaten
					return

	def fightin_time(self, player, house):
		while house.getNumMonsters() > 0 and player.getHp() > 0: #Keep fighting until you or the monsters win
			index = 0
			for i in house.getMonsters():
				for j in player.getWeapons():
					if j.getUses() > 0 and i.getHp() > 0:
						attack = player.getAttack() * j.getMod() #sets amount you will hurt monsters
						#Rules for what hurts which monsters and how badly
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
						i.setHp(i.getHp() - attack)
						if i.getHp() <= 0: #if the monster dies, turn into a Person
							house.setMonsters(index, Person())
							house.setNumMonsters(house.getNumMonsters() - 1) #one less monster
							Neighborhood.total_monsters = Neighborhood.total_monsters - 1 #one less monster
						if j.__class__.__name__ <> "HersheyKiss":
							j.setUses(j.getUses() - 1) #decrement uses if not a HersheyKiss
				index = index + 1 #helps determine place in list of monsters
			for i in house.getMonsters(): #monsters' turn, allow them to attack once per monster
				newHP = player.getHp() - i.getAttack()
				player.setHp(newHP)

def main():
	p = Player()
	n = Neighborhood(5,2)
	n.quest_time(p)
main()

