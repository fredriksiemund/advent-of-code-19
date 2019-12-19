import sys
import math

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
        if instruction[j] == "1": # immediate mode, the parameter stores the value
          addresses[j] = i + (3 - j)
        elif instruction[j] == "2": # relative mode, the parameter stores the relative address
          addresses[j] = relative_base + int(input_array[(i + (3 - j))]) 
        else: # == "0", position mode, the parameter stores the address
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
        nbr = input("Input: ")
        program_memory[address1] = str(nbr)
        i += 2
      elif opcode == 4:
        print("Output: " + program_memory[address1])
        print(i, address1)
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
      
