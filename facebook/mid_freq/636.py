import collections
from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = collections.defaultdict(int)
        cur_time = 0
        for log in logs:
            log = log.split(':')
            if log[1] == 'start':
                if stack:
                    res[stack[-1]] += int(log[2]) - cur_time
                stack.append(int(log[0]))
                cur_time = int(log[2])
            else:
                res[stack.pop()] += int(log[2]) - cur_time + 1
                cur_time = int(log[2]) + 1
            # print(res, stack, cur_time)
        return list(res.values())


if __name__ == '__main__':
    n = 1
    logs = ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]
    sol = Solution()
    print(sol.exclusiveTime(n, logs))
