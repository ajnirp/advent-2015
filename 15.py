inp = '''Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3,
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3,
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8,
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8,'''

from operator import mul

# fun with list comprehensions!
data = [map(lambda y: int(x[y << 1][:-1]), xrange(1,6)) for x in [line.split() for line in inp.split('\n')]]
print max(reduce(mul, (max(val,0) for val in [i*data[0][x] + j*data[1][x] + k*data[2][x] + (100-i-j-k)*data[3][x] for x in xrange(4)]), 1) for i in xrange(101) for j in xrange(101-i) for k in xrange(101-i-j)) # 21367368
print max(reduce(mul, (max(val,0) for val in [i*data[0][x] + j*data[1][x] + k*data[2][x] + (100-i-j-k)*data[3][x] if i*data[0][4] + j*data[1][4] + k*data[2][4] + (100-i-j-k)*data[3][4] == 500 else 0 for x in xrange(4)]), 1) for i in xrange(101) for j in xrange(101-i) for k in xrange(101-i-j)) # 1766400
