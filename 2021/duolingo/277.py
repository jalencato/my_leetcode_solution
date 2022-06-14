from functools import lru_cache


class Solution:
    def LCS(self, str_x, str_y):
        common_str, common_len = '', 0

        @lru_cache()
        def helper(len_x, len_y):
            if len_x == 0 or len_y == 0:
                return 0, ''
            if str_x[len_x - 1] == str_y[len_y - 1]:
                cnt, s = helper(len_x - 1, len_y - 1)
                return cnt + 1, s + str_x[len_x - 1]
            else:
                cnt, s = helper(len_x - 1, len_y) if helper(len_x - 1, len_y) > helper(len_x, len_y - 1) else helper(len_x, len_y - 1)
                return cnt, s

        return helper(len(str_x), len(str_y))



if __name__ == '__main__':
    str1 = "GeeksforGeeks"
    str2 = "GeeksQuiz"
    s = Solution()
    print(s.LCS(str1, str2))
