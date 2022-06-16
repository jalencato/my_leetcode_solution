import heapq
from collections import defaultdict, Counter
from functools import lru_cache

@lru_cache(None)
def dfs(city, fuel):
    return city + fuel + 1

# heapq
a = [1,2,3]
heapq.heapify(a)
heapq.heappop(a)
heapq.heappush(a, 4)

# defaultdict
places = defaultdict(list)
for i in reversed(range(len(a))):
    key = int(a[i])
    places[key].append(i)

# counter
cnt = Counter(a)

