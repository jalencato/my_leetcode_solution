from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = []
        for i in range(0, len(nums)):
            res.append(nums[i])

        for i in range(1, len(nums)):
            res[i] = max(res[i - 1] + nums[i], nums[i])

        return max(res)


if __name__ == '__main__':
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray(nums))