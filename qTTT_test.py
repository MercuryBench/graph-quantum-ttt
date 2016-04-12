from qTTT_graph import *
from qTTT_MCTS import *
import math

param = 1/math.sqrt(2)
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
smp1 = SpookyMarkPars(['X', 0, 1, 5])
smp2 = SpookyMarkPars(['O', 1, 7, 8])
smp3 = SpookyMarkPars(['X', 2, 9, 5])

mc1 = Movecode(None, smp1)
mc2 = Movecode(None, smp2)
mc3 = Movecode(None, smp3)

board = rootnode.board.copy()
board.makeMove(mc1)
board.makeMove(mc2)
board.makeMove(mc3)

rootnode = GameNode(board, None, mc3, 'O', 'X')
rootnode.board.printBoard()
node = rootnode
mc = uctsearch(node, 10, 1/math.sqrt(2))
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
