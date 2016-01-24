import random

def getGameMode():
	print("Do you want to play against the computer or against another player? Enter (c/p)")
	inp = ''
	while inp not in ['c', 'C', 'p', 'P']:
		inp = raw_input()
	if inp == 'c' or inp == 'C':
		return 'pvc'
	else:
		return 'pvp'


def whoGoesFirst():
	# Randomly choose the player who goes first.
	if random.randint(0, 1) == 0:
		return 1
	else:
		return 2

def playAgain():
	# This function returns True if the player wants to play again, otherwise it returns False.
	print('Do you want to play again? (yes or no)')
	return raw_input().lower().startswith('y')

def getNumRecursions():
	val = ""
	while val not in "1 2 3 4 5 6 7 8 9 10".split(" "):
		print("How many recursions? (1-10)")
		val = raw_input()
	return int(val)

def getPlayerCollapse(board, lastMark):
    # Let the player type in their preferred collapse target
    print("You may collapse letter {0}{1} on field {2} or {3}".format(lastMark.letter, lastMark.num, lastMark.pos, lastMark.otherpos))
    choice = None
    while (not choice or choice not in [lastMark.pos, lastMark.otherpos]):
      print('What choice do you want to make? ({0}, {1})'.format(lastMark.pos, lastMark.otherpos))
      choice = int(raw_input())
    if choice == lastMark.pos:
      return choice, lastMark.otherpos
    else:
      return choice, lastMark.pos

def getPlayerMove(board):
	# Let the player type in their move.
	move = ' '
	move2 = ' '
	while ((move not in '1 2 3 4 5 6 7 8 9'.split() or move2 not in '1 2 3 4 5 6 7 8 9'.split()) and move == move2) or not board.isSpaceFree(int(move)) or not board.isSpaceFree(int(move2)):
		print('What is your next move? (1-9)')
		move = raw_input()
		print('Second field? (1-9)')
		move2 = raw_input()
	return int(move), int(move2)

def getComputerMove_Random(board):
	l = []
	for n in range(1, 10):
		if board.isSpaceFree(n):
			l.append(n)
			
	if len(l) > 1:
		r1 = random.choice(l)
		l.remove(r1)
		r2 = random.choice(l)
		return r1, r2
	else: 
		return None

def getComputerCollapse_Random(board, lastMark):
	l = [lastMark.pos, lastMark.otherpos]
	r = random.choice(l)
	l.remove(r)
	r2 = l[0]
	return r, r2
