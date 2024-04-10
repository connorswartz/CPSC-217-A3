# Assignment 3
# Connor Swartz
# UCID: 30055899
# Tutorial 05

import math
import random
import sys
import time

#End game with message function
def GO():
	print('GAME OVER')
	sys.exit()

#Command alternatives
ALTS = {
	'n': 'north',
	'e': 'east',
	's': 'south',
	'w': 'west',
	'q': 'quit',
}

#Dictionary for klingon locations and health
KLINGONS = {}

#List for klingon locations
klocations = []

#Enterprise energy
energy = 125

#Klingon hit chance variable
difficulty = 42

#Destruct variable
countdown = '12345'

#Universe location variables
x = 0
y = 0

#Number of stars
nstars = 10

#Number of kingons
nklingons = 4


#Start of referenced code given under 'Major spoilers' on Assignment 3
#Universe size
uheight = 9
uwidth = 12

#Objects in universe
enterprise = 'E'
klingon = 'K'
space = '.'
star = '*'

#Universe map
universe = []
for y in range(uheight):
	universe.append([space] * uwidth)

#Populate universe
for i in range(nstars):
	while True:
		x = random.randint(0, uwidth - 1)
		y = random.randint(0, uheight - 1)
		if universe[y][x] == space:
			break
	universe[y][x] = star

for i in range(nklingons):
	while True:
		x = random.randint(0, uwidth - 1)
		y = random.randint(0, uheight - 1)
		if universe[y][x] == space:
			break
	universe[y][x] = klingon
	KLINGONS[(x, y)] = 50
	klocations.append((x, y))

while True:
	x = random.randint(0, uwidth - 1)
	y = random.randint(0, uheight - 1)
	if universe[y][x] == space:
		break
universe[y][x] = enterprise
xent = x
yent = y
#End of referenced code


while True:

#Check number of klingons
	if nklingons == 0:
		print('All klingons have been destroyed. YOU WIN!')
		GO()

#Distance between enterprise and klingons/klingon shooting
	for i in range(nklingons):
		if klocations[i] == (xent, yent):
			klocations.pop(i)
		if (math.dist((xent, yent), klocations[i])) < 3:
			if random.randint(1, 100) <= difficulty:
				energy = energy - random.randint(5, 10)
				print('The klingon at', klocations[i], 'fired and hit.')

				#Check if game has been lost
				if energy <= 0:
					print('The Enterprise was destroyed. YOU LOSE.')
					GO()
				else:
					print('Remaining energy:', energy)
			else:
				print('The klingon at', klocations[i], 'fired and missed.')

#Print universe
	for y in range(int(len(universe))):
		for x in range(int(len(universe[y]))):
			print(universe[y][x], end=' ')
		print()

	line = input('Command:')

#Check for alternatives
	if line in ALTS:
		line = ALTS[line]

#Self-destruct
	elif line == 'destruct':
		print('The Enterprise will self-destruct in...')
		for i in range(-int(len(countdown)), 0):
			print(-i, '...')
			if str(-i) in countdown:
				time.sleep(1)
		print('The Enterprise has self-destructed.')
		GO()

#End game
	if line == 'quit':
		GO()

#Directions
	elif line == 'north':
		if yent - 1 < 0:
			print('You shall not pass!')
		elif universe[yent - 1][xent] == star:
			print('One does not simply fly through a star.')
		elif universe[yent - 1][xent] == klingon:
			KLINGONS[(xent, yent - 1)] = KLINGONS[(xent, yent - 1)] - random.randint(23, 28)
			if KLINGONS[(xent, yent - 1)] <= 0:
				print('Klingon destroyed!')
				nklingons = nklingons - 1
				universe[yent][xent] = space
				yent = yent - 1
				universe[yent][xent] = enterprise
		else:
			universe[yent][xent] = space
			yent = yent - 1
			universe[yent][xent] = enterprise

	elif line == 'east':
		if xent + 1 == uwidth:
			print('You shall not pass!')
		elif universe[yent][xent + 1] == star:
			print('One does not simply fly through a star.')
		elif universe[yent][xent + 1] == klingon:
			KLINGONS[(xent + 1, yent)] = KLINGONS[(xent + 1, yent)] - random.randint(23, 28)
			if KLINGONS[(xent + 1, yent)] <= 0:
				print('Klingon destroyed!')
				nklingons = nklingons - 1
				universe[yent][xent] = space
				xent = xent + 1
				universe[yent][xent] = enterprise
		else:
			universe[yent][xent] = space
			xent = xent + 1
			universe[yent][xent] = enterprise

	elif line == 'south':
		if yent + 1 == uheight:
			print('You shall not pass!')
		elif universe[yent + 1][xent] == star:
			print('One does not simply fly through a star.')
		elif universe[yent + 1][xent] == klingon:
			KLINGONS[(xent, yent + 1)] = KLINGONS[(xent, yent + 1)] - random.randint(23, 28)
			if KLINGONS[(xent, yent + 1)] <= 0:
				print('Klingon destroyed!')
				nklingons = nklingons - 1
				universe[yent][xent] = space
				yent = yent + 1
				universe[yent][xent] = enterprise
		else:
			universe[yent][xent] = space
			yent = yent + 1
			universe[yent][xent] = enterprise

	elif line == 'west':
		if xent - 1 < 0:
			print('You shall not pass!')
		elif universe[yent][xent - 1] == star:
			print('One does not simply fly through a star.')
		elif universe[yent][xent - 1] == klingon:
			KLINGONS[(xent - 1, yent)] = KLINGONS[(xent - 1, yent)] - random.randint(23, 28)
			if KLINGONS[(xent - 1, yent)] <= 0:
				print('Klingon destroyed!')
				nklingons = nklingons - 1
				universe[yent][xent] = space
				xent = xent - 1
				universe[yent][xent] = enterprise
		else:
			universe[yent][xent] = space
			xent = xent - 1
			universe[yent][xent] = enterprise

#Unknown commands
	else:
		print('Unknown Command.')
