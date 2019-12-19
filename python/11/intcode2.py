import sys
import math

def run(input_array):
    program_memory = {}
    for pc in enumerate(input_array):
      program_memory[pc] = input_array[pc]
    relative_base = 0
    pc = 0
    while pc < len(input_array):
      instruction = program_memory[pc]
      
      if instruction == 99:
        break

      
with open("input.txt", "r") as fp:
    input_array = fp.readline()
    input_array = map(int, input_array.split(','))
    input_array = input_array + [0]*2
    print(input_array)
    