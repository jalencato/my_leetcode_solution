class Solution:
    def numberOfSteps (self, num: int) -> int:
        cnt = 0
        val = num
        while val != 0:
            if val % 2 == 0:
                cnt += 1
                val /= 2
            else:
                cnt += 1
                val -= 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSteps(123))