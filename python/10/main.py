import math

def part1():
  with open("input.txt", "r") as fp:
    lines = fp.readlines()
    asteroids = {}
    current_X = -1
    current_Y = -1
    for current_Y, line in enumerate(lines):
      for current_X, char in enumerate(line):
        if char == "#":
          viewable_asteroids = {} # Key: angle ratio, value: distance
          for other_Y, line in enumerate(lines):
            for other_X, char in enumerate(line):
              if char == "#" and (other_X != current_X or other_Y != current_Y):
                angle_base = 0
                Y_delta = current_Y - other_Y
                X_delta = other_X - current_X
                angle = math.atan2(Y_delta, X_delta)
                distance = math.sqrt((other_Y - current_Y)**2 + (other_X - current_X)**2)
                if str(angle) in viewable_asteroids:
                  if distance < viewable_asteroids[str(angle)]:
                    viewable_asteroids[str(angle)] = distance
                else:
                  viewable_asteroids[str(angle)] = distance
          asteroids[str(current_X) + ","+ str(current_Y)] = len(viewable_asteroids)
    maximum = max(asteroids, key=asteroids.get)
    print(maximum, asteroids[maximum])
              
def part2():
  with open("input.txt", "r") as fp:
    lines = fp.readlines()
    asteroids = {}
    current_X = 25
    current_Y = 31
    destroyed_asteroids = []
    while len(destroyed_asteroids) <= 200:
      viewable_asteroids = {} # Key: angle ratio, value: [distance, coordinates]
      for other_Y, line in enumerate(lines):
        for other_X, char in enumerate(line):
          if char == "#" and (other_X != current_X or other_Y != current_Y):
            coordinate_string = str(other_X)+","+str(other_Y)
            if coordinate_string not in destroyed_asteroids:
              Y_delta = current_Y - other_Y
              X_delta = other_X - current_X
              angle = math.atan2(Y_delta, X_delta)
              distance = math.sqrt((other_Y - current_Y)**2 + (other_X - current_X)**2)
              if str(angle) in viewable_asteroids:
                if distance < viewable_asteroids[str(angle)]:
                  viewable_asteroids[str(angle)] = [distance, coordinate_string]
              else:
                viewable_asteroids[str(angle)] = [distance, str(other_X) + ","+ str(other_Y)]
      order = []
      for key in viewable_asteroids:
        order.append([float(key), viewable_asteroids[key][1]])
      order = sorted(order, key=lambda x: x[0])
      start_index = -1
      for i, element in enumerate(order):
        if element[0] > math.atan2(1,0):
          start_index = i - 1
          break
      new_order = order[start_index + 1:len(order)] + order[0:start_index + 1]
      for i in range(len(new_order)-1, 0, -1):
        destroyed_asteroids.append(new_order[i][1])
    print(destroyed_asteroids[199])

part2()