from functools import lru_cache
from typing import List


class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        l, r = len(cost), len(cost[0])
        cost = []
        return 1


if __name__ == '__main__':
    s = Solution()
    cost = [[15, 96], [36, 2]]
    print(s.connectTwoGroups(cost))
