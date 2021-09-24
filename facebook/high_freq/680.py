class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isvalid(s, left, right):
            while left<right:
                if s[left]!=s[right]:
                    return left, right
                left+=1
                right-=1
            return -1, -1

        start, end = 0, len(s) - 1
        st,ed= isvalid(s, start, end)
        if (st,ed)==(-1,-1):
            return True
        return isvalid(s,st+1, ed)==(-1,-1) or isvalid(s, st, ed-1)==(-1,-1)


if __name__ == '__main__':
    ss = 'abcd'

    s = Solution()
    print(s.validPalindrome(ss))