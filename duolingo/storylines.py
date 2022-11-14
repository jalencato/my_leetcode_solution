from collections import defaultdict, Counter


def mostRead(choices, ending):
    cnt = defaultdict(int)
    q, choice_pnt = [(1, [1], set({1}))], set()
    for ch in choices:
        choice_pnt.add(ch[0])

    while q:
        cur, path, is_visited = q.pop(0)
        if cur in ending:
            for ele in path:
                cnt[ele] += 1
            continue

        if cur not in choice_pnt:
            q.append((cur + 1, path + [cur + 1], is_visited.union({cur + 1})))
            continue

        for i, ch in enumerate(choices):
            ch_cur, nxt1, nxt2 = ch[0], ch[1], ch[2]
            if ch_cur != cur:
                continue
            if (ch_cur, nxt1) in is_visited and (ch_cur, nxt2) in is_visited:
                break
            if (ch_cur, nxt1) in is_visited:
                q.append((nxt2, path + [nxt2], is_visited.union({(ch_cur, nxt2)})))
            elif (ch_cur, nxt2) in is_visited:
                q.append((nxt1, path + [nxt1], is_visited.union({(ch_cur, nxt1)})))
            else:
                q.append((nxt2, path + [nxt2], is_visited.union({(ch_cur, nxt2)})))
                q.append((nxt1, path + [nxt1], is_visited.union({(ch_cur, nxt1)})))

    cnt = Counter(cnt)
    return cnt.most_common(1)[0]


if __name__ == '__main__':
    ending1 = [5, 10]
    choices1 = [[3, 7, 9], [9, 10, 8]]
    print(mostRead(choices1, ending1))