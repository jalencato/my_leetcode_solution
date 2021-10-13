def helper(pair, curIndex, res):
    tmp = []
    if len(pair) == 1:
        return [l + pair[0] for l in res] if res != [] else [pair[0]]
    index = curIndex + 1
    for i, let in enumerate(pair):
        tmp += helper(pair[0:i] + pair[i + 1:], index, res.append(let))
    return tmp


print(helper(['ab'], 0, ['']))
