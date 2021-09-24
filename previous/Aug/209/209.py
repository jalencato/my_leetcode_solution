from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        dp = [0]

        if not nums:
            return 0

        res = len(nums)
        for i in range(1, nums.__len__() + 1):
            cur = dp[i - 1]
            if cur > 0:
                update = sum(nums[i-cur-1:i])
                cnt = 0
                for j in range(i-cur-1, i+1):
                    if update - nums[j] >= s:
                        update -= nums[j]
                        cnt += 1
                    else: break
                dp.append(cur - cnt + 1)
            else:
                if sum(nums[0:i]) >= s:
                    update = sum(nums[0:i])
                    cnt = 0
                    for j in range(0, i + 1):
                        if update - nums[j] >= s:
                            update -= nums[j]
                            cnt += 1
                        else: break
                    dp.append(i - cnt)
                else:
                    dp.append(0)
        print(dp[1:])
        se = set(dp)
        se.remove(0)
        return min(se) if se else 0


if __name__ == '__main__':
    # s = 7
    # nums = [2, 3, 1, 2, 4, 3]
    s = 3
    nums = [1, 1]
    sol = Solution()
    print(sol.minSubArrayLen(s, nums))