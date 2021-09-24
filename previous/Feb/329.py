from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[0 for j in range(len(matrix[0]))] for j in range(len(matrix))]
        dp[0][0] = 1
        res = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + 1 if matrix[i][j - 1] > matrix[i][j] else 1
                    continue
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + 1 if matrix[i - 1][j] > matrix[i][j] else 1
                    continue

                if matrix[i - 1][j] > matrix[i][j] and matrix[i][j - 1] > matrix[i][j]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + 1
                elif matrix[i - 1][j] > matrix[i][j] > matrix[i][j - 1]:
                    dp[i][j] = max(dp[i - 1][j], 0) + 1
                elif matrix[i - 1][j] < matrix[i][j] < matrix[i][j - 1]:
                    dp[i][j] = max(dp[i][j - 1], 0) + 1
                else:
                    dp[i][j] = 1
        for i in range(0, len(dp)):
            for j in range(0, len(dp[0])):
                res = max(res, dp[i][j])
        return res


if __name__ == '__main__':
    m = [[9,9,4],[6,6,8],[2,1,1]]
    s = Solution()
    print(s.longestIncreasingPath(m))