from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def make_suit(val: int):
            start = 1
            res = 1
            for i in range(1, m):
                if List[i] - List[start] >= val:
                    start = i
                    res += 1
            return res

        max = List[-1] - List[0]
        iter = max
        if make_suit(iter) < m:
            return 1