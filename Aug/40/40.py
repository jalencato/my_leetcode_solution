# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        heap = []
        heapq.heapify(heap)
        heapq.heappush(heap, 1)

if __name__ == '__main__':
    s = Solution()