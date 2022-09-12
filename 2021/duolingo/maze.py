inital = ["south", "east", "east", "south", "south", "west", "west", "east", "east", "south"]

# inital = ["south", "south", "south", "east", "east", "east", "east", "east", "south", "south", "west", "west",
#           "west", "west", "west", "south", "south", "east", "east", "north", "north", "east", "east", "east",
#           "north", "north", "west", "west", "west", "west", "west", "north", "north", "east", "east", "east",
#           "east", "east", "east", "east", "south", "south", "south", "south", "south", "south", "south", "south"]

# inital = ["south", "south", "south", "south", "east", "north", "east", "south", "east", "north", "north", "east"]
def helper():
    # build map
    visited = set()
    cur = (0, 0)
    visited.add(cur)

    for dir in inital:
        if dir == "south":
            x, y = cur
            cur = (x, y - 1)
            visited.add(cur)
        elif dir == "north":
            x, y = cur
            cur = (x, y + 1)
            visited.add(cur)
        elif dir == "east":
            x, y = cur
            cur = (x + 1, y)
            visited.add(cur)
        elif dir == "west":
            x, y = cur
            cur = (x - 1, y)
            visited.add(cur)

    end, cur = cur, (0, 0)
    q = [[cur, [cur], set()]]
    q[0][2].add(cur)

    while q:
        cur, path, is_visited = q.pop(0)
        if cur == end:
            return path
        for dir in [[[0, 1], "north"], [[0, -1], "south"], [[1, 0], "east"], [[-1, 0], "west"]]:
            dir, way = dir[0], dir[1]
            nxt = (cur[0] + dir[0], cur[1] + dir[1])
            if nxt not in visited or nxt in is_visited:
                continue
            is_visited.add(nxt)
            q.append([nxt, path + [way], is_visited])


if __name__ == '__main__':
    print(helper())
