inp = '''Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3,
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3,
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8,
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8,'''

from operator import mul
from functools import reduce
r = range
d = [[int(x[y*2][:-1]) for y in r(1,6)] for x in [l.split() for l in inp.split('\n')]]
print(max(reduce(mul,(max(v,0) for v in [i*d[0][x] + j*d[1][x] + k*d[2][x] + (100-i-j-k)*d[3][x] for x in r(4)]), 1) for i in r(101) for j in r(101-i) for k in r(101-i-j))) # 21367368
print(max(reduce(mul,(max(v,0) for v in [i*d[0][x] + j*d[1][x] + k*d[2][x] + (100-i-j-k)*d[3][x] if i*d[0][4] + j*d[1][4] + k*d[2][4] + (100-i-j-k)*d[3][4] == 500 else 0 for x in r(4)]), 1) for i in r(101) for j in r(101-i) for k in r(101-i-j))) # 1766400
