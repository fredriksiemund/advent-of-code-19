with open("input.txt", "r") as i:
  input = i.readline()
  input = input.split('-')
  possible_solution = []
  current_code = int(input[0])
  while current_code <= int(input[1]):
    adjacents = {}
    previous_digit = -1
    not_decreasing = 1
    for i in str(current_code):
      if int(i) is previous_digit:
        if i in adjacents:
          adjacents[i] += 1
        else:
          adjacents[i] = 2
      if int(i) < previous_digit:
        not_decreasing = 0
        break
      previous_digit = int(i)
    if not_decreasing:
      for key in adjacents:
        if adjacents[key] is 2:
          print(current_code)
          possible_solution.append(current_code)
          break
    current_code += 1

  print('Nbr of solutions: ' + str(len(possible_solution)))