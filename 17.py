inp = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]

from collections import Counter
ways = Counter()

# expects 'buckets' to be pre-sorted
def combinations(target, buckets, buckets_used):
    global ways
    if target < 0 or sum(buckets) < target:
        return 0
    if target == 0:
        ways[buckets_used] += 1
        return 1
    combos_with = combinations(target - buckets[-1], buckets[:-1], buckets_used + 1)
    combos_without = combinations(target, buckets[:-1], buckets_used)
    return combos_with + combos_without

print(combinations(150, sorted(inp), 0), ways[min(ways)]) # 654 57