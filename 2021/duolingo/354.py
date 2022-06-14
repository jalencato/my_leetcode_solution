from functools import lru_cache
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        print(envelopes)
        width = [k[0] for k in envelopes]
        height = [k[1] for k in envelopes]

        @lru_cache()
        def helper(num):
            if num == 0:
                return 1
            cnt = 0

                # if height[num] > height[i] and width[num] > width[i]:
                #     cnt = max(cnt, helper(i) + 1)
            return cnt

        res = [helper(i) for i in range(len(envelopes))]
        return max(res)


if __name__ == '__main__':
    envelopes = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
    s = Solution()
    print(s.maxEnvelopes(envelopes))