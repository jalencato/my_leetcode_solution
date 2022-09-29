import math
from collections import defaultdict


def is_valid(pnt, graph):
    x, y = pnt
    if x < 0 or x > len(graph) - 1 or y < 0 or y > len(graph) - 1:
        return False
    return True


def findOptimalPath(graph, time, cost, start, end):
    q, costMap, dir = [], defaultdict(int), [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for d in dir:
        nxt = tuple([x + y for x, y in zip(d, start)])
        if not is_valid(nxt, graph):
            continue
        x, y = nxt
        q.append(tuple((nxt, time[graph[x][y] - 1], cost[graph[x][y] - 1], set().union({nxt}), graph[x][y])))

    minStep, minCost, final_pattern = defaultdict(int), math.inf, []
    while q:
        cur, step_cur, cost_cur, visited, pattern = q.pop(0)
        if cur == end:
            if cur not in minStep:
                minStep[cur], minCost, final_pattern = step_cur, cost_cur, [pattern]
            else:
                if minStep[cur] < step_cur:
                    continue
                elif minStep[cur] == step_cur:
                    if minCost < cost_cur:
                        continue
                    elif minCost == cost_cur:
                        final_pattern.append(pattern)
                else:
                    minStep[cur], minCost, final_pattern = step_cur, cost_cur, [pattern]

        for d in dir:
            nxt = tuple([x + y for x, y in zip(d, cur)])
            x, y = nxt
            if not is_valid(nxt, graph) or (graph[x][y] != pattern and graph[x][y] != "D") or nxt in visited:
                continue
            if graph[x][y] == "D":
                q.append((nxt, step_cur + time[pattern - 1], cost_cur + cost[pattern - 1], visited.union({nxt}), pattern))
                continue
            q.append((nxt, step_cur + time[pattern - 1], cost_cur + cost[pattern - 1], visited.union({nxt}), pattern))
    return final_pattern




if __name__ == '__main__':
    graph = [[3, 3, "S", 2, "X", "X"],
             [3, 1, 1,   2, "X",  2],
             [3, 1, 1, 2, 2, 2],
             [3, 1, 1, 1, "D", 3],
             [3, 3, 3, 3, 3, 4],
             [4, 4, 4, 4, 4, 4]]
    time = [3, 2, 1, 1]
    cost = [0, 1, 3, 2]
    start, end = (0, 2), (3, 4)
    print(findOptimalPath(graph, time, cost, start, end))
    # should return 2