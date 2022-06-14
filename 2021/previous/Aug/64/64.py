from collections import deque
from functools import lru_cache
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        stack = deque()
        stack.append([grid[0][0], 0, 0, 0])
        #val pos_x pos_y cur_Sum
        m = grid.__len__()
        n = grid[0].__len__()

        @lru_cache(None)
        def helper(x, y):
            if x == 0 and y == 0:
                return grid[x][y]
            if x == 0 and y > 0:
                return grid[x][y] + helper(x, y - 1)
            if y == 0 and x > 0:
                return grid[x][y] + helper(x - 1, y)
            if x > 0 and y > 0:
                return min(grid[x][y] + helper(x - 1, y), grid[x][y] + helper(x, y - 1))
        return helper(m - 1, n - 1)
        # maxSum = 99999999999
        # while stack:
        #     s = stack.pop()
        #     cur_x = s[1]
        #     cur_y = s[2]
        #     cur_Sum = s[0] + s[3]
        #     if cur_x + 1 < m:
        #         stack.append([grid[cur_x + 1][cur_y], cur_x + 1, cur_y, cur_Sum])
        #     if cur_y + 1 < n:
        #         stack.append([grid[cur_x][cur_y + 1], cur_x, cur_y + 1, cur_Sum])
        #     if cur_x == m - 1 and cur_y == n - 1:
        #         maxSum = min(cur_Sum, maxSum)
        # return maxSum

if __name__ == '__main__':
    s = Solution()
    grid = [
        [1, 2, 5],
        [3, 2, 1]
    ]
    print(s.minPathSum(grid))