import sys
import math

# print "Enter the numbers"
# a = raw_input()
# #converting all elements of array to integer
# a = (map(int,a.split()))

with open("input.txt", "r") as i:
    input = i.readline()
    input = input.split(',')

    i = 0
    while i < len(input):
      input_nbr = int(input[i])
      if input_nbr is 99:
        break

      address1 = int(input[i+1])
      address2 = int(input[i+2])
      address3 = int(input[i+3])
      if input_nbr is 1:
        input[address3] = str(int(input[address1]) + int(input[address2]))
      elif input_nbr is 2:
        input[address3] = str(int(input[address1]) * int(input[address2]))
      i += 4
      
    print(input[0])