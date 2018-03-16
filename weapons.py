import random #for the chance aspect of the game
"""**********************************************************
Weapon Classes: 	
	Different Weapons Player can use:
		mod = attack multiplier to modify Player attack value
		uses = how many times a weapon can be used
@author Dane Bramble
@version March 16, 2018
*************************************************************"""
class HersheyKiss:
	"""***************************************
	Attack Multiplier and Uses for HersheyKiss
	******************************************"""

	def __init__(self):
		self.mod = 1
		self.uses = 1000 

	"""*************************************************
	get/set methods to return/set values of the weapon
	*************************************************"""
	def getMod(self):
		return self.mod

	def getUses(self):
		return self.uses

	#@param value = value to set weapon uses to
	def setUses(self, value):
		self.uses = value

class SourStraw:
	"""**************************************************
	Attack Multiplier, Uses, and Stock Uses for SourStraw
	**************************************************"""
	def __init__(self):
		self.mod = random.uniform(1.0, 1.75)
		self.uses = 10 # was 2
		self.stock_val = self.uses #amount of times default weapon can be used

	"""*************************************************
	get/set methods to return/set values of the weapon
	*************************************************"""

	def getMod(self):
		return self.mod

	def getUses(self):
		return self.uses

	def getStock(self):
		return self.stock_val

	#@param value = value to set weapon uses to
	def setUses(self, value):
		self.uses = value

class ChocolateBar:
	"""*****************************************************
	Attack Multiplier, Uses, and Stock Uses for ChocolateBar
	*****************************************************"""
	def __init__(self):
		self.mod = random.uniform(2.0, 2.4)
		self.uses = 12 # was 4
		self.stock_val = self.uses #amount of times default weapon can be used

	"""*************************************************
	get/set methods to return/set values of the weapon
	*************************************************"""

	def getMod(self):
		return self.mod

	def getUses(self):
		return self.uses

	def getStock(self):
		return self.stock_val

	#@param value = value to set weapon uses to
	def setUses(self, value):
		self.uses = value

class NerdBomb:	
	"""**************************************************
	Attack Multiplier, Uses, and Stock Uses for NerdBomb
	**************************************************"""
	def __init__(self):
		self.mod = random.uniform(3.5, 5)
		self.uses = 5 # was 1
		self.stock_val = self.uses #amount of times default weapon can be used

	"""*************************************************
	get/set methods to return/set values of the weapon
	*************************************************"""

	def getMod(self):
		return self.mod

	def getUses(self):
		return self.uses

	def getStock(self):
		return self.stock_val

	#@param value = value to set weapon uses to
	def setUses(self, value):
		self.uses = value