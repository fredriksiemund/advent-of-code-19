import sys
import math

latest_output = [] # Color,rotation
next_input = 1
visted_nodes = {(0,0): 0}
current_node = (0,0)
rotation = 90

def calcNextInput():
  global next_input, latest_output, visted_nodes, current_node, rotation
  visted_nodes[current_node] = latest_output[0]
  if latest_output[1] == 0:
    rotation += 90
  elif latest_output[1] == 1:
    rotation -= 90
  rotation = rotation % 360
  if rotation == 0:
    current_node = (current_node[0]+1, current_node[1])
  elif rotation == 90:
    current_node = (current_node[0], current_node[1]+1)
  elif rotation == 180:
    current_node = (current_node[0]-1, current_node[1])
  elif rotation == 270:
    current_node = (current_node[0], current_node[1]-1)
  latest_output = []
  if current_node in visted_nodes:
    next_input = visted_nodes[current_node]
  else:
    next_input = 0
  
def printOutput():
  global visted_nodes
  max_y = 0
  min_y = 0
  max_x = 0
  min_x = 0
  for key in visted_nodes:
    if key[0] > max_x:
      max_x = key[0]
    if key[1] > max_y:
      max_y = key[1]
    if key[0] < min_x:
      min_x = key[0]
    if key[1] < min_y:
      min_y = key[1]
  output_matrix = []
  for row in range(0,(max_y - min_y) + 1):
    output_matrix.append([1] * (max_x - min_x + 1))
  for key in visted_nodes:
    output_matrix[4+key[1]][key[0]] = visted_nodes[key] 
  for row in output_matrix:
    temp_output = list(map(str, row))
    print(''.join(temp_output))


def main(): 
  global next_input, latest_output
  with open("input.txt", "r") as fp:
      input_array = fp.readline()
      input_array = input_array.split(',')
      input_array.append('0')
      input_array.append('0')
      program_memory = {}
      for index, element in enumerate(input_array):
        program_memory[str(index)] = input_array[index]
      relative_base = 0
      i = 0
      while i < len(input_array):
        instruction = program_memory[str(i)]
    
        if instruction == '99':
          break

        while len(instruction) < 5:
          instruction = "0" + instruction
        addresses = [0, 0, 0] # Address 3,2,1
        for j in range(0,3):
          if instruction[j] == "1": # immediate mode, tha parameter stores the value
            addresses[j] = i + (3 - j)
          elif instruction[j] == "2": # relative mode, the parameter stores the relative address
            addresses[j] = relative_base + int(input_array[(i + (3 - j))]) 
          elif instruction[j] == "0": # position mode, the parameter stores the address
            addresses[j] = int(input_array[i + (3 - j)])
          if str(addresses[j]) not in program_memory:
            program_memory[str(addresses[j])] = 0
        address3 = str(addresses[0])
        address2 = str(addresses[1])
        address1 = str(addresses[2])

        opcode = int(instruction[len(instruction) - 2: len(instruction)])
        if opcode == 1:
          program_memory[address3] = str(int(program_memory[address2]) + int(program_memory[address1]))
          i += 4
        elif opcode == 2:
          program_memory[address3] = str(int(program_memory[address2]) * int(program_memory[address1]))
          i += 4
        elif opcode == 3:
          program_memory[address1] = next_input
          i += 2
        elif opcode == 4:
          latest_output.append(int(program_memory[address1]))
          if len(latest_output) == 2:
            calcNextInput()
          i += 2
        elif opcode == 5:
          if int(program_memory[address1]) != 0:
            i = int(program_memory[address2])
          else: 
            i += 3
        elif opcode == 6:
          if int(program_memory[address1]) == 0:
            i = int(program_memory[address2])
          else: 
            i += 3
        elif opcode == 7:
          if int(program_memory[address1]) < int(program_memory[address2]):
            program_memory[address3] = "1"
          else:
            program_memory[address3] = "0"
          i += 4
        elif opcode == 8:
          if int(program_memory[address1]) == int(program_memory[address2]):
            program_memory[address3] = "1"
          else:
            program_memory[address3] = "0"
          i += 4
        elif opcode == 9:
          relative_base += int(program_memory[address1])
          i += 2
      
main()
printOutput()