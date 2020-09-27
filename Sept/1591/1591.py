from typing import List


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        def test(c):
            for i in range(pos[c][0], pos[c][2] + 1):
                for j in range(pos[c][1], pos[c][3] + 1):
                    if targetGrid[i][j] != 0 and targetGrid[i][j] != c:
                        return False
            for i in range(pos[c][0], pos[c][2] + 1):
                for j in range(pos[c][1], pos[c][3] + 1):
                    targetGrid[i][j] = 0
            return True

        l, r = len(targetGrid), len(targetGrid[0])
        pos = [[l, r, 0, 0] for i in range(61)] # m, n = 1 - 60
        colors = set()
        for i in range(l):
            for j in range(r):
                c = targetGrid[i][j]
                colors.add(c)
                pos[c][0] = min(pos[c][0], i) # left_min
                pos[c][1] = min(pos[c][1], j) # right_min
                pos[c][2] = max(pos[c][2], i) # left_max
                pos[c][3] = max(pos[c][3], j) # right_max

        while colors:
            colors_new = set()
            for c in colors:
                if not test(c):
                    colors_new.add(c)
            if colors == colors_new:
                return False
            colors = colors_new
        return True


if __name__ == '__main__':
    s = Solution()
    targetGrid = [[1, 1, 1, 1], [1, 1, 3, 3], [1, 1, 3, 4], [5, 5, 1, 4]]
    print(s.isPrintable(targetGrid))