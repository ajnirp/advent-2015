inp = '''Alice would lose 57 happiness units by sitting next to Bob.
Alice would lose 62 happiness units by sitting next to Carol.
Alice would lose 75 happiness units by sitting next to David.
Alice would gain 71 happiness units by sitting next to Eric.
Alice would lose 22 happiness units by sitting next to Frank.
Alice would lose 23 happiness units by sitting next to George.
Alice would lose 76 happiness units by sitting next to Mallory.
Bob would lose 14 happiness units by sitting next to Alice.
Bob would gain 48 happiness units by sitting next to Carol.
Bob would gain 89 happiness units by sitting next to David.
Bob would gain 86 happiness units by sitting next to Eric.
Bob would lose 2 happiness units by sitting next to Frank.
Bob would gain 27 happiness units by sitting next to George.
Bob would gain 19 happiness units by sitting next to Mallory.
Carol would gain 37 happiness units by sitting next to Alice.
Carol would gain 45 happiness units by sitting next to Bob.
Carol would gain 24 happiness units by sitting next to David.
Carol would gain 5 happiness units by sitting next to Eric.
Carol would lose 68 happiness units by sitting next to Frank.
Carol would lose 25 happiness units by sitting next to George.
Carol would gain 30 happiness units by sitting next to Mallory.
David would lose 51 happiness units by sitting next to Alice.
David would gain 34 happiness units by sitting next to Bob.
David would gain 99 happiness units by sitting next to Carol.
David would gain 91 happiness units by sitting next to Eric.
David would lose 38 happiness units by sitting next to Frank.
David would gain 60 happiness units by sitting next to George.
David would lose 63 happiness units by sitting next to Mallory.
Eric would gain 23 happiness units by sitting next to Alice.
Eric would lose 69 happiness units by sitting next to Bob.
Eric would lose 33 happiness units by sitting next to Carol.
Eric would lose 47 happiness units by sitting next to David.
Eric would gain 75 happiness units by sitting next to Frank.
Eric would gain 82 happiness units by sitting next to George.
Eric would gain 13 happiness units by sitting next to Mallory.
Frank would gain 77 happiness units by sitting next to Alice.
Frank would gain 27 happiness units by sitting next to Bob.
Frank would lose 87 happiness units by sitting next to Carol.
Frank would gain 74 happiness units by sitting next to David.
Frank would lose 41 happiness units by sitting next to Eric.
Frank would lose 99 happiness units by sitting next to George.
Frank would gain 26 happiness units by sitting next to Mallory.
George would lose 63 happiness units by sitting next to Alice.
George would lose 51 happiness units by sitting next to Bob.
George would lose 60 happiness units by sitting next to Carol.
George would gain 30 happiness units by sitting next to David.
George would lose 100 happiness units by sitting next to Eric.
George would lose 63 happiness units by sitting next to Frank.
George would gain 57 happiness units by sitting next to Mallory.
Mallory would lose 71 happiness units by sitting next to Alice.
Mallory would lose 28 happiness units by sitting next to Bob.
Mallory would lose 10 happiness units by sitting next to Carol.
Mallory would gain 44 happiness units by sitting next to David.
Mallory would gain 22 happiness units by sitting next to Eric.
Mallory would gain 79 happiness units by sitting next to Frank.
Mallory would lose 16 happiness units by sitting next to George.'''

names = set()
change = {}
for line in inp.split('.')[:-1]:
    split = line.strip().split()
    fst, snd = split[0], split[-1]
    names.add(fst)
    change[(fst, snd)] = int(('-' if split[2] == 'lose' else '+') + split[3])

# this problem is pretty similar to 8.py

# generate a list of lists, where each list
# is a permutation of [0, 1, 2, ..., n-1]
def gen_perms(n): return [[0]] if n == 1 else [ls[:i] + [n-1] + ls[i:] for ls in gen_perms(n-1) for i in xrange(0, len(ls)+1)]

names.remove('Alice')
names = list(names)

orders = gen_perms(len(names))
for i in xrange(len(orders)):
    orders[i].append(len(names))
    orders[i].append(orders[i][0])

names.append('Alice')

def get_change(idx1, idx2):
    global names, change
    name1, name2 = names[idx1], names[idx2]
    return change[(name1, name2)] if (name1, name2) in change else change[(name2, name1)]

def get_net_change(order): return sum(get_change(order[i], order[i+1]) + get_change(order[i+1], order[i]) for i in xrange(len(order)-1))

print max(get_net_change(order) for order in orders) # 618

for name in names:
    change[('Me', name)] = 0
    change[(name, 'Me')] = 0

orders = gen_perms(len(names))
for i in xrange(len(orders)):
    orders[i].append(len(names))
    orders[i].append(orders[i][0])

names.append('Me')

print max(get_net_change(order) for order in orders) # 601