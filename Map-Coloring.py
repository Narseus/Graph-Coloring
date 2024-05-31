def start():
    maxcolor = 3
    firstnode = ''
    neighbourNumber = 0
    for node, neighbours in adjacencyList.items():
        if len(neighbours) > neighbourNumber and color[node] == 0:
            neighbourNumber = len(neighbours)
            firstnode = node
    if possibleColor(firstnode, maxcolor):
        return True
    else:
        print("Can't color the map with only 3 colors.")
        return False


def possibleColor(node, maxcolor):
    if node == '':
        for key, value in color.items():
            if value == 0:
                possibleColor(key, maxcolor)
        return True

    for c in range(1, maxcolor + 2):
        if canColor(node, c):
            color[node] = c
            shift = ''
            if possibleColor(shift, maxcolor):
                return True
            else:
                color[node] = 0
    return False


def canColor(node, c):
    return all([color[neighbours] != c for neighbours in adjacencyList[node]])


def colorName(color):
    if color == 1:
        return 'RED'
    elif color == 2:
        return 'GREEN'
    elif color == 3:
        return 'BLUE'


adjacencyList = {
    'Fars': ['Kerman', 'Yazd', 'Isfahan', 'Hormozgan'],
    'Kerman': ['Yazd', 'Fars', 'Hormozgan'],
    'Isfahan': ['Yazd', 'Fars'],
    'Hormozgan': ['Kerman', 'Fars'],
    'Yazd': ['Kerman', 'Isfahan', 'Fars']
}

color = {
    'Fars': 0,
    'Kerman': 0,
    'Isfahan': 0,
    'Yazd': 0,
    'Hormozgan': 0,
}

start()

for node, color in color.items():
    print(node, ':', colorName(color))
