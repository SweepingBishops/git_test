import tkinter
import random
import time
from plantMines import plantMines, identifyNeighbouringSquares
from functools import partial

###Global variables###
firstClickFlag = True
bIdentity , minePositions , squareValues = {}, {}, {}

def main():
	def onClick(i,j):
		global firstClickFlag, minePositions, squareValues

		button = bIdentity[(i,j)]	#stores the object at (i,j) into local variable button
		button['state'] = 'disabled'	#so that the same button can't be clicked multiple times

		if firstClickFlag:
			minePositions, squareValues = plantMines(i,j,gridSize,mineCount)	#the mines are planted at the first click
			firstClickFlag = False

		if (i,j) not in minePositions:	#if clicked square does not contain mine it is coloured green
			tkinter.Label(mainWindow,text= squareValues[(i,j)],bg='green', height = 2, width = 4).grid(row=i,column=j)
		else:				#if the square contains a mine it is coloured red and the game exits
			tkinter.Label(mainWindow,text= str(i) +','+ str(j),bg='red', height = 2, width = 4).grid(row=i,column=j)
			print('You lost:(')
			mainWindow.after(2000,func=exit)
			
		if squareValues[(i,j)] == None:		#opens neighbouring squares if current squareValue is 0 (game rule)
			neighbouringSquares = identifyNeighbouringSquares(i, j, gridSize)
			for neighbouringSquare in neighbouringSquares:
				bIdentity[neighbouringSquare].invoke()


	gridSize = int(input('Enter grid size: '))
	mineCount = int(input('Enter number of mines: '))

	#creating main screen
	mainWindow = tkinter.Tk(className='Minesweeper')
	mainWindow.option_add('*Font','22')
	
	for i in range(gridSize):
		for j in range(gridSize):
			#creates and sets the buttons onto the window
			button = tkinter.Button(mainWindow, text= f'{str(i)},{str(j)}', command = partial(onClick,i,j) , height = 2, width = 4)
			button.grid(row=i,column=j)
			
			bIdentity[(i,j)] = button	#adds the object into the dictionary so that it can be used later
			
	mainWindow.mainloop()

if __name__ == '__main__':
	main()
