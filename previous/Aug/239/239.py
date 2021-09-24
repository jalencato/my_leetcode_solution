from typing import List
import heapq

# #deque
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         # h = map(lambda x: nums[x] if 0 <= x < k, nums)
#         h = [nums[x] for x in range(k)]
#         heapq.heapify(h)
#
#         res = []
#         for count, val in enumerate(nums):
#             if count < k - 1:
#                 continue
#             if count == k - 1:
#                 res.append(max(h))
#             if count >= k:
#                 heapq.heappop(h)
#                 heapq.heappush(h, val)
#                 res.append(max(h))
#         return res
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums) or not nums:
            return []

        ret = []
        q = deque()

        for i in range(len(nums)):
            # remove everything from the back that is <= the current num
            while q and q[-1][0] <= nums[i]:
                q.pop()
            # add the new num to the back
            q.append((nums[i], i))
            # remove everything from the front if it's not in the window
            while q[0][1] <= i - k:
                q.popleft()
            # start adding results to output array once we have our first size k window
            if i >= k - 1:
                ret.append(q[0][0])

        return ret


if __name__ == '__main__':
    nums = [7, 2, 4]
    k = 2
    s = Solution()
    print(s.maxSlidingWindow(nums, k))