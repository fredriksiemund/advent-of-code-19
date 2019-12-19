import sys
import numpy as np


image_height = 6
image_width = 25

def part2():
  with open("input.txt", "r") as file:
    global image_height, image_width
    image = file.read()
    layers = []
    i = 0
    while i < len(image):
      layers.append(image[i:i+(image_width)])
      i += image_width
    final_image = np.zeros((image_height, image_width), int)
    for layer_index,layer in enumerate(layers):
      for digit_index,digit in enumerate(layer):
        if layer_index < image_height: # initiate all layers in final image
          final_image[layer_index%image_height][digit_index] = 2
        if digit != "2" and final_image[layer_index%image_height][digit_index] == 2:
          final_image[layer_index%image_height][digit_index] = digit
    print(final_image)


def part1():
  with open("input.txt", "r") as file:
    global image_height, image_width
    image = file.read()
    layers = []
    i = 0
    while i < len(image):
      layers.append(image[i:i+(image_height*image_width)])
      i += image_height*image_width
    del layers[-1]
    layer_with_zeros = [sys.maxsize,-1,0,0] # [nbr of zeroes,layer id,nbr of ones, nbr of twos]
    for index, layer in enumerate(layers):
      counter = [0,0,0] # zeroes, ones, twos
      for digit in layer:
        if digit == "0":
          counter[0] += 1
        elif digit == "1":
          counter[1] += 1
        elif digit == "2":
          counter[2] += 1
      if counter[0] < layer_with_zeros[0]:
        layer_with_zeros = [counter[0],index,counter[1],counter[2]]
    result = layer_with_zeros[2] * layer_with_zeros[3]
    print(layer_with_zeros)

part2()
