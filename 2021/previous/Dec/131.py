class Solution(object):
    def partition(self, s):
        self.res = []
        def helper(start, accu):
            if start == len(s):
                self.res.append(accu[::])
                return
            else:
                for end in range(start, len(s)):
                    word = s[start: end + 1]
                    if word == word[::-1]:
                        accu.append(word)
                        helper(end + 1, accu)
                        accu.pop()
        helper(0, [])
        return self.res


if __name__ == '__main__':
    str = "aab"
    s = Solution()
    print(s.partition(str))