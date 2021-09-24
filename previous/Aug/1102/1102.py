from functools import lru_cache
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:

        @lru_cache(None)
        def helper(k):
            if k == 0:
                return 0
            if k == 1:
                return books[0][1]

            cur_width = books[k - 1][0]
            cur_height = books[k - 1][1]

            ret = cur_height + helper(k - 1)
            for cnt, b in enumerate(books[k - 2::-1]):
                cur_width += b[0]
                if cur_width > shelf_width:
                    break
                cur_height = max(cur_height, b[1])
                ret = min(ret, helper(k - 2 - cnt) + cur_height)
            return ret

        # return helper(books.__len__())
        return helper(4)


if __name__ == '__main__':
    s = Solution()
    # books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
    # shelf_width = 4
    books = [[7, 3], [8, 7], [2, 7], [2, 5]]
    shelf_width = 10
    print(s.minHeightShelves(books, shelf_width))
