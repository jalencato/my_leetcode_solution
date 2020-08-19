from functools import lru_cache
from typing import List


class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        graph = [[] for i in range(n)]
        for road in roads:
            graph[road[0]].append(road[1])
            graph[road[1]].append(road[0])
        # Point target

        @lru_cache(None)
        def dp(path_length, node):
            if path_length == -1:
                return 0, None
            edit_difference = float('inf')
            res_node = None
            for adjacent in graph[node]:
                prev_length, prev_node = dp(path_length - 1, adjacent)
                if prev_length < edit_difference:
                    edit_difference = prev_length
                    res_node = adjacent
            if names[node] != targetPath[path_length]:
                edit_difference += 1
            return edit_difference, res_node

        mn = float('inf')
        end = None
        for i in range(n):
            dis, _ = dp(len(targetPath) - 1, i)
            if dis < mn:
                mn = dis
                end = i

        # here, we construct the path from end to start, and reverse the path
        path = [end]
        for idx in range(len(targetPath) - 1, 0, -1):
            _, end = dp(idx, end)
            path.append(end)
        return path[::-1]


if __name__ == '__main__':
    # n = 5
    # roads = [[0, 2], [0, 3], [1, 2], [1, 3], [1, 4], [2, 4]]
    # names = ["ATL", "PEK", "LAX", "DXB", "HND"]
    # targetPath = ["ATL", "DXB", "HND", "LAX"]
    n = 6
    roads = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
    names = ["ATL", "PEK", "LAX", "ATL", "DXB", "HND"]
    targetPath = ["ATL", "DXB", "HND", "DXB", "ATL", "LAX", "PEK"]
    s = Solution()
    print(s.mostSimilar(n, roads, names, targetPath))
