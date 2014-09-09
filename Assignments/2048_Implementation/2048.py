import random

def start():
	print '--------------------------------\n            2048\n--------------------------------'
	grid = []
	board(grid)
	move(grid)

def move(grid):
	move = raw_input('Left, right, up, or down? Use the arrow keys! ')
	if move == '\x1b[A':
		boardMove('up', grid)
	elif move == '\x1b[B':
		boardMove('down', grid)
	elif move == '\x1b[C':
		boardMove('right', grid)
	elif move == '\x1b[D':
		boardMove('left', grid)
	elif move == 'q':
		return
	else:
		print "That's not a valid move"
		return move()

def boardMove(direction, grid):
	print direction
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






	if direction == 'left':
		for row in range(3):
			for column in range(3):
				if grid[row][column]!=0 or grid[row][column+1]!=0 or grid[row][column+2]!=0 or grid[row][column+3]!=0:
					grid[row
				elif grid[row][column+1] == grid[row][column]:
					grid[row][column] = grid[row][column]*2
					grid[row][column+1] = 0
				else:
					grid[row][column] = grid[row][column+1]
	printGrid(grid)
	return move(grid)

def board(grid):
	for row in range(4):
		grid.append([])
		for column in range(4):
			grid[row].append(0)
	x = random.randint(0,3)
	y = random.randint(0,3)
	grid[x][y] = 2
	grid[y][x] = 2
	printGrid(grid)
	return grid

def printGrid(grid):
	for row in range(4):
		print grid[row]

if __name__ == '__main__':
	start()
