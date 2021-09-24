class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]
        curr = 0
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] != text2[j - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    continue
                dp[i][j] = dp[i - 1][j - 1] + 1
                curr = max(dp[i][j], curr)
        print(dp)
        return curr


if __name__ == '__main__':
    text1 = "abc"
    text2 = "def"
    s = Solution()
    print(s.longestCommonSubsequence(text1, text2))