class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        dic = {
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "0":0
        }

        n1 = sum([dic[num1[len(num1) - i - 1]]*(10**i) for i in range(len(num1))])
        n2 = sum([dic[num2[len(num2) - i - 1]]*(10**i) for i in range(len(num2))])
        return str(n1+n2)

class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:

        i = 0
        n = len(num1)
        m = len(num2)
        add = 0
        ans = ""
        while(i < n and i < m):
            x = ord(num1[n-1-i]) - ord("0")
            y = ord(num2[m-1-i]) - ord("0")
            t = x + y + add
            add = t // 10
            ans = str(t % 10) + ans
            i += 1

        while(i < n):
            x = ord(num1[n-1-i]) - ord("0")
            t = x + add
            add = t // 10
            ans = str(t % 10) + ans
            i += 1

        while(i < m):
            x = ord(num2[m-1-i]) - ord("0")
            t = x + add
            add = t // 10
            ans = str(t % 10) + ans
            i += 1

        if add:
            ans = str(add) + ans

        return ans