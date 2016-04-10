from qTTT import *

class GameTree:		# views the game as a game tree
	def __init__(self):
		self.rootnode = GameNode()


class GameNode:	# class for an abstract node: has a board as its status etc.
	def __init__(self, l):	# should only be used for first initialization of game
		self.board = Board()
		self.parent = None
		self.originmovecode = None
		self.letter = l				# letter of current turn's player
		movecodes = self.board.getListOfMovecodes(None, self.letter, 0)
		self.children = [[mc, None] for mc in movecodes]	# construct list of possible children. 'None' means that there are no children actually constructed yet
		
		
	def __init__(self, b, np, omc, l):	# standard constructor for inserting new leaf in tree
		self.board = b				# board belonging to this
		self.parent = np			# this board's parent node
		self.originmovecode = omc		# move code resulting in this node's board
		self.letter = l							# letter of curent turn's player
		if self.originmovecode:
			smp = self.originmovecode.spookyMarkPars
			lastMark = SpookyMark(smp)
		else:
			lastMark = None
		movecodes = self.board.getListOfMovecodes(lastMark, self.letter, 0)
		self.children = [[mc, None] for mc in movecodes]	# construct list of possible children. 'None' means that there are no children actually constructed yet
		
