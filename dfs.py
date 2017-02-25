import itertools
import copy
import time


class node:
	def __init__(self, value, path, parent, level):
		self.value = value
		self.path = path
		self.parent = parent
		self.level = level

	def __repr__(self):
		return "%s %s %s %s" % (self.value, self.path, self.parent, self.level)

	def getPath(self):
		return self.path

	def getParent(self):
		return self.parent

	def getValue(self):
		return self.value

	def getLevel(self):
		return self.level


def toArray(string):
	array = []
	for var in string.split(';'):
		array2 = []
		separated = var.replace(' ', '')
		for val in ((separated.replace('(', '')).replace(')', '')).split(','):
			if val != '':
				array2.append(val)
		array.append(array2)
	return array

def move(current_node, visited, possible_movements):
	array = []
	current_array = current_node.getValue()
	for action in possible_movements:
		current = copy.deepcopy(current_array)
		if len(current[action[0]]) >= 1:
			current[action[1]].append((current[action[0]])[-1])
			(current[action[0]]).pop()
		if current not in visited:
			array.append(node(current, [action[0], action[1]], current_node, current_node.getLevel() + 1))
	return list(array)

def equals(actual, goal):
	count = 0
	for index, item in enumerate(goal):
		if item != ['X']:
			if actual[index] == goal[index]:
				count += 1
	if count == len(goal) - goal.count(['X']):
		return True, actual
	return False


def dfs(lenght, current, goal):
	cost = 0
	found = False
	current_array = toArray(current)
	goal_array = toArray(goal)
	lifo = [node(current_array, [], [], 0)]
	path = []
	visited = []
	nodesVisited =[]
	possible_movements = list(itertools.permutations(range(0, len(current_array)), 2))
	if all(len(var) <= lenght for var in goal_array) and len(current_array) == len(goal_array):
		while len(lifo) > 0:
			if equals(lifo[-1].getValue(), goal_array):
				recursive = lifo[-1].getParent()
				path.append(lifo[-1].getPath())
				cost = 1 + abs((lifo[-1].getPath())[0] - (lifo[-1].getPath())[1])
				while recursive != []:
					pathCost = recursive.getPath()
					path.append(pathCost)
					if pathCost != []:
						cost += 1 + abs(pathCost[0] - pathCost[1])
					recursive = recursive.getParent()
				print(cost)
				print((str(path[::-1]))[5:-1]).replace('[', '(').replace(']', ')')
				break;
			else:
				if lifo[-1].getLevel() <= lenght:
					lifo.extend(move(lifo[-1], visited, possible_movements))
					visited.append(lifo[-1].getValue())
					nodesVisited.append(lifo[-1])
				lifo.pop()
	else:
		print("No solution found")



