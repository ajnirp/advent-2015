#! /usr/bin/env python3

# hp, damage, armor
boss = [103, 9, 2]

from itertools import chain

# cost, damage, armor
weapons = [(8,4,0), (10,5,0), (25,6,0), (40,7,0), (74,8,0)]
armors = [(13,0,1), (31,0,2), (53,0,3), (75,0,4), (102,0,5)]
rings = [(25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3)]

for equipment in [weapons, armors, rings]:
	equipment.append((0, 0, 0))

def all_pairs(n):
	return ((i, j) for i in range(n) for j in range(i+1, n))

# return an iterator of (cost, damage, armor)
def ring_sets():
	def one_or_two_rings():
		for i1, i2 in all_pairs(len(rings)):
			c1, d1, a1 = rings[i1]
			c2, d2, a2 = rings[i2]
			yield (c1+c2, d1+d2, a1+a2)
	def no_rings():
		yield (0, 0, 0)
	return chain(no_rings(), one_or_two_rings())

def overall_stats():
	for weapon in weapons:
		for armor in armors:
			for ring_set in ring_sets():
				yield tuple(x+y+z for x,y,z in zip(weapon, armor, ring_set))

def simulate_fight(player):
	pass # todo