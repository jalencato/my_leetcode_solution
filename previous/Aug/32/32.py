from collections import deque


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        start = 0
        res = 0

        stack = deque()
        for index, cc in enumerate(s):
            if cc == '(':
                stack.append(index)
            else:
                if len(stack) != 0:
                    stack.pop()
                    if len(stack) != 0:
                        res = max(res, index - stack[-1])
                    else:
                        res = max(res, index - start + 1)
                else:
                    start = index + 1
        return res

if __name__ == '__main__':
    s = Solution()
    str = ")()"
    print(s.longestValidParentheses(str))