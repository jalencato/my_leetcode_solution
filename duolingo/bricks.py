import copy


def validMoves(start, end):
    q = [(start, [])]
    while q:
        cur_state, path = q.pop(0)
        if cur_state == end:
            return path + [start]

        copy_cur_state = copy.deepcopy(cur_state)
        for i, val in enumerate(cur_state):
            if val == "_" and i != 0 and cur_state[i - 1] == "R":
                cur_state[i - 1], cur_state[i] = cur_state[i], cur_state[i - 1]
                q.append((copy.deepcopy(cur_state), path + [copy_cur_state]))
                cur_state[i - 1], cur_state[i] = cur_state[i], cur_state[i - 1]
            if val == "_" and i != len(copy_cur_state) - 1 and copy_cur_state[i + 1] == "B":
                cur_state[i + 1], cur_state[i] = cur_state[i], cur_state[i + 1]
                q.append((copy.deepcopy(cur_state), path + [copy_cur_state]))
                cur_state[i + 1], cur_state[i] = cur_state[i], cur_state[i + 1]

            if val == "R":
                if i >= 2 and cur_state[i - 1] == "B" and cur_state[i - 2] == "_":
                    cur_state[i - 2], cur_state[i] = cur_state[i], cur_state[i - 2]
                    q.append((copy.deepcopy(cur_state), path + [copy_cur_state]))
                    cur_state[i - 2], cur_state[i] = cur_state[i], cur_state[i - 2]
                if i <= len(cur_state) - 3 and cur_state[i + 1] == "B" and cur_state[i - 2] == "_":
                    cur_state[i + 2], cur_state[i] = cur_state[i], cur_state[i + 2]
                    q.append((copy.deepcopy(cur_state), path + [copy_cur_state]))
                    cur_state[i + 2], cur_state[i] = cur_state[i], cur_state[i + 2]

            if val == "B":
                if i >= 2 and cur_state[i - 1] == "R" and cur_state[i - 2] == "_":
                    cur_state[i - 2], cur_state[i] = cur_state[i], cur_state[i - 2]
                    q.append((copy.deepcopy(cur_state), path + [copy_cur_state]))
                    cur_state[i - 2], cur_state[i] = cur_state[i], cur_state[i - 2]
                if i <= len(cur_state) - 3 and cur_state[i + 1] == "R" and cur_state[i - 2] == "_":
                    cur_state[i + 2], cur_state[i] = cur_state[i], cur_state[i + 2]
                    q.append((copy.deepcopy(cur_state), path + [copy_cur_state]))
                    cur_state[i + 2], cur_state[i] = cur_state[i], cur_state[i + 2]
    return False


if __name__ == '__main__':
    start_1 = ["R", "_", "B", "B"]
    end_1 = ["B", "_", "B", "R"]

    # ['R', '_', 'B', 'B']
    # ['_', 'R', 'B', 'B']
    # ['B', 'R', '_', 'B']
    # ['B', 'R', 'B', '_']
    # ['B', '_', 'B', 'R']
    start_2 = ["R", "R", "_"]
    end_2 = ["_", "R", "R"]
    print(validMoves(start_1, end_1))
    # print(validMoves(start_2, end_2))
    # print(validMoves(start_1, start_1))
