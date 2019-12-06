import math
import sys
from collections import defaultdict

grand_total = 0

def count_orbits(solar_system, current_planet, orbit_total):
  global grand_total
  if current_planet not in solar_system:
    return
  orbit_total += 1
  for planet in solar_system[current_planet]:
    grand_total += orbit_total
    count_orbits(solar_system, planet, orbit_total)


with open('input.txt') as fp:
  total_fuel = 0
  solar_system = defaultdict(set)
  for line in fp:
    planets = line.split(")")
    base = planets[0].rstrip()
    current_planet = planets[1].rstrip()
    solar_system[base].add(current_planet)
  
  count_orbits(solar_system, 'COM', orbit_total = 0)
  print('Grand total: ' + str(grand_total))

    
