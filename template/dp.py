from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        n = len(nums)
        nums.append(1)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for dist in range(2, n + 2):
            for left in range(-1, n - dist + 1):
                right = left + dist
                max_coin = float('-inf')
                left_right = nums[left] * nums[right]
                for j in range(left + 1, right):
                    max_coin = max(max_coin, left_right * nums[j] + dp[left][j] + dp[j][right])
                dp[left][right] = max_coin
        nums.pop()
        return dp[-1][n]