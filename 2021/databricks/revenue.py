from collections import defaultdict
from sortedcontainers import SortedList, SortedDict
import heapq


class Revenue:
    def __init__(self):
        self.maxcnt = 0
        self.idToRevenue = defaultdict(int)
        self.revenueToId = defaultdict(list) # sortedDict version
        # self.revenueToId = SortedDict()
        # def _remove_revenue(self, revenue, id_):
        #       self.revenue_to_ids[revenue].remove(id_)
        #
        #   if not self.revenue_to_ids[revenue]:
        #         del self.revenue_to_ids[revenue]
        # def _add_new_revenue(self, revenue, id_):
        #       if revenue not in self.revenue_to_ids:
        #             self.revenue_to_ids[revenue] = set()
        #
        #   self.revenue_to_ids[revenue].add(id_)

        self.idrefer = defaultdict(list) # used for the last extra question

    def insert(self, revenue):
        self.idToRevenue[self.maxcnt] = revenue
        self.revenueToId[revenue] = []
        self.revenueToId[revenue].append(self.maxcnt)
        self.maxcnt += 1
        return self.maxcnt - 1

    def insert_refer(self, revenue, referID):
        self.idToRevenue[self.maxcnt] = revenue
        self.revenueToId[revenue].append(self.maxcnt)

        self.idrefer[referID].append(self.maxcnt) # used for the last extra question

        originalValue = self.idToRevenue[referID]
        self.revenueToId[originalValue + revenue].append(referID)

        self.revenueToId[originalValue].remove(referID)
        self.idToRevenue[referID] = originalValue + revenue
        self.maxcnt += 1
        return self.maxcnt - 1

    def getKLowestSorted(self, k, targetRevenue):
        sorted(self.revenueToId.items())
        cnt, res = 0, []
        for key, value in self.revenueToId.items():
            if not value:
                continue
            if key < targetRevenue:
                continue
            for v in value:
                cnt += 1
                res.append(v)
                if cnt >= k:
                    return res
        return res

    def getLowestKByTotalRevenue(self, k, threshold):
        # 给定k和revenue，要求返回>给定revenue的k个最小revenue所对应的customer ID
        resHeap = []
        heapq.heapify(resHeap)  # minheap
        # find the revenue using binary search
        for key, value in self.revenueToId.items():
            if not value:
                continue
            heapq.heappush(resHeap, [key, value])
        cnt, res = 0, []
        while True:
            if cnt >= k:
                return res
            if not resHeap:
                return res
            nxt = heapq.heappop(resHeap)
            profit, ids = nxt[0], nxt[1]
            if profit < threshold:
                continue
            for id in ids:
                res.append(id)
                cnt += 1
                if cnt >= k:
                    return res
        # if it does not have k result
        return res

    def getNestedRevenue(self, id, max_nesting):
        q = [[0, self.idToRevenue[id], self.idrefer[id]]]
        max_profit = -1

        while q:
            step, profit, candidates = q.pop(0)
            if step == max_nesting:
                max_profit = max(profit, max_profit)
                continue
            if len(candidates) == 0:
                max_profit = max(profit, max_profit)
            for c in candidates:
                q.append([step + 1, profit + self.idToRevenue[c], self.idrefer[c]])
        return max_profit


if __name__ == '__main__':
    r = Revenue()
    print(r.insert(10))
    print(r.insert_refer(20, 0))
    print(r.insert_refer(40, 1))
    # print(r.insert_refer(15, 1))
    print("----------------------------")
    # r.insert_refer(2, 0)
    print(r.getLowestKByTotalRevenue(2, 35))
    print(r.getKLowestSorted(3, 35))
    # print(r.get_nested_revenue(0, 2))
    print("----------------------------")
    print(r.getNestedRevenue(0, 2))
