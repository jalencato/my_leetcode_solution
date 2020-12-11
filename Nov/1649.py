from typing import List


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        N = max(instructions)
        cc = [0] * (N + 1)

        def update(x):
            while x <= N:
                cc[x] += 1
                x += -x & x

        def query(x):
            ans = 0
            while x > 0:
                ans += cc[x]
                x -= -x & x
            return ans

        ans = 0
        for i, n in enumerate(instructions):
            ans += min(query(n - 1), i - query(n))
            update(n)
        return ans % (10^7)


    def BIT(self, val: List[int], n) -> int:
        num = [0] * (n + 1)

        def prefixSum(ind):
            res = 0
            while(ind > 0):
                res += num[ind]
                ind -= ind & (-ind)# remove the lowest bit of the num value
            return res

        def rangeSum(min, max):
            return prefixSum(max) - prefixSum(min - 1)