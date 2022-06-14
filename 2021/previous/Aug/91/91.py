class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        if len(s) >= 1 and s[0] == '0':
            return 0
        elif len(s) == 1 or len(s) == 0:
            return 1
        res = res + self.numDecodings(s[1:])
        if int(s[0:2]) <= 26:
            res = res + self.numDecodings(s[2:])
        return res


if __name__ == '__main__':
    decode = '225'
    s = Solution()
    print(s.numDecodings(decode))