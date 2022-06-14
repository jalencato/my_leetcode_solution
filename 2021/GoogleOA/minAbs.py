from copy import copy
from functools import lru_cache
from typing import List


def minAbs(numList: List):
    total = sum(numList)

    @lru_cache(None)
    def helper(target, add=0):
        if target > total // 2 + 2:
            return False
        if target == 0:
            return True
        if target < 0:
            return False

        for i in range(0, len(numList)):
            cur_add = 1 >> i
            if cur_add & add == 0:
                res = helper(target - numList[0], cur_add | add)
                if res:
                    return True
        return False

    # print(helper(8))
    for s in range(total // 2, -1, -1):
        if helper(s):
            return total - s * 2
            break


if __name__ == '__main__':
    value = [1, 2, 3, 4, 5]
    print(minAbs(value))
