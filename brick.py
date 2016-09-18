import sys, pygame

class Brick:
	"A brick class for our brick breaker game"
	brick_count = 0

	def __init__(self, x, y, isHit):
		self.x = x
		self.y = y
		self.isHit = isHit
		self.text = ""
		Brick.brick_count+=1

class Player:
	"A class to represent the player's paddle"
	def __init__(self, x, y, lives):
		self.x = x
		self.y = y
		self.lives = lives

    	