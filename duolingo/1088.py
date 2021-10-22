class Solution:
    def confusingNumberII(self, n: int) -> int:
        confusingdigit = [0, 1, 6, 8, 9]
        res = set()
        self.dfs(res, [], confusingdigit, n)
        # return len(res)
        return res

    def dfs(self, res, path, confusingdigit, limitation):f
        tmp, flag = 0, False
        for i in range(len(path)):
            tmp = tmp * 10 + path[i]
        if tmp > limitation:
            path = path[:-1]
            tmp = 0
            for i in range(len(path)):
                tmp = tmp * 10 + path[i]

            res.add(tmp)

        for digit in confusingdigit:
            if path == [] and digit == 0:
                continue
            self.dfs(res, path + [digit], confusingdigit, limitation)



if __name__ == '__main__':
    s = Solution()
    print(s.confusingNumberII(20))