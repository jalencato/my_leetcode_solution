from itertools import combinations
from typing import List
from scipy.optimize import linprog

# class Solution:
#     def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
#         for k in range(len(requests), 0, -1):
#             for c in combinations(range(len(requests)), k):
#                 degree = [0] * n
#                 for i in c:
#                     degree[requests[i][0]] -= 1
#                     degree[requests[i][1]] += 1
#                 if not any(degree): # any means all the elements are false or 0
#                     return k
#         return 0

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        length = len(requests)

        cost = [-1] * length
        A = [[0 for i in range(length)] for j in range(n)]
        # the i-th line represents the information about the i-th building with out degree and in degree
        b = [0] * n
        for i, edge in enumerate(requests):
            A[edge[0]][i] -= 1
            A[edge[1]][i] += 1

        res = linprog(cost, A_eq=A, b_eq=b, bounds=(0, 1))

        return round(-res.fun)


if __name__ == '__main__':
    s = Solution()
    n = 3
    requests = [[0, 0], [1, 2], [2, 1]]
    print(s.maximumRequests(n, requests))