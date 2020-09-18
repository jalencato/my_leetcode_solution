#tarjan algorithm
from collections import defaultdict
from typing import List

from pip._vendor.msgpack.fallback import xrange


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list) # graph
        parent = [-1] * (1 + n)
        low = [float('inf')] * (1 + n)
        # the smallest node that can visit without parent node
        dfn = [0] * (1 + n)
        # timestamp of parent node is smaller than child node
        self.time = 1
        res = []

        def tarjan(node):
            low[node] = self.time
            dfn[node] = self.time
            self.time += 1
            for vertex in g[node]:
                if not dfn[vertex]: # have not visited
                    parent[vertex] = node
                    tarjan(vertex)
                    low[node] = min(low[node], low[vertex])
                    if low[vertex] > dfn[node]:
                        res.append([node, vertex])
                elif vertex != parent[node]:
                    low[node] = min(low[node], dfn[vertex])

        for x, y in connections:
            g[x].append(y)
            g[y].append(x)

        for i in xrange(1, n + 1):
            if not dfn[i]:
                tarjan(i)
        return res


if __name__ == '__main__':
    s = Solution()
    n = 4
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
    print(s.criticalConnections(n, connections))