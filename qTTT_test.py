from qTTT_graph import *
#node = GameNode(Board(), None, None, 'X')
"""turnboard = node.board.copy()
mc = node.children[12][0]
turnboard.makeMove(mc)
newNode = GameNode(turnboard, node, mc, 'O')
for num, c in enumerate(node.children):
	if mc == c[0]:
		node.children[num][1] = newNode
		print(num)
node = newNode


turnboard = node.board.copy()
mc = node.children[11][0]
turnboard.makeMove(mc)

newNode = GameNode(turnboard, node, mc, 'O')
for num, c in enumerate(node.children):
	if mc == c[0]:
		node.children[num][1] = newNode
		print(num)
node = newNode
"""

b = Board()
b.addSpookyMark_('O', 1, 2, 4)
b.addSpookyMark_('O', 3, 2, 4)
omc = Movecode(None, SpookyMarkPars(['O', 3, 2, 4]))
b.printBoard()
node = GameNode(b, None, omc, 'X')
