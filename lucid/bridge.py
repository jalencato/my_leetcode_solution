from collections import defaultdict

initialCountdown = 5
colorMap, countMap = defaultdict(str), defaultdict(int)


def is_valid(point, board):
    x, y = point
    if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
        return False
    return True


def checkSameColor(x, y, state, board):
    dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for d in dir:
        nxt = tuple([x + y for x, y in zip((x, y), d)])
        nxt_x, nxt_y = nxt
        if not is_valid(nxt, board):
            continue
        if board[nxt_x][nxt_y] == state:
            if (x, y) in countMap:
                countMap.pop((x, y))
            if nxt in countMap:
                countMap.pop(nxt)


def countDown(board):
    delset = set()
    for k, v in countMap.items():
        if v != 1:
            countMap[k] = v - 1
        elif v == 1:
            x, y = k
            delset.add(k)
            dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for d in dir:
                nxt = tuple([x + y for x, y in zip((x, y), d)])
                if not is_valid(nxt, board):
                    continue
                nxt_x, nxt_y = nxt
                if board[nxt_x][nxt_y] == 'grey':
                    continue
                delset.add((nxt_x, nxt_y))
    for pnt in delset:
        pnt_x, pnt_y = pnt
        board[pnt_x][pnt_y] = 'grey'
        if pnt in countMap:
            del countMap[pnt]


def restartTimer(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'grey' or (i, j) in countMap:
                continue
            dir, found = [(-1, 0), (1, 0), (0, 1), (0, -1)], False
            for d in dir:
                nxt = tuple([x + y for x, y in zip((i, j), d)])
                if not is_valid(nxt, board):
                    continue
                nxt_x, nxt_y = nxt
                if board[nxt_x][nxt_y] == board[i][j]:
                    found = True
                    break
            if not found:
                countMap[(i, j)] = initialCountdown - 1


def checkWin(board):
    blackcluster, redcluster = [], []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'grey':
                continue
            elif board[i][j] == 'black':
                if len(blackcluster) == 0:
                    blackcluster.append([(i, j)])
                    continue
                clusterIndex = []
                for index, bc in enumerate(blackcluster):
                    for node in bc:
                        bcx, bcy = node
                        x_diff, y_diff = abs(bcx - i), abs(bcy - j)
                        if (x_diff == 1 and y_diff == 0) or (x_diff == 0 and y_diff == 1):
                            clusterIndex.append(index)
                            break
                if len(clusterIndex) == 0:
                    blackcluster.append([(i, j)])
                elif len(clusterIndex) == 1:
                    if (i, j) not in blackcluster[clusterIndex[0]]:
                        blackcluster[clusterIndex[0]].append((i, j))
                else:
                    res = []
                    for ii in clusterIndex:
                        res += blackcluster[ii]
                    for ii in clusterIndex:
                        blackcluster[ii] = []
                    blackcluster = [x for x in blackcluster if x != []]
            elif board[i][j] == 'red':
                if len(redcluster) == 0:
                    redcluster.append([(i, j)])
                    continue
                clusterIndex = []
                for index, bc in enumerate(blackcluster):
                    for node in bc:
                        bcx, bcy = node
                        x_diff, y_diff = abs(bcx - i), abs(bcy - j)
                        if (x_diff == 1 and y_diff == 0) or (x_diff == 0 and y_diff == 1):
                            clusterIndex.append(index)
                            break
                if len(clusterIndex) == 0:
                    redcluster.append([(i, j)])
                elif len(clusterIndex) == 1:
                    if (i, j) not in redcluster[clusterIndex[0]]:
                        redcluster[clusterIndex[0]].append((i, j))
                else:
                    res = []
                    for ii in clusterIndex:
                        res += redcluster[ii]
                    for ii in clusterIndex:
                        redcluster[ii] = []
                    redcluster = [x for x in redcluster if x != []]
    for cluster in blackcluster:
        flag_start, flag_end = False, False
        for c in cluster:
            _, cy = c
            if cy == 0:
                flag_start = True
            elif cy == len(board) - 1:
                flag_end = True
        if flag_end and flag_start:
            print("black win")
    for cluster in redcluster:
        flag_start, flag_end = False, False
        for c in cluster:
            cx, _ = c
            if cx == 0:
                flag_start = True
            elif cx == len(board[0]) - 1:
                flag_end = True
        if flag_end and flag_start:
            print("red win")


def mouseClick(x, y, state, board):
    if board[x][y] != "grey":
        return -1
    board[x][y], countMap[(x, y)] = state, initialCountdown
    checkSameColor(x, y, state, board)
    countDown(board)
    restartTimer(board)
    checkWin(board)
    return


if __name__ == '__main__':
    board = [["grey", "grey", "grey", "grey"],
             ["grey", "grey", "grey", "grey"],
             ["grey", "grey", "grey", "grey"],
             ["grey", "grey", "grey", "grey"]]
    mouseClick(0, 0, "black", board)
    mouseClick(0, 1, "black", board)
    mouseClick(1, 2, "black", board)
    mouseClick(0, 2, "black", board)
    mouseClick(0, 3, "black", board)
