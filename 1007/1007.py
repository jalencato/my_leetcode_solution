from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        intersect = set(A).intersection(set(B))
        if len(set(A)) == 1 or len(set(B)) == 1:
            return 0
        if not intersect:
            return -1



        res = float('inf')
        for element in intersect:
            cnt_A = 0
            for i in range(0, len(A)):
                if A[i] != element:
                    cnt_A = cnt_A + 1 if B[i] == element else float('inf')
                    if cnt_A == float('inf'):
                        break

            cnt_B = 0
            for j in range(0, len(B)):
                if B[j] != element:
                    cnt_B = cnt_B + 1 if A[j] == element else float('inf')
                    if cnt_B == float('inf'):
                        break

            res = min(res, cnt_B, cnt_A)
        return res if res != float('inf') else -1


if __name__ == '__main__':
    # A = [2, 1, 2, 4, 2, 2]
    # B = [5, 2, 6, 2, 3, 2]
    A = [2]
    B = [1]
    s = Solution()
    print(s.minDominoRotations(A, B))
