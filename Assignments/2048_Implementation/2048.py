import random

def start():
	print '--------------------------------\n            2048\n--------------------------------'
	print 'Available commands:\nleft, right, up, down, quit, new'
	count = 0
	grid = []
	board(grid, count)
	move(grid, count)

def move(grid, count):
	move = raw_input('\n')
	if move == '\x1b[A' or move == 'up':
		randomPoint(grid, count)
		boardMove('up', grid, count)
	elif move == '\x1b[B' or move == 'down':
		randomPoint(grid, count)
		boardMove('down', grid, count)
	elif move == '\x1b[C' or move == 'right':
		randomPoint(grid, count)
		boardMove('right', grid, count)
	elif move == '\x1b[D' or move == 'left':
		randomPoint(grid, count)
		boardMove('left', grid, count)
	elif move == 'q' or move == 'quit':
		return
	elif move == 'n' or move == 'new':
		return start()
	else:
		print "That's not a valid move"
		return move(grid, count)

def boardMove(direction, grid, count):
	if direction == 'up':
		i = 0
		for j in range(0,4):
			if grid[i][j]!=0 or grid[i+1][j]!=0 or grid[i+2][j]!=0 or grid[i+3][j]!=0:
				if grid[i][j]==0:
					while grid[i][j]==0:
						grid[i][j]=grid[i+1][j]
						grid[i+1][j]=grid[i+2][j]
						grid[i+2][j]=grid[i+3][j]
						grid[i+3][j]=0
				if grid[i+1][j]==0 and (grid[i+2][j]!=0 or grid[i+3][j]!=0):
					while grid[i+2][j]==0:
						grid[i+2][j]=grid[i+3][j]
						grid[i+3][j]=0
		i = 0
		for j in range(0,4):
			if grid[i][j]==grid[i+1][j]:
				grid[i][j]=grid[i][j]+grid[i+1][j]
				grid[i+1][j]=grid[i+2][j]
				grid[i+2][j]=grid[i+3][j]
				grid[i+3][j]=0
			if grid[i+1][j]==grid[i+2][j]:
				grid[i+1][j]=grid[i+1][j]+grid[i+2][j]
				grid[i+2][j]=grid[i+3][j]
				grid[i+3][j]=0
			if grid[i+2][j]==grid[i+3][j]:
				grid[i+2][j]=grid[i+2][j]+grid[i+3][j]
				grid[i+3][j]=0
	elif direction == 'down':
		i = 0
		for j in range(0,4):
			if grid[i][j]!=0 or grid[i+1][j]!=0 or grid[i+2][j]!=0 or grid[i+3][j]!=0:
				if grid[i+3][j]==0:
					while grid[i+3][j]==0:
						grid[i+3][j]=grid[i+2][j]
						grid[i+2][j]=grid[i+1][j]
						grid[i+1][j]=grid[i][j]
						grid[i][j]=0
				if grid[i+2][j]==0 and (grid[i+1][j]!=0 or grid[i][j]!=0):
					while grid[i+2][j]==0:
						grid[i+2][j]=grid[i+1][j]
						grid[i+1][j]=grid[i][j]
						grid[i][j]=0
 
				if grid[i+1][j]==0 and grid[i][j]!=0:
					while grid[i+1][j]==0:
						grid[i+1][j]=grid[i][j]
						grid[i][j]=0
		i = 0
		for j in range(0,4):
			if grid[i+3][j]==grid[i+2][j]:
				grid[i+3][j]=grid[i+3][j] + grid[i+2][j]
				grid[i+2][j]=grid[i+1][j]
				grid[i+1][j]=grid[i][j]
				grid[i][j]=0
			if grid[i+2][j]==grid[i+1][j]:
				grid[i+2][j]=grid[i+2][j]+grid[i+1][j]
				grid[i+1][j]=grid[i][j]
				grid[i][j]=0
			if grid[i+1][j]==grid[i][j]:
				grid[i+1][j]=grid[i+1][j]+grid[i][j]
				grid[i][j]=0
	elif direction == 'left':
		j=0
		for i in range(0,4):
			if grid[i][j]!=0 or grid[i][j+1]!=0 or grid[i][j+2]!=0 or grid[i][j+3]!=0:
				if grid[i][j]==0:
					while grid[i][j]==0:
						grid[i][j]=grid[i][j+1]
						grid[i][j+1]=grid[i][j+2]
						grid[i][j+2] = grid[i][j+3]
						grid[i][j+3]=0
				if grid[i][j+1]==0 and (grid[i][j+2]!=0 or grid[i][j+3]!=0):
					while grid[i][j+1]==0:
						grid[i][j+1]=grid[i][j+2]
						grid[i][j+2]=grid[i][j+3]
						grid[i][j+3]=0
				if grid[i][j+2]==0 and (grid[i][j+3]!=0):
					while grid[i][j+2]==0:
						grid[i][j+2]=grid[i][j+3]
						grid[i][j+3]=0
		j = 0
		for i in range(0,4):
			if grid[i][j]==grid[i][j+1]:
				grid[i][j]=grid[i][j]+grid[i][j+1]
				grid[i][j+1]=grid[i][j+2]
				grid[i][j+2]=grid[i][j+3]
				grid[i][j+3]=0
			if grid[i][j+1]==grid[i][j+2]:
				grid[i][j+1]=grid[i][j+1]+grid[i][j+2]
				grid[i][j+2]=grid[i][j+3]
				grid[i][j+3]=0
			if grid[i][j+2]==grid[i][j+3]:
				grid[i][j+2]=grid[i][j+2]+grid[i][j+3]
				grid[i][j+3]=0
	elif direction == 'right':
		j=0
		for i in range(0,4):
			if grid[i][j]!=0 or grid[i][j+1]!=0 or grid[i][j+2]!=0 or grid[i][j+3]!=0:
				if grid[i][j+3]==0:
					while grid[i][j+3]==0:
						grid[i][j+3]=grid[i][j+2]
						grid[i][j+2]=grid[i][j+1]
						grid[i][j+1]=grid[i][j]
						grid[i][j]=0
				if grid[i][j+2]==0 and (grid[i][j+1]!=0 or grid[i][j]!=0):
					while grid[i][j+2]==0:
						grid[i][j+2]=grid[i][j+1]
						grid[i][j+1]=grid[i][j]
						grid[i][j]=0
				if grid[i][j+1]==0 and grid[i][j]!=0:
					while grid[i][j+1]==0:
						grid[i][j+1]=grid[i][j]
						grid[i][j]=0
		j = 0
		for i in range(0,4):
			if grid[i][j+3]==grid[i][j+2]:
				grid[i][j+3]=grid[i][j+3] + grid[i][j+2]
				grid[i][j+2]=grid[i][j+1]
				grid[i][j+1]=grid[i][j]
				grid[i][j]=0
			if grid[i][j+2]==grid[i][j+1]:
				grid[i][j+2]=grid[i][j+2]+grid[i][j+1]
				grid[i][j+1]=grid[i][j]
				grid[i][j]=0
			if grid[i][j+1]==grid[i][j]:
				grid[i][j+1]=grid[i][j+1]+grid[i][j]
				grid[i][j]=0
	printGrid(grid)
	return move(grid, count)

def board(grid, count):
	for row in range(4):
		grid.append([])
		for column in range(4):
			grid[row].append(0)
	x = random.randint(0,3)
	y = random.randint(0,3)
	grid[x][y] = 2
	randomPoint(grid, count)
	printGrid(grid)
	return grid

def randomPoint(grid, count):
	x = random.randint(0,3)
	y = random.randint(0,3)
	if grid[x][y] == 0:
		grid[x][y] = 2
	else:
		if count >= 100:
			return gameOver()
		else:
			count += 1
			return randomPoint(grid, count)

def printGrid(grid):
	for row in range(4):
		print grid[row]

def gameOver():
	print 'Game Over'
	return 'lol'

if __name__ == '__main__':
	start()
