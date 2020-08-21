from functools import lru_cache
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sumStone = sum(stones)

        @lru_cache(None)
        def helper(sum, add):
            if sum > sumStone / 2:
                return -1
            if sum == sumStone / 2:
                return 0
            # add

        return helper(sum/2, )


if __name__ == '__main__':
    l = [2, 7, 4, 1, 8, 1]
    s = Solution()
    print(s.lastStoneWeightII(l))
