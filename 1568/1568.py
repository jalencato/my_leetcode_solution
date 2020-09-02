import copy
from collections import deque
from itertools import product
from typing import List


# tarjan Algorithm
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        for i, j in product(range(len(grid)), range(len(grid[0]))):
            if grid[i][j] == 1:
                start = [i, j]
                break

        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # judge if there are more than two islands
        def helper(i, j):
            new_grid = copy.deepcopy(grid)

            queue = deque()
            queue.append(new_grid[i][j])
            while not queue:
                element = queue.popleft()
                new_grid[element[0]][element[1]] = 0
                for d in dir:
                    if 0 < element[0] + d[0] < len(new_grid) and 0 < element[1] + d[1] < len(new_grid[0]):
                        queue.append(new_grid[element[0] + d[0]][element[1] + d[1]])

            for val in new_grid:
                if val == 1:
                    return False
            return True

        if not helper(start[0], start[j]):
            return 0
        for a, b in product(range(len(grid)), range(len(grid[0]))):
            if grid[a][b] == 1:
                grid[a][b] == 0
                if not helper(i, j):
                    return 1
        return 2


if __name__ == '__main__':
    grid = [[0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]]
    s = Solution()
    print(s.minDays(grid))
