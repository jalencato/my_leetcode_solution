#2
m = 3
n = 3
dp = []
dp = [[0 for j in range(n)] for m in range(m)]
def part_sum():
    dp[0][0] = arr[0][0]

    for i in range(0, m):
        dp[i][0] = dp[i - 1][0] + arr[i][0]

    for j in range(0, n):
        dp[0][j] = dp[0][j - 1] + arr[0][j]

    for i in range(1, m):
        for j in range(1, n):
            rem = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]
            dp[i][j] = rem + arr[i][j]

    print(dp)

def sum_submatrix(pointer_1, pointer_2):
    x_min = pointer_1[0]
    x_max = pointer_2[0]

    y_min = pointer_1[1]
    y_max = pointer_2[1]

    if x_min < 0 or x_max >= m:
        return None
    if y_min < 0 or y_max >= n:
        return None

    # #1
    # res = 0
    # for i in range(x_min, x_max + 1):
    #     for j in range(y_min, y_max + 1):
    #        res += arr[i][j]

    #2
    if x_min == 0 and y_min == 0:
        res = dp[x_max][y_max]
    elif x_min == 0 and y_min != 0:
        res = dp[x_max][y_max] - dp[x_max][y_min - 1]
    elif x_min != 0 and y_min == 0:
        res = dp[x_max][y_max] - dp[x_min - 1][y_max]
    else:
        res = dp[x_max][y_max] - dp[x_min - 1][y_max] - dp[x_max][y_min - 1] + dp[x_min - 1][y_min - 1]

    return res

if __name__ == '__main__':
    arr = [[1,2,3], [4,5,6], [7,8,9]]
    part_sum()
    print(sum_submatrix([0,0], [0,1]))