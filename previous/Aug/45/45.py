from functools import lru_cache
from typing import List


# actually it is a greedy
class Solution:
    # Dp method:
    # def jump(self, nums: List[int]) -> int:
    #
    #     @lru_cache(None)
    #     def helper(dist):
    #         if dist == 0:
    #             return 0
    #         res = float('inf')
    #         for i in range(dist):
    #             tmp = i + nums[i]
    #             if tmp >= dist:
    #                 res = min(res, helper(i) + 1)
    #         return res
    #     return helper(len(nums) - 1)

    #Greedy Method:
    class Solution:
        def jump(self, arr: List[int]) -> int:
            jumps = 0
            cr = 0  # Current Range
            nr = 0  # Next Range
            i = 0
            while i <= cr:
                if i == len(arr) - 1:
                    return jumps
                nr = max(nr, arr[i] + i)
                if i == cr:
                    jumps += 1
                    cr = nr
                i += 1
            return -1

            
if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 1, 1, 1]
    print(s.jump(nums))
