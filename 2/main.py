import sys
import math

with open("input.txt", "r") as i:
    input = i.readline()
    input = input.split(',')
    for i in range(0, len(input)):
        if input[i] is '1':
            address1 = int(input[i+1])
            address2 = int(input[i+2])
            address3 = int(input[i+3])
            input[address3] = str(int(input[address1]) + int(input[address2]))
            i += 3
        elif input[i] is '2':
            address1 = int(input[i+1])
            address2 = int(input[i+2])
            address3 = int(input[i+3])
            input[address3] = str(int(input[address1]) * int(input[address2]))
            i += 3
        elif input[i] is '99':
            break
    print(input)