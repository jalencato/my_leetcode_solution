from functools import lru_cache
from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        @lru_cache(None)
        def pos_helper(len):
            if len == 0:
                return 0
            if len == 1:
                return 1 if nums[0] > 0 else 0
            if nums[len - 1] > 0:
                return pos_helper(len - 1) + 1
            if nums[len - 1] == 0:
                return 0
            if nums[len - 1] < 0:
                return neg_helper(len - 1) + 1 if neg_helper(len - 1) != 0 else 0

        @lru_cache(None)
        def neg_helper(len):
            if len == 0:
                return 0
            if len == 1:
                return 1 if nums[0] < 0 else 0
            if nums[len - 1] > 0:
                return neg_helper(len - 1) + 1 if neg_helper(len - 1) > 0 else 0
            if nums[len - 1] == 0:
                return 0
            if nums[len - 1] < 0:
                return pos_helper(len - 1) + 1

        res = 0
        for i in range(0, len(nums) + 1):
            res = max(res, pos_helper(i))
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [5, -20, -20, -39, -5, 0, 0, 0, 36, -32, 0, -7, -10, -7, 21, 20, -12, -34, 26, 2]
    print(len(nums))
    print(s.getMaxLen(nums))
