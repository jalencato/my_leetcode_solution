import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        vertices, conn = len(points), defaultdict(list)
        for i in range(vertices):
            for j in range(i + 1, vertices):
                dis = manhattan(points[i], points[j])
                conn[i].append((dis, j))
                conn[j].append((dis, i))

        cnt, ans, visited, heap = 1, 0, [False for i in range(vertices)], conn[0]
        visited[0] = True
        heapq.heapify(heap)
        while heap:
            dis, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt, ans = True, cnt + 1, ans + dis
                for path in conn[j]:
                    heapq.heappush(heap, path)
                if cnt >= vertices:
                    break
        return ans


if __name__ == '__main__':
    s = Solution()
    points = [[3, 12], [-2, 5], [-4, 1]]
    print(s.minCostConnectPoints(points))