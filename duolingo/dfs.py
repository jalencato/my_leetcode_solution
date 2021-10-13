# word v is said to derive from word w if v can be obtained by rearranging the letters in w
# and adding one more letter (e.g. two -> wout).
# Given a list of vocabulary and a word w, return all words in the vocabulary that can be derived from w
# (either direct derivation or indirect derivation, so there can be intermediate steps between w and v)
import string


class DFS_Template:
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


class Solution:
    def findDerived(self, s: str) -> str:
        import collections
        # letter = collections.defaultdict(list)
        letter = []
        # letter.append([l for l in s])
        for i in range(26):
            const = [l for l in s]
            const.append(chr(ord('a') + i))
            letter.append(const)

        def helper(pair, curIndex, res):
            tmp = []
            if not pair:
                return
            for i, let in enumerate(pair):
                tmp += helper(pair[0:i] + pair[i+1:], curIndex + 1, res.append(let))
            return tmp
        res = []
        for pair in letter:
            res += helper(pair, 0, [])

        return 1


if __name__ == '__main__':
    s = "abc"
    ss = Solution()
    print(ss.findDerived(s))
# Each word in the vocabulary has a value associated with it. Given (w, v),
# return the path whose sum of values are the largest.
