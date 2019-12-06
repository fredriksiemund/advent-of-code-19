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

path_to_me = []
path_to_santa = []
def count_santa_dist(solar_system, current_planet, current_path):
  global path_to_me
  global path_to_santa
  new_list = list(current_path)
  if current_planet == "SAN":
    path_to_santa = new_list
    return
  if current_planet == "YOU":
    path_to_me = new_list
    return
  new_list.append(current_planet)
  for planet in solar_system[current_planet]:
    count_santa_dist(solar_system, planet, new_list)



with open('input.txt') as fp:
  solar_system = defaultdict(set)
  my_orbit = ""
  for line in fp:
    planets = line.split(")")
    base = planets[0].rstrip()
    orbiting_planet = planets[1].rstrip()
    solar_system[base].add(orbiting_planet)
    if orbiting_planet == "YOU":
      my_orbit = base
  
  # Part 2
  count_santa_dist(solar_system, 'COM', [])
  i = 0
  while i < len(path_to_me) and i < len(path_to_santa):
    if path_to_me[i] != path_to_santa[i]:
      break
    i += 1
  total = (len(path_to_me) - i)  + (len(path_to_santa) - i)
  print(total)

  # # Part 1
  # count_orbits(solar_system, 'COM', 0)
  # print('Grand total: ' + str(grand_total))

    
