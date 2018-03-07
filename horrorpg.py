import random

class HersheyKiss:
	"""A class to store HersheyKiss information"""
	def __init__(self):
		self.mod = 1
		self.uses = 1000

class SourStraw:
	"""A class to store SourStraw information"""
	def __init__(self):
		self.mod = random.uniform(1.0, 1.75)
		self.uses = 2

class ChocolateBar:
	"""A class to store ChocolateBar information"""
	def __init__(self):
		self.mod = random.uniform(2.0, 2.4)
		self.uses = 4

class NerdBomb:	
	"""A class to store NerdBomb information"""
	def __init__(self):
		self.mod = random.uniform(3.5, 5)
		self.uses = 1

class Player:
	"""A class to store Player information"""
	def __init__(self):
		self.hp = random.randint(100, 126)
		self.attack_val = random.randint(10, 21)
		self.weapons = []
		while len(self.weapons) < 10:
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
class Person:
	"""A class to store Person information"""
	def __init__(self):
		self.hp = 100
		self.attack_val = -1

class Zombie:
	"""A class to store Zombie information"""
	def __init__(self):
		self.hp = random.randint(50,101)
		self.attack_val = random.randint(0,11)

class Vampire:
	"""A class to store Vampire information"""
	def __init__(self):
		self.hp = random.randint(100,201)
		self.attack_val = random.randint(10,21)

class Ghoul:
	"""A class to store Ghoul information"""
	def __init__(self):
		self.hp = random.randint(40,81)
		self.attack_val = random.randint(15,31)

class Werewolf:
	"""A class to store Werewolf information"""
	def __init__(self):
		self.hp = 200
		self.attack_val = random.randint(0,41)

class Home:
	"""A class to store Home information"""
	def __init__(self):
		self.monsters = []
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
		self.num_monsters = len(self.monsters)

class Neighborhood:
	"""A class to store Neighborhood information"""
	total_monsters = 0
	def __init__(self, height, width):
		if (height > 0 and width > 0):
			self.height = height
			self.width = width
			self.grid = []
			for i in range(width):
				self.grid.append([])
				for j in range(height):
					h = Home()
					self.grid[i].append(h)
					Neighborhood.total_monsters = Neighborhood.total_monsters + h.num_monsters
					

	def quest_time(self, player):
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				if player.hp > 0 and Neighborhood.total_monsters > 0:
					self.fightin_time(player, self.grid[i][j])
				if Neighborhood.total_monsters < 1:
					print('The neighborhood is saved!')
					return
				elif player.hp < 1:
					print("The Monsters have won...")
					return

	def fightin_time(self, player, house):
		while house.num_monsters > 0 and player.hp > 0:
			index = 0
			for i in house.monsters:
				for j in player.weapons:
					if j.uses > 0 and i.hp > 0:
						attack = player.attack_val * j.mod
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
						i.hp = i.hp - attack
						if i.hp <= 0:
							house.monsters[index] = Person()
							house.num_monsters = house.num_monsters - 1
							Neighborhood.total_monsters = Neighborhood.total_monsters - 1
						if j.__class__.__name__ <> "HersheyKiss":
							j.uses = j.uses - 1
				index = index + 1
			for i in house.monsters:
				player.hp = player.hp - i.attack_val

def main():
	p = Player()
	n = Neighborhood(5,5)
	n.quest_time(p)
main()

