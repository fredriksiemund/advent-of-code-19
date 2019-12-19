import sys
import math

with open("input.txt", "r") as i:
    paths = set()
    path1 = []
    path2 = []
    j = 1
    lines = i.readlines()
    line1 = lines[0]
    line = line1.replace('\n', '')
    latestPos = [0,0]
    steps = line.split(',')
    for direction in steps:
        for step in range(0, int(direction[1:])):
            if direction[0] == 'R':
                latestPos[0] += 1
            elif direction[0] == 'D':
                latestPos[1] -= 1
            elif direction[0] == 'L':
                latestPos[0] -= 1
            elif direction[0] == 'U':
                latestPos[1] += 1
            paths.add((latestPos[0], latestPos[1]))
            path1.append((latestPos[0], latestPos[1]))

    line2 = lines[1]
    line = line2.replace('\n', '')
    latestPos = [0,0]
    steps = line.split(',')

    intersections = set()
    shortest_path = sys.maxsize
    for direction in steps:
        for step in range(0, int(direction[1:])):
            if direction[0] == 'R':
                latestPos[0] += 1
            elif direction[0] == 'D':
                latestPos[1] -= 1
            elif direction[0] == 'L':
                latestPos[0] -= 1
            elif direction[0] == 'U':
                latestPos[1] += 1
            path2.append((latestPos[0], latestPos[1]))
            if (latestPos[0], latestPos[1]) in paths:
                intersections.add((latestPos[0], latestPos[1]))
                path_length = math.sqrt(latestPos[0]**2) + math.sqrt(latestPos[1]**2)
                if path_length < shortest_path:
                    shortest_path = path_length
    
    print('Shortest path: ' + str(shortest_path))
    sum = sys.maxsize


    for intersection in intersections:
        distance = path1.index(intersection) + path2.index(intersection)
        if distance < sum:
            sum = distance
    print('Shortest sum: ' + str(sum + 2))

