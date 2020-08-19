import heapq
from typing import List


class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = [[0 for _ in range(M)] for _ in range(M)]
        print(graph.__len__())
        for edge in edges:
            graph[edge[0]][edge[1]] = edge[2]
            graph[edge[1]][edge[0]] = edge[2]


        path = [(0, 0)]
        visited = [False] * M

        while not path:
            node = heapq.heappop(path)
        return 1


if __name__ == '__main__':
    s = Solution()
    edges = [[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]]
    M = 10
    N = 4
    print(s.reachableNodes(edges, M, N))