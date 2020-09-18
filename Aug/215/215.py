from collections import Counter
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        s = Counter(nums)

        cnt = 0
        for i in range(0, s.keys().__len__()):
            cur = max(s.keys())
            cnt += s[cur]
            s.pop(max(s.keys()))
            if cnt >= k:
                return cur
        return -1


if __name__ == '__main__':
    s = Solution()
    l = [3, 2, 3, 1, 2, 4, 5, 5, 7]
    k = 2
    print(s.findKthLargest(l, k))
