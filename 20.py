inp = 34000000

from math import sqrt
from collections import Counter

visited = Counter()

def find_factors(n):
    if n == 1:
        return [1]
    if n in [2, 3]: return [1, n]
    i = 2
    res = [1]
    while i <= sqrt(n):
        if n % i == 0:
            res.append(i)
            res.append(n/i)
        i += 1
    res.append(n)
    return res

def presents_recd(n):
    return 10 * sum(find_factors(n))

i = 1000
while True:
    if presents_recd(i) >= inp:
        print i # 786240
        break
    i += 1

i = 1000
while True:
    factors = set(find_factors(i))
    to_remove = set()
    for factor in factors:
        if visited[factor] == 50:
            to_remove.add(factor)
        else:
            visited[factor] += 1
    for f in to_remove:
        factors.remove(f)
    presents = 11 * sum(factors)
    if presents > inp:
        print i # 831600
        break
    i += 1

# note: with pypy, on my machine, this takes nearly 7 sec + 15 sec