from collections import Counter
from typing import List


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        if nums.__len__() % k != 0:
            return -1
        count = Counter(nums)
        print(count)

        return 0


if __name__ == '__main__':
    s = Solution()
    nums = [6, 3, 8, 1, 3, 1, 2, 2]
    k = 4
    print(s.minimumIncompatibility(nums, k))
