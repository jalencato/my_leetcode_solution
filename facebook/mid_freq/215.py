import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        stack = []
        for val in nums:
            heapq.heappush(stack, val)
            if len(stack) > k:
                heapq.heappop(stack)

        return stack[0]

if __name__ == '__main__':
    sol = Solution()
    nums = [3,2,1,5,6,4]
    print(sol.findKthLargest(nums, 2))