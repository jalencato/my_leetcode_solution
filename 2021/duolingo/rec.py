from functools import lru_cache


class Solution:
    def ret_matrix(self, matrix):
        pos = []
        cow, row = len(matrix), len(matrix[0])
        is_visited = [[False for j in range(row)] for i in range(row)]
        print(is_visited)
        for i in range(cow):
            for j in range(row):
                if matrix[i][j] == 1:
                    is_visited[i][j] = True

        def dfs(i, j):
            col_tmp, row_tmp = i, j
            while col_tmp < cow and matrix[col_tmp][j] == 0 and not is_visited[col_tmp][j]:
                col_tmp += 1
            while row_tmp < row and matrix[i][row_tmp] == 0 and not is_visited[i][row_tmp]:
                row_tmp += 1
            for iter_x in range(i, col_tmp):
                for iter_y in range(j, row_tmp):
                    is_visited[iter_x][iter_y] = True
            return col_tmp - 1, row_tmp - 1

        for i in range(cow):
            for j in range(row):
                if not is_visited[i][j]:
                    x, y = dfs(i, j)
                    pos.append([i, j, x, y])
        return pos


if __name__ == '__main__':
    matrix = [
        [1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 1, 0, 1, 0],
        [1, 0, 0, 1, 1, 1]
    ]
    s = Solution()
    print(s.ret_matrix(matrix))
