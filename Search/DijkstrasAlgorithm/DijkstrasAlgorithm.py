##

"""
O(n^2)
"""
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

print(graph)
print(costs)
print(parents)

def findLowestCostNode(costs: dict):
	lowestCost = float("inf")
	lowestCostNode = None
	for node in costs:
		cost = costs[node]
		if cost < lowestCost and node not in processed:
			lowestCost = cost
			lowestCostNode = node
	return lowestCostNode

node = findLowestCostNode(costs)
while node is not None:
	cost = costs[node]
	neighbors = graph[node]
	for n in neighbors.keys():
		newCost = cost + neighbors[n]
		if costs[n] > newCost:
			costs[n] = newCost
			parents[n] = node
	processed.append(node)
	node = findLowestCostNode(costs)

print(parents)

def createPath(startNode, endNode, parentsDict):
	curNode = startNode
	path = [startNode]
	while curNode != endNode:
		for i in parentsDict:
			if parentsDict[i] == curNode:
				path.append(i)
				curNode = i
	return path

print(createPath("start", "fin", parents))
