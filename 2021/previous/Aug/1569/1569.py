from functools import lru_cache
from typing import List


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        root = nums[0]
        up_order = []
        down_order = []
        for i in nums[1:]:
            if i > root:
                up_order.append(i)
            if i < root:
                down_order.append(i)
        if len(up_order) == 0 or len(down_order) == 0:
            return 0
        large = len(up_order) if len(up_order) > len(down_order) else len(down_order)
        tiny = len(up_order) if len(up_order) < len(down_order) else len(down_order)

        def multi(order):
            tmp_root = order[0]
            cnt = -1
            for i, val in enumerate(order):
                if val > tmp_root:
                    break
                cnt += 1
            if cnt == len(order) - 1:
                return 1
            elif len(order) == 2:
                return 1
            return multi(order[1:i]) * multi(order[i:]) * 2

        @lru_cache(None)
        def helper(large, tiny):
            res = 0
            if large == 1 and tiny > 0:
                return tiny
            if tiny == 0:
                return 1
            for k in range(0, large):
                res += helper(large - k, tiny - 1)
            return res

        return (helper(large + 1, tiny) * multi(up_order) * multi(down_order) - 1) % (10 ^ 9 + 7)


#组合数（选定位置） * 左子树的种类 * 右子树的种类
if __name__ == '__main__':
    s = Solution()
    nums = [9, 4, 2, 1, 3, 6, 5, 7, 8, 14, 11, 10, 12, 13, 16, 15, 17, 18]
    # nums = [3, 1, 2, 5, 4, 6]
    print(s.numOfWays(nums))
