import sys
import math

# print "Enter the numbers"
# a = raw_input()
# #converting all elements of array to integer
# a = (map(int,a.split()))

def calcThruster(input_file, phase_settings): 
  program_inputs = [0]
  amplifier_counter = 0
  while amplifier_counter < len(phase_settings):
    local_inputs = [phase_settings[amplifier_counter], program_inputs[amplifier_counter]]
    input_read = 0
    with open(input_file, "r") as i:
      input_array = i.readline()
      input_array = input_array.split(',')
      i = 0
      while i < len(input_array):
        opcode = int(input_array[i])
        if opcode is 99:
          amplifier_counter += 1
          break
        
        if opcode >= 10000:
          address3 = i+3
          opcode -= 10000
        else:
          address3 = int(input_array[i+3])

        if opcode >= 1000:
          address2 = i+2
          opcode -= 1000
        else:
          address2 = int(input_array[i+2])

        if opcode >= 100:
          address1 = i+1
          opcode -= 100
        else:
          address1 = int(input_array[i+1])

        
        if opcode % 10 is 1:
          input_array[address3] = str(int(input_array[address1]) + int(input_array[address2]))
          i += 4
        elif opcode % 10 is 2:
          input_array[address3] = str(int(input_array[address1]) * int(input_array[address2]))
          i += 4
        elif opcode % 10 is 3:
          # nbr = input("Nbr: ")
          input_array[address1] = local_inputs[input_read]
          input_read += 1
          i += 2
        elif opcode % 10 is 4:
          program_inputs.append(input_array[address1])
          if amplifier_counter + 1 == len(phase_settings):
            return input_array[address1]
          i += 2
        elif opcode % 10 is 5:
          if int(input_array[address1]) != 0:
            i = int(input_array[address2])
          else: 
            i += 3
        elif opcode % 10 is 6:
          if int(input_array[address1]) == 0:
            i = int(input_array[address2])
          else: 
            i += 3
        elif opcode % 10 is 7:
          if int(input_array[address1]) < int(input_array[address2]):
            input_array[address3] = "1"
          else:
            input_array[address3] = "0"
          i += 4
        elif opcode % 10 is 8:
          if int(input_array[address1]) == int(input_array[address2]):
            input_array[address3] = "1"
          else:
            input_array[address3] = "0"
          i += 4
      
