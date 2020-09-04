from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(filter(lambda x: x > 0, nums))
        if not nums:
            return 1
        # for count, val in enumerate(nums):
            # if 0 <= val <= len(nums) - 1 and nums[val - 1] != val:
            #     nums[val - 1], nums[count] = nums[count], nums[val - 1]
        for count in range(len(nums)):
            while 0 < nums[count] <= len(nums) - 1 and nums[nums[count] - 1] != nums[count]:
                nums[nums[count] - 1], nums[count] = nums[count], nums[nums[count] - 1]
        for check_count, check_val in enumerate(nums):
            if check_val != check_count + 1:
                return check_count + 1
            if check_count == len(nums) - 1:
                return check_count + 2


if __name__ == '__main__':
    # nums = [2, 2, 4, 0, 1, 3, 3, 3, 4, 3]
    nums = [0, 1, 3]
    s = Solution()
    print(s.firstMissingPositive(nums))
