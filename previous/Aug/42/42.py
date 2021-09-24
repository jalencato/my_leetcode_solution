# Trapping the water
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        def find_leftMax(pos):
            res = 0
            for left_iter in range(0, pos):
                if not dp[left_iter]:
                    res = max(res, height[left_iter])
            return res

        def find_rightMax(pos):
            res = 0
            for right_iter in range(pos + 1, len(height)):
                if not dp[right_iter]:
                    res = max(res, height[right_iter])
            return res

        dp = []
        for i in height:
            if i > 0:
                dp.append(False)
            else:
                dp.append(True)

        res = 0
        for j, k in enumerate(dp):
            if j == 0 or j == dp.__len__() - 1:
                continue

            leftMax, rightMax = [0], [0]
            # use left_max or right_max array instead of function call
            left_max = find_leftMax(j)
            right_max = find_rightMax(j)
            res = res + min(left_max, right_max) - height[j] if min(left_max, right_max) > height[j] else res
        return res


if __name__ == '__main__':
    s = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trap(height))
