import itertools
import copy

class node:
   def __init__(self, value, path, parent):
      self.value = value
      self.path = path
      self.parent = parent

   def __repr__(self):
   	return "%s" % self.value 
   
   def getPath(self):
   	return self.path

   def getParent(self):
   	return self.parent

   def getValue(self):
   	return self.value


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

def move(current_array, nodes, possible_movements):
	array = []
	for action in possible_movements:
		current = copy.deepcopy(current_array)
		if len(current[action[0]]) >= 1:
			current[action[1]].append((current[action[0]])[-1])
			(current[action[0]]).pop()
		array.append(current)
		nodes.append(node(current, action, current_array))
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

def getPath(nodes, goal_array):
	for nodex in nodes:
		if nodex.getValue() == goal_array:
			return nodex

def bfs(lenght, current, goal):
	cost = 0
	found = False
	current_array = toArray(current)
	goal_array = toArray(goal)
	fifo = []
	path = []
	movements = [[]]
	nodes = [node(current_array, [], [])]
	movements.extend(list(itertools.permutations(range(0, len(current_array)), 2)))
	possible_movements = list(itertools.permutations(range(0, len(current_array)), 2))
	if all(len(var) <= lenght for var in goal_array) and len(current_array) == len(goal_array):
		fifo.append(current_array)
		while len(fifo) > 0:
			if equals(fifo[0], goal_array):
				recursive = (equals(fifo[0], goal_array))[1]
				while recursive != current_array:
					value = getPath(nodes, recursive)
					path.append(value.getPath())
					cost = cost + 1 + abs((list(value.getPath()))[0] - (list(value.getPath()))[1])
					recursive = value.getParent()
				print(cost)
				print(path[::-1])
				break;
			else:
				del movements[0]
				movements.extend(possible_movements)
				fifo.extend(move(fifo[0], nodes, possible_movements))
				del fifo[0]
	else:
		print("No solution found")

bfs(2, "(A); (B); ()", "(A, B); X; X")


