from collections import deque

def isDesiredNode(name: str):
	return name[-1] == 'm'

graph = {}
#start node
graph["you"] = ["alice", "bob", "claire"]
#first level nodes
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "johny"]
#second level nodes
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johny"] = []

def breathFirstSearch(startNode):
	"""
	O(V+E)
	V - vertices value
	E - edges value
	"""
	searchQueue = deque()
	searchQueue += graph["you"]
	checkedNodes = []
	while searchQueue:
		node = searchQueue.popleft()
		if not node in checkedNodes:
			if isDesiredNode(node):
				return {"result":True, "node": node}
			else:
				searchQueue += graph[node]
				checkedNodes.append(node)
	return {"result":False, "node": None}

print(breathFirstSearch("you")["node"])

