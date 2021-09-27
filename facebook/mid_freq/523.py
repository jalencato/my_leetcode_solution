import collections
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dict = collections.defaultdict(int)
        dict[0] = -1
        sum = 0
        if len(nums) <= 1:
            return False
        if k == 0:
            return True
        for i, val in enumerate(nums):
            sum += val
            mod = sum%k
            if mod == 0 and i!=0:
                return True
            if mod not in dict:
                dict[mod] = i
            else:
                if i - dict[mod]>1:
                    return True
        return False


if __name__ == '__main__':
    nums = [5,0,0,0]
    k = 3
    sol = Solution()
    print(sol.checkSubarraySum(nums, k))
