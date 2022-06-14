class Solution:
    def find_path(self, matrix, i, j):


if __name__ == '__main__':
    board1 = [
        [ 0, -1, 0, 0 ],
        [ 0, 0, -1, 0 ],
        [ 0, 0, 0, -1 ]
    ]
    board3 = [
        [ 1, 0, 0, 0, 0 ],
        [ 0, -1, -1, 0, 0 ],
        [ 0, -1, 0, 1, 0 ],
        [ -1, 0, 0, 0, 0 ],
        [ 0, 1, -1, 0, 0 ],
        [ 0, 0, 0, 0, 0 ],
    ]

    s = Solution()
    print(s.find_path(board3, i, j))