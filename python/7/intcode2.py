import sys
import math

def calcThruster(input_file, phase_settings): 
  with open(input_file, "r") as i:
    input_array = i.readline()
    input_array = input_array.split(',')

    # Variables
    program_inputs = []
    program_counters = []
    program_memories = []
    amp_read = []
    last_output = 0
    amplifier_counter = 0

    for i in range(0, len(phase_settings)):
      program_inputs.append(0)
      program_counters.append(0)
      program_memories.append(list(input_array))
      amp_read.append(0)
    
    while True:
      i = program_counters[amplifier_counter]
      input_array = program_memories[amplifier_counter]
      while i < len(input_array):
        opcode = int(input_array[i])
        if opcode is 99:
          if amplifier_counter + 1 == len(phase_settings):
            return last_output
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
          if amp_read[amplifier_counter]:
            input_array[address1] = program_inputs[amplifier_counter]
          else: 
            input_array[address1] = phase_settings[amplifier_counter]
            amp_read[amplifier_counter] = 1
          i += 2
        elif opcode % 10 is 4:
          i += 2
          program_counters[amplifier_counter] = i
          program_memories[amplifier_counter] = list(input_array)
          amplifier_counter += 1
          if amplifier_counter == len(phase_settings):
            amplifier_counter = 0
          last_output = input_array[address1]
          program_inputs[amplifier_counter] = input_array[address1]
          break
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
      
