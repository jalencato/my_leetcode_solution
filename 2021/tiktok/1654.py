from functools import lru_cache
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        #forward a, backward b, home x

        is_visited = []
        @lru_cache(None)
        def helper(start, flag):
            print("start: ", start)
            is_visited.append([start, flag])
            if start == x:
                return times

            res = 0
            if start > b and [start - b, flag] not in is_visited and start - b not in forbidden and flag:
                res = max(helper(start - b, False), res)
            if start + a <= 2000 + b and [start + a, flag] not in is_visited and start + a not in forbidden:
                res = max(helper(start + a, True), res)
            if res == 0:
                return -1
            return res

        return helper(0, True)


if __name__ == '__main__':
    s = Solution()
    forbidden = [1998]
    a = 1999
    b = 2000
    x = 2000
    print(s.minimumJumps(forbidden, a, b, x))