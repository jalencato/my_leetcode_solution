from heapq import heappush, heappop


class Solution(object):
    def findKthLargest(self, nums, k):
        if not nums or len(nums) == 0:
            return -1

        topK = []

        # Iterate and push into minheap 
        for i in range(len(nums)):
            heappush(topK, nums[i])
            if len(topK) > k:
                heappop(topK)

            #return 0th element in topK which holds the kth largest element
        return topK[0]