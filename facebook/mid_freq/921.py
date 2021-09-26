class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        s_fix = [k for k in s if k=='(' or k==')']
        stack = []
        right_count = 0
        for i in range(0,s_fix.__len__()):
            if s_fix[i] == '(':
                stack.append(s_fix[i])
            if s_fix[i] == ')':
                if len(stack):
                    stack.pop()
                else:
                    right_count += 1

        stack = []
        left_count = 0
        for j in range(0, s_fix.__len__()):
            if s_fix[len(s_fix) - j - 1] == ')':
                stack.append(')')
            if s_fix[len(s_fix) - j - 1] == '(':
                if len(stack):
                    stack.pop()
                else:
                    left_count += 1

        return left_count + right_count


if __name__ == '__main__':
    sol = Solution()
    st = '()))(('
    print(sol.minAddToMakeValid(st))
