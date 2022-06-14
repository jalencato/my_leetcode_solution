class Solution:
    def numWays(self, s: str) -> int:
        one_count, length = s.count('1'), len(s)
        if one_count % 3 != 0:
            return 0
        if one_count == 0:
            return ((length - 1) * (length - 2) // 2) % (10 ** 9 + 7)
        cnt, left, right = 0, float('inf'), float('inf')
        for ind, c in enumerate(s):
            if c == '1': cnt += 1
            if cnt == one_count//3: left = min(ind, left)
            if cnt == one_count//3: left_next = ind
            if cnt == (one_count//3) * 2: right = min(ind, right)
            if cnt == (one_count//3) * 2: right_next = ind
        left_count, right_count = s[left:left_next + 1].count('0'), s[right:right_next + 1].count('0')
        return (left_count + 1) * (right_count + 1) % (10 ** 9 + 7)


if __name__ == '__main__':
    s = Solution()
    input = "100100010100110"
    print(s.numWays(input))