from cmath import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return sqrt(pow(x[0] - y[0], 2) + pow(x[1] - y[1], 2))

        points.sort(key = lambda x: sqrt(x[0]*x[0]+x[1]*x[1]))
        return points[0:k]


if __name__ == '__main__':
    points = [[3,3],[5,-1],[-2,4]]
    k = 2

    s = Solution()
    print(s.kClosest(points, k))