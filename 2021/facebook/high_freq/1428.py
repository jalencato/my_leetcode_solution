# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:
import math

class Solution2:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        nRow, nCol = binaryMatrix.dimensions()

        res = math.inf

        for r in range(nRow):
            left, right = 0, nCol-1
            border = -1
            while (left <= right):
                mid = (left + right) // 2
                temp = binaryMatrix.get(r,mid)
                if temp == 1:
                    right = mid - 1
                    border = mid
                else:
                    left = mid + 1
            if border > -1:
                res = min(res, border)


        return res if res < math.inf else -1

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        curr_row , curr_col = 0, cols - 1

        res = math.inf
        while curr_row < rows and curr_col > -1:
            if binaryMatrix.get(curr_row, curr_col) > 0:
                res = curr_col
                curr_col -= 1
            else:
                curr_row += 1

        return res if res != math.inf else -1


if __name__ == '__main__':
    mat = [[0,0],[1,1]]