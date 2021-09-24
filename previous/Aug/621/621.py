from collections import defaultdict, Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # print(tasks[0])
        # task_dict = defaultdict(list)
        # for i, j in enumerate(tasks):
        #     print(i, j)
        #     task_dict[j] += 1

        count = Counter(tasks)
        num = max(count.values())

        cnt = 0
        for i, j in count.items():
            if j == num:
                cnt += 1
        res = max((num - 1) * (n + 1) + cnt, len(tasks))
        return res


if __name__ == '__main__':
    s = Solution()
    tasks = ['A', 'A', 'B']
    n = 2
    print(s.leastInterval(tasks, n))