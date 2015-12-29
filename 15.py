inp = '''Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8'''

from operator import mul

data = []
for line in inp.split('\n'):
	x = line.split()
	data.append((int(x[2][:-1]), int(x[4][:-1]), int(x[6][:-1]), int(x[8][:-1]), int(x[10])))

# fun with list comprehensions!
print max(reduce(mul, (max(val, 0) for val in [i*data[0][x] + j*data[1][x] + k*data[2][x] + (100-i-j-k)*data[3][x] for x in xrange(4)]), 1) for i in xrange(0,101) for j in xrange(0,101-i) for k in xrange(0,101-i-j)) # 21367368