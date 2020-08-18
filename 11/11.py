from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def areaCal(i, j):
            return abs((i - j) * min(height[i], height[j]))

        res = 0
        start, end = 0, height.__len__() - 1
        # for i in range(start, end):
        #     for j in range(i, end):
        #         res = max(res, areaCal(i, j))
        while True:
            if start == end:
                break
            res = max(res, areaCal(start, end))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(s.maxArea(height))
