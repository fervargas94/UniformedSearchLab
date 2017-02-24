import itertools
import copy

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

def move(current_node, possible_movements):
	array = []
	current_array = current_node.getValue()
	for action in possible_movements:
		current = copy.deepcopy(current_array)
		if len(current[action[0]]) >= 1:
			current[action[1]].append((current[action[0]])[-1])
			(current[action[0]]).pop()
		array.append(node(current, [action[0], action[1]], current_array, current_node.getLevel() + 1))
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

def getPath(visited, goal_array):
	for visit in visited:
		if visit.getValue() == goal_array:
			return visit

def bfs(lenght, current, goal):
	cost = 0
	found = False
	current_array = toArray(current)
	goal_array = toArray(goal)
	lifo = [node(current_array, [], [], 0)]
	path = []
	visited = []
	possible_movements = list(itertools.permutations(range(0, len(current_array)), 2))
	if all(len(var) <= lenght for var in goal_array) and len(current_array) == len(goal_array):
		while len(lifo) > 0:
			if equals(lifo[-1].getValue(), goal_array):
				print("found")
				recursive = lifo[-1].getParent()
				path.append(lifo[-1].getPath())
				cost = 1 + abs((lifo[-1].getPath())[0] - (lifo[-1].getPath())[1])
				while recursive != current_array:
					value = getPath(visited, recursive)
					path.append(value.getPath())
					cost = cost + 1 + abs((value.getPath())[0] - (value.getPath())[1])
					recursive = value.getParent()
					print(recursive)
				print(cost)
				print(path[::-1])
				break;
			else:
				if lifo[-1].getLevel() <= lenght:
					print("Es menor", lifo[-1])
					lifo.extend(move(lifo[-1], possible_movements))
					visited.append(lifo[-1])
				else:
					print("Es mayor", lifo[-1])
				lifo.pop()
	else:
		print("No solution found")

bfs(3, "(A); (B); (C)", "(A, B); X; X")


