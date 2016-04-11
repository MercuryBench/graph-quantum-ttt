from qTTT_graph import *
from qTTT_MCTS import *
import math

node = GameNode(Board(), None, None, 'X', 'O')


#mc = uctsearch(node, 1, 1/math.sqrt(2))

rootnode = node
newNode = treepolicy(node, 0.5)
"""
for n in range(5):
		mc = random.choice(node.children)
		newBoard = node.board.copy()
		newBoard.makeMove(mc[0])
		newNode = GameNode(newBoard, node, mc[0], node.notletter, node.letter)
		node = newNode"""

"""
turnboard = node.board.copy()
mc = node.children[12][0]
turnboard.makeMove(mc)
newNode = GameNode(turnboard, node, mc, 'O', 'X')
for num, c in enumerate(node.children):
	if mc == c[0]:
		node.children[num][1] = newNode
		print(num)
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
