from qTTT import *

class GameTree:		# views the game as a game tree
	def __init__(self):
		self.rootnode = GameNode()


class GameNode:	# class for an abstract node: has a board as its status etc.
	def __init__(self, b, np, omc, l, lnot):	# standard constructor for inserting new leaf in tree
		self.board = b				# board belonging to this
		self.parent = np			# this board's parent node
		self.originmovecode = omc		# move code resulting in this node's board
		self.letter = l							# letter of curent turn's player
		self.notletter = lnot
		self.N = 0						# counts occurences
		self.Q = 0						# saves value of node
		if self.originmovecode:
			smp = self.originmovecode.spookyMarkPars
			if smp:
				lastMark = SpookyMark(smp)
				movecodes = self.board.getListOfMovecodes(lastMark, self.letter, lastMark.num+1)
			else:			# case only collapse, no move (hence win by one player or tie, so no move was possible)
				lastMark = None				
				movecodes = self.board.getListOfMovecodes(lastMark, self.letter, 0) # this should be empty
		else:
			lastMark = None
			movecodes = self.board.getListOfMovecodes(lastMark, self.letter, 0)
		if len(movecodes) > 0:
			self.children = [[mc, None] for mc in movecodes]	# construct list of possible children. 'None' means that there are no children actually constructed yet
			self.isTerminal = False
			if self.board.isTerminal():
				self.isTerminal = True
		else:
			self.children = []
			self.isTerminal = True

	def isExpanded(self):
		counter = 0
		for c in self.children:
			if c[1]:
				counter = counter + 1
		return counter == len(self.children)

	def createChildNode(self, mc):	# create a new node with movecode mc and saves it as a child 

		newBoard = self.board.copy()
		newBoard.makeMove(mc)
		newNode = GameNode(newBoard, self, mc, self.notletter, self.letter)
		for c in self.children:
			if c[0] == mc:
				c[1] = newNode
		return newNode
	
	def findWinningMove(self):	# see if there's a move such that player always wins (possibly after collapse)
		for c in self.children:
			copyboard = self.board.copy()
			copyboard.makeMove(c[0])
			copynode = GameNode(copyboard, self, c[0], self.notletter, self.letter)
			isWinningMove = True
			if copyboard.actualWinner(self.letter, self.notletter):
				return c[0]
			for cc in copynode.children:
				copyboard2 = copyboard.copy()
				copyboard2.makeMove(cc[0])
				res = copyboard2.actualWinner(self.letter, self.notletter)
				if res == 0 or res == -1:	# if there is just one alternative not leading to winning, return None
					isWinningMove = False
					break
			if isWinningMove:
				return c[0]
		return None


		
