from functools import lru_cache


class Solution:
    def lcs(self, tmp):
        first, second = tmp[0], tmp[1]

        @lru_cache()
        def helper(i, j):
            if i == 0 or j == 0:
                return 0, []
            if first[i - 1] == second[j - 1]:
                cnt, l = helper(i - 1, j - 1)
                l.append(first[i - 1])
                return cnt + 1, l
            else:
                return 0, []

        res = [-1, []]
        for i in range(len(first) + 1):
            for j in range(len(second) + 1):
                cnt, l = helper(i, j)
                if cnt > res[0]:
                    res[0], res[1] = cnt, l
        return res

        # dp = [[0 for i in range(len(second))] for j in range(len(first))]
        # for i in range(len(first)):
        #     for j in range(len(second)):


if __name__ == '__main__':
    tmp = [
        ["3234.html", "xys.html", "7hsaa.html"],
        ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"]
    ]

    s = Solution()
    print(s.lcs(tmp))