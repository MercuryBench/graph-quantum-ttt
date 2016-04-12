import random


# Huge parts of this code are stolen from Al Sweigart's sample code for Tic Tac Toe implementation on
# https://inventwithpython.com/chapter10.html

class Movecode: # a compact representation of all possible moves in one turn
	def __init__(self, collPars, spookyPars):
		self.collapsePars = collPars
		self.spookyMarkPars = spookyPars
	def toString(self):
		s1 = ""
		s2 = ""
		if self.collapsePars:
			s1 = self.collapsePars.toString()
		else:
			s1 = "--"
		if self.spookyMarkPars:
			s2 = self.spookyMarkPars.toString()
		else:
			s2 = "--"
		return s1 + ", " + s2
	def __eq__(self, other):
		assert(isinstance(other, Movecode))
		return self.collapsePars == other.collapsePars and self.spookyMarkPars == other.spookyMarkPars
		
class CollapsePars: # a compact representation of all parameters of a collapse
	def __init__(self, collPars):
		self.letter = collPars[0]
		self.num = collPars[1]
		self.collapseAt = collPars[2]
		self.collapseNotAt = collPars[3]
	def twin(self): # returns parameters belonging to its twin collapse (with switched positions)
		return CollapsePars([self.letter, self.num, self.collapseNotAt, self.collapseAt])
	def toString(self):
		return self.letter + str(self.num) + str(self.collapseAt) + str(self.collapseNotAt)
	def __eq__(self, other):
		if other == None:
			return False
		assert(isinstance(other, CollapsePars))
		return (self.letter == other.letter and self.num == other.num and self.collapseAt == other.collapseAt and self.collapseNotAt == other.collapseNotAt)
		
class SpookyMarkPars: # a compact representation of all parameters of setting a spooky mark
	def __init__(self, spookyPars):
		self.letter = spookyPars[0]
		self.num = spookyPars[1]
		self.pos = spookyPars[2]
		self.otherpos = spookyPars[3]
	def twin(self): # returns parameters belonging to twin spooky mark
		return SpookyMarkPars([self.letter, self.num, self.otherpos, self.pos])
	def toString(self):
		return self.letter + str(self.num) + str(self.pos) + str(self.otherpos)
	def __eq__(self, other):
		if other == None:
			return False
		assert(isinstance(other, SpookyMarkPars))
		t = self.twin()
		ident = (self.letter == other.letter and self.num == other.num and self.pos == other.pos and self.otherpos == other.otherpos)
		ident2 = (t.letter == other.letter and t.num == other.num and t.pos == other.pos and t.otherpos == other.otherpos)
		return ident or ident2 # permutation is allowed
		
class ClassicalMarkPars:# a compact representation of all parameters of setting a classical mark
	def __init__(self, classyPars):
		self.letter = classyPars[0]
		self.num = classyPars[1]
		self.pos = classyPars[2]
		
# the following classes Field, SpookyMark and ClassicalMark are boring but contain a more compact description of the atomical objects Field, SpookyMark, ClassicalMark in the game
class Field: # is one of the 9 fields of the board, contains marks
	def __init__(self, num):
		self.contents = []
		self.num = num
		
	def copy(self):
		f = Field(self.num)
		for m in self.contents:
			f.contents.append(m.copy())
		return f
		
	def insertSpookyMark(self, pmark):
		if self.num != pmark.pos:
			print("Error: Wrong Mark position")
			return
		self.contents.append(pmark)
		
	def insertClassicalMark(self, fmark):
		if self.num != fmark.pos:
			print("Error: Wrong Final Mark position")
			return
		self.contents.append(fmark)
	
	def deleteSpookyMark(self, pmark):
		if pmark in self.contents:
			v.remove(pmark)
		else:
			print("Error: Pre Mark not in Field")
			
	def deleteSpookyMark_(self, letter, num):
		for m in self.contents:
			if isinstance(m, SpookyMark):
				if m.num == num and m.letter == letter:
					self.contents.remove(m)			
					
	def deleteClassicalMark_(self, letter, num):
		for m in self.contents:
			if isinstance(m, PreMark):
				if m.num == num and m.letter == letter:
					self.contents.remove(m)
	
	def deleteClassicalMark(self, fmark):
		if fmark in self.contents:
			self.contents.remove(fmark)
		else:
			print("Error: Final Mark not in Field")
			
	def fieldToString(self):
		for m in self.contents:
			if isinstance(m, ClassicalMark):
				return m.letter
		# so apparently there is no final mark
		s = ""
		for m in self.contents:
			s += (m.letter + str(m.num) + ", ")
		return s
			
class SpookyMark:
	def __init__(self, spookyMarkPars):
		self.letter = spookyMarkPars.letter
		self.num = spookyMarkPars.num
		self.pos = spookyMarkPars.pos
		self.otherpos = spookyMarkPars.otherpos
	def copy(self):
		pm = SpookyMark(SpookyMarkPars([self.letter, self.num, self.pos, self.otherpos]))
		return pm
		
class ClassicalMark:
	def __init__(self, classicalMarkPars):
		self.letter = classicalMarkPars.letter
		self.pos = classicalMarkPars.pos
		self.num = classicalMarkPars.num
	def copy(self):
		fm = ClassicalMark(ClassicalMarkPars([self.letter, self.num, self.pos]))
		return fm
		
class Board:
	def __init__(self): # Initialize Board with list of empty fields
		self.fields = [Field(n) for n in range(10)] # ignore index 0
		
	def copy(self): # make a (non-referential) copy of a board
		b = Board()
		b.fields = [f.copy() for f in self.fields]
		return b
	
	def addSpookyMark(self, spookyPars): # add a spooky mark with letter in {X,O} with its specific number at positions 1 and 2
		m1 = SpookyMark(spookyPars)
		self.fields[m1.pos].insertSpookyMark(m1)
		m2 = SpookyMark(spookyPars.twin())
		self.fields[m2.pos].insertSpookyMark(m2)
		return m2
		
	def addSpookyMark_(self, letter, num, pos, otherpos): # add a spooky mark with letter in {X,O} with its specific number at positions 1 and 2
		spookyPars1 = SpookyMarkPars([letter, num, pos, otherpos])
		spookyPars2 = SpookyMarkPars([letter, num, otherpos, pos])
		m1 = SpookyMark(spookyPars1)
		self.fields[m1.pos].insertSpookyMark(m1)
		m2 = SpookyMark(spookyPars2)
		self.fields[m2.pos].insertSpookyMark(m2)
		return m1
	
	def addClassicalMark(self, classyPars): # add a classical mark with letter in {X, O} at position pos
		c = ClassicalMark(classyPars)
		self.fields[c.pos].insertClassicalMark(c)
	
	def addClassicalMark_(self, letter, num, pos):
		c = ClassicalMark(ClassicalMarkPars([letter, num, pos]))
		self.fields[c.pos].insertClassicalMark(c)
		
	def hasWon(self, letter): # check whether the letter (in {X, O}) has won the game and return the lowest max subscript (see wikipedia rules for quantum TTT)
		bo, nb = self.realBoard()
		le = letter
		ttt = [False for n in range(8)]
		maxind = [0 for n in range(8)]
		ttt[0] 		= (bo[7] == le and bo[8] == le and bo[9] == le) # across the top
		maxind[0]	= max(nb[7], nb[8], nb[9])
		ttt[1] 		= (bo[4] == le and bo[5] == le and bo[6] == le) # across the middle
		maxind[1]	= max(nb[4], nb[5], nb[6])
		ttt[2] 		= (bo[1] == le and bo[2] == le and bo[3] == le) # across the bottom
		maxind[2]	= max(nb[1], nb[2], nb[3])
		ttt[3] 		= (bo[7] == le and bo[4] == le and bo[1] == le) # down the left side
		maxind[3]	= max(nb[7], nb[4], nb[1])
		ttt[4] 		= (bo[8] == le and bo[5] == le and bo[2] == le) # down the middle
		maxind[4]	= max(nb[8], nb[5], nb[2])
		ttt[5] 		= (bo[9] == le and bo[6] == le and bo[3] == le) # down the right side
		maxind[5]	= max(nb[9], nb[6], nb[3])
		ttt[6] 		= (bo[7] == le and bo[5] == le and bo[3] == le) # diagonal
		maxind[6]	= max(nb[7], nb[5], nb[3])
		ttt[7] 		= (bo[1] == le and bo[5] == le and bo[9] == le) # diagonal
		maxind[7]	= max(nb[1], nb[5], nb[9])
		
		winningEvent = False
		for t in ttt:
			if t:
				winningEvent = True
		if winningEvent:
			lowermaxsubscript = min([mi for mi, t in zip(maxind, ttt) if t])
		else: 
			lowermaxsubscript = -1 # failsafe option
		return winningEvent, lowermaxsubscript

	def actualWinner(self, letter, otherLetter): # +1 means, letter won, -1 means, otherLetter won, 0 is a tie
		we, lms = self.hasWon(letter)
		we2, lms2 = self.hasWon(otherLetter)

		if we:
			if we2:
				if lms < lms2:
					return 1
				else:
					return -1
			else:
				return 1
		elif we2:
			return -1
		else:
			return 0


	def realBoard(self): # returns only the "real" board, i.e. classical marks in any fields
		bo = [' '] * 10
		num = [' '] * 10
		for f in self.fields:
			for m in f.contents:
				if isinstance(m, ClassicalMark):		
					bo[f.num] = m.letter
					num[f.num] = m.num
		return bo, num
		
	def printBoard(self): # a crude representation of the board on screen
	    fs = self.fields
	    s7 = fs[7].fieldToString()
	    s8 = fs[8].fieldToString()
	    s9 = fs[9].fieldToString()

	    print("------------------------------------------")
	    print(s7+" "*(12-len(s7)) + "|" + s8 + " "*(12-len(s8)) +"|" + s9)
	    print("------------------------------------------")
	    s4 = fs[4].fieldToString()
	    s5 = fs[5].fieldToString()
	    s6 = fs[6].fieldToString()
	    print(s4+" "*(12-len(s4)) + "|" +s5 + " "*(12-len(s5)) +"|" + s6)
	    
	    print("------------------------------------------")
	    s1 = fs[1].fieldToString()
	    s2 = fs[2].fieldToString()
	    s3 = fs[3].fieldToString()
	    print(s1+" "*(12-len(s1)) + "|" +s2 + " "*(12-len(s2)) +"|" + s3)
	    
	    print("------------------------------------------")
			
	def isSpaceFree(self, pos):
		# Return true if the passed position pos is free on the board.
		board, num = self.realBoard()
		if str(pos) not in '1 2 3 4 5 6 7 8 9'.split(' '):
		  return False
		return board[pos] == ' '
	def isFull(self):
		# Return True if every space on the board has been taken. Otherwise return False.
		numFree = 0
		for i in range(1, 10):
			if self.isSpaceFree(i):
				numFree += 1
				if numFree >= 2:
					return False
		return True

	def isTerminal(self):	# careful: 'X' and 'O' are hard-coded here!
		return self.isFull() or self.hasWon('X')[0] or self.hasWon('O')[0]

	def makeMove(self, movecode):	# compact way of making all possible varieties of moves:
		# 1) only a normal move
		# 2) a collapse and a normal move
		# 3) only a collapse, after which the game ends
		collapse_code = movecode.collapsePars
		spooky_code = movecode.spookyMarkPars
		pm = None
		if collapse_code:
			self.collapse(collapse_code)
		if spooky_code:
			pm = self.addSpookyMark(spooky_code)
		return pm

	def getListOfMovecodes(self, lastMark, letter, num):
		collapseNecessary = False
		copyBoard = None
		listOfMoveCodes = []
		if not lastMark: # case no lastMark: first mark
			collapse_codes = None
			spooky_codes = []
			copyboard = self.copy()
			listFreePos = [pm for pm in range(1, 10) if copyboard.isSpaceFree(pm)]
			for m in range(len(listFreePos)):
				for n in range(m+1, len(listFreePos)):
					newSpookyCode = SpookyMarkPars([letter, num, listFreePos[m], listFreePos[n]])
					spooky_codes.append(newSpookyCode)
					listOfMoveCodes.append(Movecode(None, newSpookyCode))
		else:
			if (self.findCycle(lastMark.pos)):
				collapseNecessary = True
				collapse_codes = [CollapsePars([lastMark.letter, lastMark.num, lastMark.pos, lastMark.otherpos]), CollapsePars([lastMark.letter, lastMark.num, lastMark.otherpos, lastMark.pos])]
				spooky_codes = [[], []]
				copyBoard = [self.copy(), self.copy()]
				gameEnds = [False for cb in copyBoard]
			
				copyBoard[0].collapse(collapse_codes[0])
				gameEnds[0] = (copyBoard[0].hasWon(letter)[0] or copyBoard[0].hasWon(lastMark.letter)[0] or copyBoard[0].isFull())
			
				copyBoard[1].collapse(collapse_codes[1])
				gameEnds[1] = (copyBoard[1].hasWon(letter)[0] or copyBoard[1].hasWon(lastMark.letter)[0] or copyBoard[0].isFull())
			
				listFreePos = [[], []]
			
				if gameEnds[0]:
					spooky_codes[0] = []
					listOfMoveCodes.append(Movecode(collapse_codes[0], None))
				else:
					listFreePos[0] = [pm for pm in range(1, 10) if copyBoard[0].isSpaceFree(pm)]
					for m in range(len(listFreePos[0])):
						for n in range(m+1, len(listFreePos[0])):
							newSpookyCode = SpookyMarkPars([letter, num, listFreePos[0][m], listFreePos[0][n]])
							spooky_codes[0].append(newSpookyCode)
							listOfMoveCodes.append(Movecode(collapse_codes[0], newSpookyCode))
				if gameEnds[1]:
					spooky_codes[1] = []
					listOfMoveCodes.append(Movecode(collapse_codes[1], None))
				else:
					listFreePos[1] = [pm for pm in range(1, 10) if copyBoard[1].isSpaceFree(pm)]
					for m in range(len(listFreePos[1])):
						for n in range(m+1, len(listFreePos[1])):
							newSpookyCode = SpookyMarkPars([letter, num, listFreePos[1][m], listFreePos[1][n]])
							spooky_codes[1].append(newSpookyCode)
							listOfMoveCodes.append(Movecode(collapse_codes[1], newSpookyCode))
			else: # no cyclic entanglement, hence no collapse necessary
				copyBoard = self.copy()
				spooky_codes = []
				listFreePos = [pm for pm in range(1, 10) if copyBoard.isSpaceFree(pm)]
				for m in range(len(listFreePos)):
					for n in range(m+1, len(listFreePos)):
						newSpookyCode = SpookyMarkPars([letter, num, listFreePos[m], listFreePos[n]])
						spooky_codes.append(newSpookyCode)
						listOfMoveCodes.append(Movecode(None, newSpookyCode))
		return listOfMoveCodes

#	def getListOfMoves(self): # returns all possible moves
#		listOfMoves = []
#		for move in range(1, 10):
#			if self.isSpaceFree(move):
#				listOfMoves.append(move)
#		return listOfMoves

	def makeSteps(self, currentFieldNum, initialFieldNum):
		conts = self.fields[currentFieldNum].contents # all possible marks from the current position
		listOfNext = [c.copy() for c in conts]
		for m in listOfNext:
			if isinstance(m, ClassicalMark):
				continue
			nextNum = m.otherpos
			cboard = self.copy()
			# delete the current mark from the copied board in order to not to use this connection as a path later
			cboard.fields[currentFieldNum].deleteSpookyMark_(m.letter, m.num)
			cboard.fields[nextNum].deleteSpookyMark_(m.letter, m.num)
			# in case we found our way back, we return this mark
			if nextNum == initialFieldNum: 
				return m
			else: # if we didn't make it yet, we go one step deeper
				res = cboard.makeSteps(nextNum, initialFieldNum)
				if res: 
				  return res
				else: # if "one step deeper" runs into a dead end, we take the other option in the list above
				  continue

	# the following function is the most difficult one: It is used recursively to find a cycle in the maze of spooky marks in order to 
	# find out whether a collaps will take place
	
	def findCycle(self, markStartingFrom):		
		copyBoard = self.copy()
		m = copyBoard.makeSteps(markStartingFrom, markStartingFrom)
		return m
	
	# this function collapses the entanglement starting with markletter, marknum at position [collapseAt], which has its second pos as [collapseNotAt]
	def collapse(self, collapsePars):
		markletter = collapsePars.letter
		marknum = collapsePars.num
		collapseAt = collapsePars.collapseAt
		collapseNotAt = collapsePars.collapseNotAt
		
		currentField = self.fields[collapseAt]
		otherField = self.fields[collapseNotAt]
		
		currentField.deleteSpookyMark_(markletter, marknum)
		otherField.deleteSpookyMark_(markletter, marknum)
		
		listOfMarks = list(currentField.contents)
		currentField.insertClassicalMark(ClassicalMark(ClassicalMarkPars([markletter, marknum, collapseAt])))
		
		for markToBeReplaced in listOfMarks:
			m = markToBeReplaced
			if isinstance(m, ClassicalMark):
				continue
			self.collapse(CollapsePars([m.letter, m.num, m.otherpos, m.pos]))
	def collapse_(self, letter, num, collAt, collNotAt):
		self.collapse(CollapsePars([letter, num, collAt, collNotAt]))
