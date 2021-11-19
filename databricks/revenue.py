import heapq
from bisect import bisect_left
from collections import OrderedDict

# get_nested_revenue(id: int, max_nesting: int)-> int
#
# insert(10) -> 0
# insert(20, 0) -> 1
# insert(40, 1) -> 2
#
# 0 -> 1 -> 2
#  get_nested_revenue(0, 0) -> 10
#  get_nested_revenue(0, 1) -> 30

class Solution:
    def isPossibleDivide(self, nums: [int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        nums.sort()
        d = OrderedDict()
        for num in nums:
            d[num] = d.get(num, 0) + 1

        for key, val in d.items():
            while val != 0:
                for i in range(1, k):
                    nxt_key = key + i
                    if nxt_key not in d or d[nxt_key] == 0:
                        return False
                    d[nxt_key] -= 1
                val -= 1

        return True


# for one person, how many people can refer he or she?
# If we can refer the past user
class Revenue:
    def __init__(self):
        self.maxcnt = 0
        self.sortedlistarr = OrderedDict() # max_revenue list
    #   self.balancedTree =

    def insert(self, revenue):
        # self.sortedlistarr.append([revenue, [self.maxcnt]])
        res = self.maxcnt
        self.sortedlistarr[self.maxcnt] = [revenue, [self.maxcnt]]
        print(self.sortedlistarr)
        self.maxcnt += 1
        return res

    def insertRevenue(self, revenue, referrerID):
        l = self.sortedlistarr[referrerID]
        maxprofit, sortedlist = l[0], l[1]
        maxprofit += revenue
        l[1].append(self.maxcnt)
        self.sortedlistarr[referrerID] = [maxprofit, sortedlist]

        self.sortedlistarr[self.maxcnt] = [revenue, [self.maxcnt]]
        print(self.sortedlistarr)
        self.maxcnt += 1
        return self.maxcnt - 1

    def getKLowestRevenue(self, k, targetRevenue): # N*logk
        # 给定k和revenue，要求返回>给定revenue的k个最小revenue所对应的customer ID
        resHeap = []
        heapq.heapify(resHeap) #minheap
        heapq.heappush(resHeap, [-0.11, -1])
        threshold = 2
        # find the revenue using binary search
        for index in range(0, self.maxcnt):
            profit, linklist = self.sortedlistarr[index][0], self.sortedlistarr[index][1]
            # print(profit)
            if profit <= threshold:
                continue
            elif len(resHeap) == k:
                if profit < -1 * resHeap[0][0]:
                    heapq.heappop(resHeap)
                    heapq.heappush(resHeap, [-profit, index])
            else:
                heapq.heappush(resHeap, [-profit, index])
            heapq.heappush(resHeap, [-profit, index])

        # print(resHeap)
        return [k[1] for k in resHeap]

# may we go back to the same id again?
    def get_nested_revenue(self, id, max_nesting):
        step, queue = 0, []
        queue.append([0, []])
        cur_id = id
        while step < max_nesting and not queue:
            step += 1
            l = self.sortedlistarr[cur_id]
            profit, linklist = l[0], l[1]
            for s in linklist:

                queue.append()

if __name__ == '__main__':
    r = Revenue()
    r.insert(1)
    r.insert(2)
    r.insertRevenue(2, 0)
    print(r.getKLowestRevenue(1, 1))