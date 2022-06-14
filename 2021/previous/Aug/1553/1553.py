from functools import lru_cache
from typing import List


class Solution:
    # def minDays(self, n: int) -> int:
    #     def eat(num: int, dp: List):
    #         if num % 6 == 0:
    #             return min(dp[num-1], dp[num//2], dp[num//3])
    #         elif num % 3 == 0:
    #             return min(dp[num-1], dp[num//3])
    #         elif num % 2 == 0:
    #             return min(dp[num-1], dp[num//2])
    #         else:
    #             return dp[num-1]
    #
    #     num = n
    #     dp = [0] * (num + 1)
    #     dp[1] = 1
    #     for i in range(0, num + 1):
    #         if i == 1 or i == 0:
    #             continue
    #         residue = eat(i, dp)
    #         dp[i] = residue + 1
    #     return dp[num]

    @lru_cache
    def minDays(self, n: int) -> int:

        @lru_cache(None)
        def helper(n):
            if n < 2:
                return n
            return 1 + min(n%2 + helper(n//2), n%3 + helper(n//3))
        return helper(n)

if __name__ == '__main__':
    s = Solution()
    print(7//2)
    print(s.minDays(1))
    print(s.minDays(9))
    print(s.minDays(10))
    print(s.minDays(56))