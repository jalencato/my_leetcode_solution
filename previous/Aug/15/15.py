class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    ans = [nums[i], nums[left], nums[right]]
                    if res and res.count(ans) != 0:
                        left += 1
                        pass
                    else:
                        res.append(ans)
                if sum > 0:
                    right -= 1
                if sum < 0:
                    left += 1
        return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [1, 0, -1]
    s = Solution()
    print(s.threeSum(nums))