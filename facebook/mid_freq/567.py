import collections
from typing import List


class Solution:
    res = 0
    def subarraySum(self, nums: List[int], k: int) -> int:
        # is_visited = [False] * len(nums)
        # #for general
        # def backtrack(nums, is_visited, cur, target):
        #     # print(target)
        #     if target == 0:
        #         self.res += 1
        #         return
        #     if target < 0 or cur == len(nums):
        #         return
        #     is_visited[cur] = True
        #     backtrack(nums, is_visited, cur + 1, target - nums[cur])
        #     # print("res" + str(res))
        #     is_visited[cur] = False
        #     backtrack(nums, is_visited, cur + 1, target)
        #
        # backtrack(nums, is_visited, 0, k)
        # return self.res

    def subarraySum_On(self, nums: List[int], k: int) -> int:
        counter = collections.defaultdict(int)
        counter[0]=1

        cur_sum = 0
        ans = 0
        for j,num in enumerate(nums):
            cur_sum+= num
            ans += counter[cur_sum-k]
            counter[cur_sum]+=1

        return ans

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    k = 3
    print(s.subarraySum(nums, k))
