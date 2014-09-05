def start():
	print '--------------------------------\n            2048\n--------------------------------'
	board()
	move()

def move():
	move = raw_input('Left, right, up, or down?')
	if move == '\x1b[A':
		print 'up'
		boardMove('up')
	elif move == '\x1b[B':
		print 'down'
		boardMove('down')
	elif move == '\x1b[C':
		print 'right'
		boardMove('right')
	elif move == '\x1b[D':
		print 'left'
		boardMove('left')
	else:
		print "That's not a valid move"
		return move()

def boardMove(direction):
	return

def board():
	grid = []
	for row in range(4):
		grid.append([])
		for column in range(4):
			grid[row].append(0)
	return

if __name__ == '__main__':
	start()