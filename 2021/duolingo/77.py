from typing import List


class Solution:
    def combine(self, n, k):
        res = []
        if k == 0:
            return
        if k == 1:
            return [[l] for l in range(1, n+1)]
        self.dfs(res, [], 0, range(1, n+1), k)
        return res

    def dfs(self, res, path, index, number, times):
        if times == 0:
            res.append(path)
            return
        for i in range(index, len(number)):
            self.dfs(res, path+[number[i]], number[i], number, times - 1)

    # def combine(self, n, k):
    #     res = [] #1
    #     self.dfs(range(1,n+1), k, 0, [], res) #2
    #     return res #3
    #
    # def dfs(self, nums, k, index, path, res):  #4
    #     print('index is:', index)
    #     print('path is:', path)
    #     if k == 0:  #7
    #         res.append(path)  #8
    #         return # backtracking  #9
    #     for i in range(index, len(nums)):  #10
    #         self.dfs(nums, k-1, i+1, path+[nums[i]], res)


if __name__ == '__main__':
    n = 4
    k = 2
    s = Solution()
    print(s.combine(n, k))
