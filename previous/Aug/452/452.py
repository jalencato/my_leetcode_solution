from collections import deque
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        stack = deque()
        arrows = 0
        for p in points:
            if not stack:
                stack.append(p)
                arrows += 1
            elif stack[0][1] > p[0]:
                stack.append(p)
            else:
                stack.clear()
                arrows += 1
                stack.append(p)
        return arrows


if __name__ == '__main__':
    points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
    s = Solution()
    print(s.findMinArrowShots(points))
