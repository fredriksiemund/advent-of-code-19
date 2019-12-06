import math
import sys
from collections import defaultdict


with open('input.txt') as fp:
  total_fuel = 0
  solarSystem = defaultdict(set)
  line = fp.readline()
  com = line[0:3]
  currentPlanet = line[4]
  solarSystem[com].add(currentPlanet)
  for line in fp:
    base = line[0]
    currentPlanet = line[2]
    solarSystem[base].add(currentPlanet)

  totalOrbits = 0
  currentPlanet = "COM"
  while True:
    for planet in solarSystem[currentPlanet]:

    
