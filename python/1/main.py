import math

def fuelCalc(fuel):
  new_fuel = math.floor(int(fuel) / 3) - 2
  if new_fuel <= 0:
    return 0
  return new_fuel + fuelCalc(new_fuel)

with open('input.txt') as fp:
  total_fuel = 0
  for line in fp:
    total_fuel += fuelCalc(int(line))
  print(total_fuel)