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
		
		numberOfMines = input int("Enter Number of Mines")
		rows = input int("Enter Number of Rows")
		columns = input int("Enter Number of columns")

		veryLongList = []

		lengthOfRandomList = rows * columns 		#creates list of length row*column
		for i in range(0, lengthOfRandomList - 1):  #fills list with 0, the default state
			veryLongList[i] = 0
		for mine in range(numberOfMines):           #first few cells are filled with mines
			veryLongList[mine] = 1

		fieldArray = np.asarray(lengthOfRandomList) 
		r.shuffle(fieldArray)
		np.reshape(fieldArray, (rows, columns))

class Cell(object):
	def __init__(self, isMine, isFlag, isNotKnown, isNearMe):
		self.isMine = isMine                 # true or false
		self.isFlag = isFlag                 # true or false
		self.isRevealed = isRevealed         # true or false
		self.isNearMe = isNearMe             # integer between 0 and 8

	def isMine(coord):
		if coordState == 1:
			return True
		else:
			return False

	def isFlag(coord):
		if coordState == 2:
			return True
		else: 
			return False

	def isRevealed(coord):
		if coordState == 99:
			return True
		else:
			return False

	def isNearMe(coord): #Coord is [Xpos, Ypos]
	
		Xpos = coord[0]
		Ypos = coord[1]

		mineIncrement = 0

		if Xpos == 0 and Ypos == 0: #Top Left
			for x in [ 0 , 1 ]: 
				for y in [ 0 , 1 ]:	# 00 01 10 11
					newCoord = [ Xpos + x, Ypos + y ]
					
					if isMine(newCoord) == True:
						mineIncrement += 1
					else:
						mineIncrement += 0
				return mineIncrement     #Finished


		if Xpos == 0 and Ypos == rows: #Bottom Left
			for x in [ 0 , 1 ]:
				for y in [ -1 , 0 ]:   # 0-1 00 1-1 10
					newCoord = [ Xpos + x, Ypos + y ]

					if isMine(newCoord) = True:
						mineIncrement += 1
				 	else:
				 		mineIncrement += 0
				return mineIncrement #finished


		if Xpos == columns and Ypos == 0: #Top Right
			for x in [ -1 , 0 ]:
				for y in [ 0 , 1 ]:
					newCoord = [ Xpos + x, Ypos + y ]

					if isMine(newCoord) = true:
						mineIncrement += 1
					else:
						mineIncrement += 0
				return mineIncrement #finsished


		if Xpos == columns and Ypos == rows: #Bottom Right
			for x in [ -1 , 0 ]:
				for y in [ -1 , 0 ]:
					newCoord = [ Xpos + x, Ypos + y ]

					if isMine( newCoord ) = true:
						mineIncrement += 1
					else:
						mineIncrement += 0


		elif Xpos == 0 and (Ypos != 0 and Ypos != rows):
			for x in [ 0 , 1 ]:
				for y in [ -1 , 0 , 1 ]:
					newCoord = [ Xpos + x, Ypos + y ]

					if isMine( newCoord ) = true:
						mineIncrement += 1
					else:
						mineIncrement += 0


		if Xpos == columns and (Ypos != 0 and Ypos != rows):
			for x in [ -1 , 0 ]:
				for y in [ -1 , 0 , 1 ]:
					newCoord = [ Xpos + x, Ypos + y ]

					if isMine( newCoord ) = true:
						mineIncrement += 1
					else:
						mineIncrement += 0


		if (Xpos != 0 and Xpos != columns) and Ypos = 0:
				for x in [ -1 , 0 , 1 ]:
					for y in [ 0 , 1 ]:
						newCoord = [ Xpos + x, Ypos + y ]

					if isMine( newCoord ) = true:
						mineIncrement += 1
					else:
						mineIncrement += 0


		if (Xpos != 0 and Xpos != columns) and Ypos = rows:
			for x in [ -1 , 0 , 1 ]:
				for y in [ -1 , 0 ]:
					newCoord = [ Xpos + x, Ypos + y ]

					if isMine( newCoord ) = true:
						mineIncrement += 1
					else:
						mineIncrement += 0


		else:
			for x in [-1, 0, 1]:
				for y in [-1, 0, 1]:
					if isMine(newCoord) == true:
					
	

'''
So far we have... 

-Made a random array consisting of mines 
and empty cells with the initialize Function 

-Defined the Cell object and its properties 
that we will need to use 

'''

class MineField(object):

	def __init__(self, isSolved, isDead):
		self.isSolved = isSolved
		self.isDead = isDead
		self.x = Xloc
		self.y = Yloc
		self.minesLeft


	def isDead(coordState):
		if self.isMine = True and self.isRevealed = True:
			return True
		else:
			returrn False

	def isSolved(fieldState):
		for cells in 



def Main():
		#initialize
		py.init
		screen = py.display.set_mode((250, 150))
		py.display.set_caption('Minesweeper')

		#set color
		background = py.Surface(screen.get_size())
		
			






	




