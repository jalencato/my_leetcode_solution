class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        stack = []
        number = ''
        for l in s:
            print(l)
            if l.isdigit():
                number += l
                continue
            number = int(number)
            if l == '+':
                res += number
            elif l == '-':
                res -= number
            number = ''
            print(res)
        return res

if __name__ == '__main__':
    expression = "1+1"
    # expression = "2*(5+5*2)/3+(6/2+8)"
    s = Solution()
    print(s.calculate(expression))