import collections
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        res = []
        for i, account in enumerate(accounts):
            name, email_list = account[0], account[1:]
            for email in email_list:
                dic[email] += [i]
        print(dic)
        is_visited = [False] * len(accounts)

        def dfs(i, email):
            if is_visited[i]:
                return
            is_visited[i] = True
            for index in range(1, len(accounts[i])):
                if email.count(accounts[i][index]) == 0:
                    email.append(accounts[i][index])
                for neighbor in dic[accounts[i][index]]:
                    dfs(neighbor, email)

        for i, account in enumerate(accounts):
            if is_visited[i]:
                continue
            email = []
            dfs(i, email)
            print(sorted(email))
            res.append([account[0]]+sorted(email))
        return res


if __name__ == '__main__':
    sol = Solution()
    accounts = accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                           ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                           ["John", "johnnybravo@mail.com"]]
    print(sol.accountsMerge(accounts))
