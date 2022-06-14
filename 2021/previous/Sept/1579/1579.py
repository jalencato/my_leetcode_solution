from collections import defaultdict
from typing import List


# DSU disjoint set union
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_graph, bob_graph = defaultdict(list), defaultdict(list)

        def find(tree, x):
            if tree[x] != x:
                tree[x] = find(tree, tree[x])
            return tree[x]

        def union(tree, x, y):
            root_x = find(tree, x)
            root_y = find(tree, y)
            tree[root_x] = root_y

        # union common, then union A and union B throw each edge that still maintains the connectivity
        return 0


if __name__ == '__main__':
    s = Solution()
    n = 4
    # type ui vi
    edges = [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]
    print(s.maxNumEdgesToRemove(n, edges))
