from functools import lru_cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        sumval = sum(nums)
        if sumval % 2 == 1:
            return False
        target = sumval / 2

        nums.sort(key=lambda x:-x)
        if nums[0] > target:
            return False

        @lru_cache(None)
        def helper(sum, is_add):
            if sum > target:
                return False
            if sum == target:
                return True
            for i in range(0, length):
                add = 1 << i
                if add & is_add == 0:
                    # return helper(sum + nums[i], add | is_add)
                    if helper(sum + nums[i], add | is_add):
                        return True

        return helper(0, 0)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    s = Solution()
    print(s.canPartition(nums))
