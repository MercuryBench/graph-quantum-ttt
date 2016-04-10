from qTTT import *
from qTTT_game_util import *
from qTTT_graph import *
import random

while(True): # loop for games
	#mode = getGameMode()
	mode = "pvp"
	if mode == "pvp":
		print("You're playing against a human opponent")
	else:
		print("You're playing against the computer")
	turn = whoGoesFirst()
	if mode == "pvp":
		print('Player ' + str(turn) + ' will go first.')	# global assumption: X always starts
		if turn == 1:
			playerLetter, player2letter = "X", "O" #inputPlayerLetter()
		else:
			playerLetter, player2letter = "O", "X" #inputPlayerLetter()
	else:
		if turn == 1:
			print('You will go first!')
			playerLetter, player2letter = "X", "O" #inputPlayerLetter()
		else:
			print('The computer will go first')
			playerLetter, player2letter = "O", "X" #inputPlayerLetter()
	
	# INITIALIZE TREE AND BOARD HERE
	#####################################################
	# define: board (as the root of the tree)
	node = GameNode(Board(), None, None, 'X')
	lastMark = None
	numMark = 0
	

	while (True): # loop for turns
		if turn == 1:
			print("It's player 1's turn. Place your mark (" + playerLetter + ")")
			board = node.board
			board.printBoard()
			turnboard = board.copy()
			cp = None # collapsepars yet to be defined
			sp = None # spooky mark pars yet to be defined

			# Check whether there is entanglement after player 2's move
			if lastMark:
				if turnboard.findCycle(lastMark.pos):
					col = getPlayerCollapse(turnboard, lastMark) # let player 1 decide where to put the last mark
					cp = CollapsePars([lastMark.letter, lastMark.num, col[0], col[1]])
					turnboard.collapse(cp)
					turnboard.printBoard()
	  
			# look at winning conditions:
			p1won, p1lms = turnboard.hasWon(playerLetter)
			p2won, p2lms = turnboard.hasWon(player2letter)
			if p1won:
				if p2won:
					if p1lms < p2lms:
						print("\n")
						turnboard.printBoard()
						print("Player 1 (" + playerLetter + ") has won the game!")
						break
					else:
						print("\n")
						turnboard.printBoard()
						if mode == "pvp":
							print("Player 2 (" + player2letter + ") has won the game")
						else:
							print("The computer (" + player2letter + ") has won the game!")
						
						break	   			
				else:
					print("\n")
					turnboard.printBoard()
					print("Player 1 (" + playerLetter + ") has won the game!")
					break
			elif p2won:
				print("\n")
				turnboard.printBoard()
				if mode == "pvp":
					print("Player 2 (" + player2letter + ") has won the game")
				else:
					print("The computer (" + player2letter + ") has won the game!")
				break
			else:
				if turnboard.isFull():
				  print("\n")
				  turnboard.printBoard()
				  print("The game is a tie!")
				  break
		
			turn = 2
		   	# if the game hasn't ended, make a move
			pos1, pos2 = getPlayerMove(turnboard)
			sp = SpookyMarkPars([playerLetter, numMark, pos1, pos2])
		   
			lastMark = turnboard.addSpookyMark(sp)
			#print("How many recursions?")
			#rec = int(raw_input())

			mc = Movecode(cp, sp)		# this is the summary of all the player's decisions leading to turnboard, the local copy needed for visualization
			############## make the change in board by going over the game tree using mc
			newNode = GameNode(turnboard, node, mc, player2letter)
			for num, c in enumerate(node.children):
				if mc == c[0]:
					node.children[num][1] = newNode
					print(num)
			"""for num, mc_, _ in enumerate(node.children):
				if mc_.equals(mc):
					node.children[num] = newNode"""
			node = newNode	# reset pointer to current node 
			numMark += 1
		else:      	
			board = node.board
			if mode == "pvp":
				print("It's player 2's turn. Place your mark (" + player2letter + ")")
			else:
				print("It's the computer's turn")
			# Player 2's turn or computer.

			board.printBoard()

			if mode == "pvp":
				turnboard = board.copy()
				cp = None # collapsepars yet to be defined
				sp = None # spooky mark pars yet to be defined
				if lastMark:
					if turnboard.findCycle(lastMark.pos):
						col = getPlayerCollapse(turnboard, lastMark) # let player 1 decide where to put the last mark
						cp = CollapsePars([lastMark.letter, lastMark.num, col[0], col[1]])
						turnboard.collapse(cp)
						turnboard.printBoard()
		  
				# look at winning conditions:
				p1won, p1lms = turnboard.hasWon(playerLetter)
				p2won, p2lms = turnboard.hasWon(player2letter)
				if p1won:
					if p2won:
						if p1lms < p2lms:
							print("\n")
							turnboard.printBoard()
							print("Player 1 has won the game!")
							break
						else:
							print("\n")
							turnboard.printBoard()
							print("The computer has won the game!")
							break	   			
					else:
						print("\n")
						turnboard.printBoard()
						print("Player 1 has won the game!")
						break
				elif p2won:
					print("\n")
					turnboard.printBoard()
					print("The computer has won the game!")
					break
				else:
					if turnboard.isFull():
					  print("\n")
					  turnboard.printBoard()
					  print("The game is a tie!")
					  break
		
				turn = 1
			   	# if the game hasn't ended, make a move
				pos1, pos2 = getPlayerMove(turnboard)
				sp = SpookyMarkPars([player2letter, numMark, pos1, pos2])
		   
				lastMark = turnboard.addSpookyMark(sp)
			   	mc = Movecode(cp, sp)		# this is the summary of all the player's decisions leading to turnboard, the local copy needed for visualization
				############## make the change in board by going over the game tree using mc
				newNode = GameNode(turnboard, node, mc, playerLetter)
				for num, c in enumerate(node.children):
					if mc == c[0]:
						node.children[num][1] = newNode
						print(num)
				"""for num, mc_, _ in enumerate(node.children):
					if mc_.equals(mc):
						node.children[num] = newNode"""
				node = newNode 	# reset pointer to current node 
				###### MAKE THE CHANGE!!
				numMark += 1
			else: # player vs. computer, and it's the computer's turn
				print("blah")
	if not playAgain():
		break

