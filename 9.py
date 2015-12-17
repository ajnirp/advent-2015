inp = '''
AlphaCentauri to Snowdin = 66&&&
AlphaCentauri to Tambi = 28&&&
AlphaCentauri to Faerun = 60&&&
AlphaCentauri to Norrath = 34&&&
AlphaCentauri to Straylight = 34&&&
AlphaCentauri to Tristram = 3&&&
AlphaCentauri to Arbre = 108&&&
Snowdin to Tambi = 22&&&
Snowdin to Faerun = 12&&&
Snowdin to Norrath = 91&&&
Snowdin to Straylight = 121&&&
Snowdin to Tristram = 111&&&
Snowdin to Arbre = 71&&&
Tambi to Faerun = 39&&&
Tambi to Norrath = 113&&&
Tambi to Straylight = 130&&&
Tambi to Tristram = 35&&&
Tambi to Arbre = 40&&&
Faerun to Norrath = 63&&&
Faerun to Straylight = 21&&&
Faerun to Tristram = 57&&&
Faerun to Arbre = 83&&&
Norrath to Straylight = 9&&&
Norrath to Tristram = 50&&&
Norrath to Arbre = 60&&&
Straylight to Tristram = 27&&&
Straylight to Arbre = 81&&&
Tristram to Arbre = 90
'''

dist = {}
names = set()

for line in inp.split('&&&'):
	place1, _, place2, _, val = line.split()
	dist[(place1, place2)] = int(val)
	names.add(place1)
	names.add(place2)

names = list(names)

# generate a list of lists, where each list
# is a permutation of [0, 1, 2, ..., n-1]
def gen_perms(n): return [[0]] if n == 1 else [ls[:i] + [n-1] + ls[i:] for ls in gen_perms(n-1) for i in xrange(0, len(ls)+1)]

paths = gen_perms(8)

def get_dist(idx1, idx2):
	global names, dist
	place1, place2 = names[idx1], names[idx2]
	return dist[(place1, place2)] if (place1, place2) in dist else dist[(place2, place1)]

def get_path_dist(path): return sum(get_dist(path[i], path[i+1]) for i in xrange(len(path)-1))

print min(get_path_dist(path) for path in paths) # 141

print max(get_path_dist(path) for path in paths) # 736
