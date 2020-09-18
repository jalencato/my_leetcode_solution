from collections import deque


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mark = deque()
        maxlength = 0
        for i in range(0, len(s)):
            if s[i] not in mark:
                mark.append(s[i])
                maxlength = max(maxlength, len(mark))
            elif s[i] in mark and deque:
                k = mark.popleft()
                while k != s[i]:
                    k = mark.popleft()
                mark.append(s[i])
        return maxlength


if __name__ == '__main__':
    s = Solution()
    string = "ohvhjdml"
    print(s.lengthOfLongestSubstring(string))