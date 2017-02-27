import itertools
import copy

class node:
    def __init__(self, cost, heuristic, value, parent, path, visited):
        self.cost = cost
        self.heuristic = heuristic
        self.value = value
        self.parent = parent
        self.path = path
        self.visited = visited

    def __repr__(self):
        return "%s %s %s %s" % (self.cost, self.value, self.parent, self.path)
   
    def getPath(self):
        return self.path

    def getCost(self):
        return self.cost

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


def move(current_node, visited, possible_movements, goal_array, lenght):
    array = []
    current_array = current_node.getValue()
    cost = current_node.getCost()
    for action in possible_movements:
        current = copy.deepcopy(current_array)
        if len(current[action[0]]) >= 1:
            current[action[1]].append((current[action[0]])[-1])
            (current[action[0]]).pop()
        if current not in visited:
            heuristicValue = heuristic(current, goal_array)
            array.append(node(cost + (heuristicValue + (1 + abs(action[0] - action[1]))), heuristicValue, current, current_node, [action[0], action[1]], False))
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

def heuristic(actual, goal):
    count = 0
    for index, item in enumerate(goal):
        if item != ['X']:
            for char in item:
                if char not in goal[index]:
                    count += 1
    return count

'''def heuristic(actual, goal):
    goal_dict = {}
    actual_dict = {}
    cost = 0
    for index, item in enumerate(goal):
        for level, char in enumerate(item):
            if char != 'X':
                goal_dict[char] = [index, level]
        for level, char in enumerate(actual[index]):
            actual_dict[char] = [index, level]
    for item in goal_dict:
        cost = cost + abs((goal_dict[item])[0] - (actual_dict[item])[0]) + abs((goal_dict[item])[1] - (actual_dict[item])[1])
    return cost'''

'''def heuristic(actual, goal):
    distances = {}
    for index, box in enumerate(goal):
        if box != '' and box != 'X':
            for char in box:
                distances[char] = index
    for index, box in enumerate(actual):
        if box != '':
            for char in box:
                if char in distances:
                    distances[char] = abs(index - distances[char]) + 1 #calculate h
                else:
                    distances[char] = 0
    print(distances)
    return sum(distances.values())'''

def invalidHeuristic(actual, goal):
    count = 0
    for index, item in enumerate(goal):
        if item != ['X']:
            for char in item:
                if char in goal[index]:
                    count += 1
    return count

def getFinalPath(visited, goal_array):
    for visit in visited:
        if visit.getValue() == goal_array:
            return visit

def astar(lenght, current, goal):
    cost = 0
    current_array = toArray(current)
    goal_array = toArray(goal)
    priority = [node(0, 0, current_array, [], [], True)]
    path = []
    visited = []
    possible_movements = list(itertools.permutations(range(0, len(current_array)), 2))
    if all(len(var) <= lenght for var in goal_array) and len(current_array) == len(goal_array):
        while len(priority) > 0:
            priority.sort(key=lambda x: x.cost)
            if equals(priority[0].getValue(), goal_array):
                recursive = priority[0].getParent();
                path.append(priority[0].getPath())
                while recursive != []:
                    pathCost = recursive.getPath()
                    path.append(pathCost)
                    recursive = recursive.getParent()
                print(priority[0].getCost())
                print((str(path[::-1]))[5:-1]).replace('[', '(').replace(']', ')')
                break;
            else:
                #if priority[0].getValue() not in visited:
                priority.extend(move(priority[0], visited, possible_movements, goal_array, lenght))
                visited.append(priority[0].getValue())
                del priority[0]
    else:
        print("No solution found")

if __name__ == "__main__":

    height = int(input())
    start = raw_input()
    goal = raw_input()

    astar(height, start, goal)