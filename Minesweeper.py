# Minesweeper
# Thomas Lee
import math
import sys
import math
import numpy as np
import random as r
import pygame as py

coordState = 0
''' THE STATES OF A CELL
EMPTY = 0
MINE = 1
FLAG = 2
REVEALED = 99
'''
def initialize():
	def mineLocation(numberOfMines, rows, columns): #Creates a random string of 1's and 0's depending on how many mines the player wants
		veryLongList = []

		lengthOfRandomList = rows * columns 		#creates list of length row*column
		for i in range(0, lengthOfRandomList - 1):  #fills list with 0, the default state
			veryLongList[i] = 0
		for mine in range(numberOfMines):           #first few cells are filled with mines
			veryLongList[mine] = 1

		fieldArray = np.asarray(lengthOfRandomList) 
		r.shuffle(lengthOfRandomList)
		np.reshape(lengthOfRandomList, (rows, columns))
	

class Cell(object):
	def __init__(self, isMine, isFlag, isNotKnown, isNearMe):
		self.isMine = isMine                 # true or false
		self.isFlag = isFlag                 # true or false
		self.isRevealed = isRevealed         # true or false
		self.isNearMe = isNearMe             # integer between 0 and 8

	def isMine(coord):
		if coordState = 1:
			return True
		else:
			return False

	def isFlag(coord):
		if coordState = 2:
			return True
		else: 
			return False

	def isRevealed(coord):
		if coordState = 99:	
			return True
		else:
			return False

	def isNearMe(coord):
		for x in [-1, 0, 1]:
			for y in [-1, 0, 1]:

'''
So far we have...

-Made a random array consisting of mines
and empty cells with the initialize Function

-Defined the Cell object and its properties
that we will need to use

'''

class Player(object):
	def __init__(self, isSolved, isDead):
		self.isSolved = isSolved
		self.isDead = isDead

	def isDead(coordState):
		if self.isMine = True and self.isRevealed = True:
			return True
		else:
			returrn False

	def isSolved(fieldState):
		for cells in fieldState:

		
	

class Square(object):

	def isDead():

	def 
	
	



def Main():
		#initialize
		py.init
		screen = py.display.set_mode((250, 150))
		py.display.set_caption('Minesweeper')

		#set color
		background = py.Surface(screen.get_size())
		
			






	




