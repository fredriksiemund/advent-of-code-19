import sys
import math

with open("input.txt", "r") as i:
    input = i.readline()
    input = input.split(',')
    i = 0
    while i < len(input):
      input_nbr = int(input[i])
      if input_nbr is 1:
        address1 = int(input[i+1])
        address2 = int(input[i+2])
        address3 = int(input[i+3])
        input[address3] = str(int(input[address1]) + int(input[address2]))
        i += 3
      elif input_nbr is 2:
        address1 = int(input[i+1])
        address2 = int(input[i+2])
        address3 = int(input[i+3])
        input[address3] = str(int(input[address1]) * int(input[address2]))
        i += 3
      elif input_nbr is 99:
        break
      i += 1
    print(input[0])