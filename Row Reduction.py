import sympy as sy
import numpy as np
from numpy.random import randint
from sympy import pprint
import os




print("Welcome to the endless row reducer!")

def clear():
	if windows:
		os.system("cls")
	else:
		os.system("clear")


def randomvalue(difficulty):
	root = randint(-5, 5)

	chance = randint(16)

	if(chance < difficulty):
		root = sy.Rational(root, randint(2, 5))

	return root

def generateRow(size, pos, difficulty):
	row = []

	for i in range(1, size):
		if i == pos:
			row.append(1)
		else:
			row.append(0)
		
	row.append(randomvalue(difficulty))
	row = sy.Matrix([row])
	return row

def randomize(matrix, size, difficulty):


	#randomize by adding a random scalar of one row to another
	#technically it deletes the row then inserts it, but the results are effectively the same
	for i in range(0, difficulty * 3):
		#eliminate the addition of the same equation twice because its causing issues
		roll = 6

		if roll != 5:
			source = randint(0, size - 1)
			dest = randint(0, size - 1 )

			while dest == source:
				dest = randint(0, size - 1)

			sourcerow = matrix.row(source)

			#add random scalar multiple of one row to another
			destrow = matrix.row(dest) + (matrix.row(source) * randint(-size, size))

			matrix.row_del(dest)

			matrix = matrix.row_insert(0, destrow)

		else:
			#grab a random row, multiply it by a scalar and insert (not add) it to the matrix
			source = randint(0, size - 1)

			matrix = matrix.row_insert(0, (matrix.row(source) * randint(-size * 3, size * 3)))


	return matrix

def getDifficulty():
	while True:
		difficulty = input("Choose your selection:")

		try:
			difficulty = int(difficulty)
		except:
			print("ENTER AN INTEGER, FOOL!")
			continue
		break
	return difficulty


#determine the os
windows = False
if os.name == 'nt':
	windows = True

#program loop
while True:
	clear()
	print("Choose a difficulty:\n 1.Management\n 2.Arts\n 3.Honours Math/CS \n 4.Wang\n 5.Kelome's Multiple Choice\n 6+.Kicking a wall with a toothpick under your toenail\n")
	

	difficulty = getDifficulty()

	size = difficulty + 2


	A = sy.Matrix()
	

	for i in range(1, size):
		chance = 2

		if chance == 2:
			row = generateRow(size, i, difficulty)
		else:
			row = row * randomvalue(difficulty)
			print("unnh?")

		A = A.row_insert(0, row)


	#randomize the matrix
	A = randomize(A, size, difficulty)
	clear()


	print("SOLVE!")
	pprint(A)

	input("When there is \"No Hope,\" press any key to see how off you were")


	print("\nYOU FOOL!\nThe right answer was:")

	
	pprint(A.rref())

	a = input("Can you continue? Y/N\n")

	if a == 'n' or a == 'N':
		exit()
	else:
		continue
