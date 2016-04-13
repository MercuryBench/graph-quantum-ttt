from qTTT_graph import *
from qTTT_MCTS import *
import math

param = 1/math.sqrt(2)
param = 1
computerletter = 'X'
playerletter = 'O'

node = GameNode(Board(), None, None, 'X', 'O')
rootnode = node
"""
for n in range(100):
		newNode = treepolicy(rootnode, param)
		delta = defaultpolicy(newNode, rootnode.letter, rootnode.notletter)
		backup(newNode, delta)
"""

#mc = uctsearch(node, 1, 1/math.sqrt(2))
"""

param = 1/math.sqrt(2)
computerletter = 'X'
playerletter = 'O'

rootnode = node

mc = uctsearch(node, 10, 1/math.sqrt(2))
tmpboard = node.board.copy()
tmpboard.makeMove(mc)
tmpnode = GameNode(tmpboard, node, mc, node.notletter, node.letter)
node = tmpnode
node.board.printBoard()
"""


# Zwickmuehlensetup:
smp0 = SpookyMarkPars(['X', 0, 7, 5])
cmp1 = ClassicalMarkPars(['O', 1, 4])
cmp2 = ClassicalMarkPars(['X', 2, 8])
cmp3 = ClassicalMarkPars(['O', 3, 2])
cmp4 = ClassicalMarkPars(['X', 4, 1])
cmp5 = ClassicalMarkPars(['O', 5, 6])

smp6 = SpookyMarkPars(['X', 6, 3, 5])

mc0 = Movecode(None, smp0)
mc6 = Movecode(None, smp6)

board = rootnode.board.copy()
board.makeMove(mc0)
board.addClassicalMark(cmp1)
board.addClassicalMark(cmp2)
board.addClassicalMark(cmp3)
board.addClassicalMark(cmp4)
board.addClassicalMark(cmp5)
board.makeMove(mc6)

rootnode = GameNode(board, None, mc6, 'O', 'X')
rootnode.board.printBoard()
node = rootnode

for nn in range(1000):
		newNode = treepolicy(rootnode, param)
		delta = defaultpolicy(newNode, rootnode.letter, rootnode.notletter)
		backup(newNode, delta)

for n, c in enumerate(node.children):
	print(n)
	c[1].board.printBoard()
	print(c[0].toString())
	print(c[1].N)
	print(c[1].Q)
	print("----")

#mc = uctsearch(node, 10, 1/math.sqrt(2))
"""
"""
#newNode = treepolicy(node, param)
"""
for n in range(8):
		mc = random.choice(node.children)
		newBoard = node.board.copy()
		newBoard.makeMove(mc[0])
		newNode = GameNode(newBoard, node, mc[0], node.notletter, node.letter)
		node = newNode

counter = 0
for m in range(2000):
	node = tmpnode
	while not node.board.isTerminal():
		mc = random.choice(node.children)
		newBoard = node.board.copy()
		newBoard.makeMove(mc[0])
		newNode = GameNode(newBoard, node, mc[0], node.notletter, node.letter)
		node = newNode
		#node.board.printBoard()
	#node.board.printBoard()
	node.board.actualWinner(computerletter, playerletter)
	counter += node.board.actualWinner(computerletter, playerletter)

"""

"""
for n in range(1000):
		newNode = treepolicy(node, param)
		delta = defaultpolicy(newNode, node.letter, node.notletter)
		backup(newNode, delta)

delta = defaultpolicy(newNode, rootnode.letter, rootnode.notletter)

for n, c in enumerate(node.children):
	print(n)
	c[1].board.printBoard()
	print(c[1].N)
	print(c[1].Q)
	print("----")

mc = bestchild(node, param)[0]

newBoard = node.board.copy()
newBoard.makeMove(mc)
newNode = GameNode(newBoard, node, mc, node.notletter, node.letter)
node = newNode





mc = random.choice(node.children)
newBoard = node.board.copy()
newBoard.makeMove(mc[0])
newNode = GameNode(newBoard, node, mc[0], node.notletter, node.letter)
node = newNode

turnboard = node.board.copy()
mc = node.children[11][0]
turnboard.makeMove(mc)

newNode = GameNode(turnboard, node, mc, 'O', 'X')
for num, c in enumerate(node.children):
	if mc == c[0]:
		node.children[num][1] = newNode
		print(num)
node = newNode

"""
"""
b = Board()
b.addSpookyMark_('O', 1, 2, 4)
b.addSpookyMark_('O', 3, 2, 4)
omc = Movecode(None, SpookyMarkPars(['O', 3, 2, 4]))
b.printBoard()
node = GameNode(b, None, omc, 'X')"""
