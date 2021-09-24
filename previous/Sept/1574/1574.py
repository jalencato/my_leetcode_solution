from typing import List

#we can only remove one subarray
#so we can only consider the prefix and the suffix partion
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        return 0


if __name__ == '__main__':
    s = Solution()
    arr = [1, 2, 3]
    print(s.findLengthOfShortestSubarray(arr))