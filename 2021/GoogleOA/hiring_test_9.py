# public static long backpack(int people, int groups) {
#     long[][] dp = new long[people + 1][groups + 1];                dp[0][0] = 1;
#     for (int i = 1; i <= people - groups + 1; ++i) {
#         for (int j = i; j <= people; ++j) {
#             for (int k = 1; k <= groups; ++k) {
#                 dp[j][k] += dp[j - i][k - 1];
#             }
#         }
#     }
#     return dp[people][groups];
# }
from functools import lru_cache


def backpack(people, group):
    dp = []

    dp[0][0] = 1
    for i in range(1, people - group + 2):
        for j in range(i, people + 1):
            for k in range(1, group):
                dp[j][k] += dp[j - i][k - 1];

    return dp[people][group]


class Solution(object):
    def grouping_options(self, n, k):
        """
        :type n: people
        :type k: group number
        :rtype: int
        """

        row_end = n
        col_end = k
        dp_list = [[0] * (col_end + 1) for _ in range(row_end + 1)]
        dp_list[0][0] = 1

        for i in range(1, row_end + 1):
            for j in range(1, min(col_end, i) + 1):
                dp_list[i][j] = dp_list[i - j][j] + dp_list[i - 1][j - 1]

        print(dp_list)
        return dp_list[-1][-1]

def main():
    n = 8
    k = 4
    solution = Solution()
    res = solution.grouping_options(n, k)
    print(res)

if __name__ == "__main__":
    main()


