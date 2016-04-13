import time
from qTTT import *
import random
import numpy as np
import math
from qTTT_graph import *

# These functions are all explained in the survey paper

blockWinningmove = True	# Checks every time whether a move could be a winning move, needs a lot of time

def uctsearch(rootnode, maxTime, param):	# seeks to optimize game for computer (it needs to be computer's turn at rootnode)
	start_time = time.time()
	while time.time() - start_time <= maxTime or not rootnode.isExpanded(): # rootnode needs to have tried out all possibilites, else assert in bestchild will fail
		newNode =	treepolicy(rootnode, param)
		delta = defaultpolicy(newNode, rootnode.letter, rootnode.notletter)
		backup(newNode, delta)
	print("Number of sims: ")
	print(rootnode.N) 
	return bestchild(rootnode, param)[0]

def treepolicy(node, param):
	while not node.board.isTerminal():
		if not node.isExpanded():
			newNode = expand(node)
			return newNode
		else:
			node = bestchild(node, param)[1]
	return node

def expand(node):	
	assert(not node.isExpanded()) # reduce this some day to save time
	listExpandables = []
	for n, c in enumerate(node.children):
		if c[1] == None:
			listExpandables = listExpandables +  [c[0]]
	ind = random.randint(0, len(listExpandables)-1)
	newNode = node.createChildNode(listExpandables[ind])
	return newNode

def bestchild(node, param):
	assert(node.isExpanded())
	numchildren = len(node.children)
	vals = np.zeros(numchildren)
	for n, c in enumerate(node.children):
		vals[n] = 1.0*c[1].Q/c[1].N + param*math.sqrt(2*math.log(node.N)/c[1].N)
	return node.children[np.argmax(vals)]	# return best child

def defaultpolicy(node, computerletter, playerletter): # seeks to maximize computerletter's winning chance
	while not node.board.isTerminal():
		winningMove = node.findWinningMove()
		newBoard = node.board.copy()
		if blockWinningmove and winningMove:	# if exists
				newBoard.makeMove(winningMove)
				newNode = GameNode(newBoard, node, winningMove, node.notletter, node.letter)
		else:
			mc = random.choice(node.children)
			newBoard.makeMove(mc[0])
			newNode = GameNode(newBoard, node, mc[0], node.notletter, node.letter)
		node = newNode
	return node.board.actualWinner(computerletter, playerletter) 	# +1 means 'X' won, -1 means 'O' won, 0 is a tie


def backup(newNode, delta):
	while newNode:
		newNode.N = newNode.N + 1
		newNode.Q = newNode.Q + delta
		newNode = newNode.parent
			
