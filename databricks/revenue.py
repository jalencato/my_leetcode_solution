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


# for one person, how many people can refer he or she?
# If we can refer the past user
class Revenue:
    def __init__(self):
        self.maxcnt = 0
        self.sortedlistarr = OrderedDict() # max_revenue list
        self.revenue = []
        self.id = []
        self.referlist = []
    #   self.balancedTree =

    def insert(self, revenue):
        # self.sortedlistarr.append([revenue, [self.maxcnt]])
        res = self.maxcnt
        self.sortedlistarr[self.maxcnt] = [revenue, []]
        # print(bisect_left(self.sortedlistarr, 1))
        # print(self.sortedlistarr)
        self.maxcnt += 1
        return res

    def insertRevenue(self, revenue, referrerID):
        l = self.sortedlistarr[referrerID]
        maxprofit, sortedlist = l[0], l[1]
        maxprofit += revenue
        sortedlist.append(self.maxcnt)
        self.sortedlistarr[referrerID] = [maxprofit, sortedlist]

        self.sortedlistarr[self.maxcnt] = [revenue, []]
        print(self.sortedlistarr)
        self.maxcnt += 1
        return self.maxcnt - 1

    def getKLowestRevenue(self, k, targetRevenue): # N*logk
        # 给定k和revenue，要求返回>给定revenue的k个最小revenue所对应的customer ID
        resHeap = []
        heapq.heapify(resHeap) #minheap
        heapq.heappush(resHeap, [-0.11, -5])
        threshold = targetRevenue
        # find the revenue using binary search
        for index in range(0, self.maxcnt):
            print(index)
            profit, linklist = self.sortedlistarr[index][0], self.sortedlistarr[index][1]
            if profit <= threshold:
                continue
            elif len(resHeap) == k:
                if profit < -1 * resHeap[0][0]:
                    heapq.heappop(resHeap)
                    heapq.heappush(resHeap, [-profit, index])
            else:
                heapq.heappush(resHeap, [-profit, index])

        # minheap k*logk
        minHeap = []
        while resHeap:
            tmp = resHeap.pop()
            print(tmp)
            tmp = [-1*tmp[0], tmp[1]]
            heapq.heappush(minHeap, tmp)

        res = []
        while minHeap:
            tmp = minHeap.pop()
            res.append(tmp[1])
        # print(resHeap)
        # print(resHeap)
        return res

# may we go back to the same id again?
    def get_nested_revenue(self, id, max_nesting):
        step, queue = 0, []
        queue.append([0, [id]])
        while step < max_nesting:
            step += 1
            tmp_list = []
            while queue:
                q = queue.pop()
                if q[1]:
                    for i in q[1]:
                        cur_profit, cur_list = q[0] + self.sortedlistarr[i][0], self.sortedlistarr[i][1]
                        tmp_list.append([cur_profit, cur_list])
                else:
                    cur_profit, cur_list = q[0], []
                    tmp_list.append(tmp_list.append([cur_profit, cur_list]))
            queue = tmp_list
        return max([k[0] for k in queue])


# class RandomizedSet:
#
#     def __init__(self):
#         self.ls = list()
#         # self.dict=dict()
#         self.counter = defaultdict(int)
#         # self.lastinserted=-1
#
#     def insert(self, val: int) -> bool:
#         if (self.counter.get(val, 0) != 0):
#             return (False)
#
#         self.ls.append(val)
#         # self.lastinserted=val
#         self.counter[val] += 1
#         return (True)
#
#     def remove(self, val: int) -> bool:
#         if (self.counter.get(val, 0) == 0):
#             return (False)
#
#         self.ls.remove(val)
#         self.counter[val] -= 1
#         return (True)
#
#     def getRandom(self) -> int:
#
#         return self.ls[random.randint(0, len(self.ls) - 1)]
if __name__ == '__main__':
    print([1] + [2])
    r = Revenue()
    r.insert(1)
    r.insert(2)
    # print(r.getKLowestRevenue(2, 2))
    r.insertRevenue(2, 0)
    print(r.getKLowestRevenue(2, 2))
    print(r.get_nested_revenue(0, 2))