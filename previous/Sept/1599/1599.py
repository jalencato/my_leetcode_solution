from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting, profit, max_profit, count, res = 0, 0, -1, 0, 0
        for k in customers:
            count += 1
            waiting += k
            profit -= runningCost
            profit = profit + waiting * boardingCost if waiting <= 4 else profit + 4 * boardingCost
            waiting = 0 if waiting <= 4 else waiting - 4
            if max_profit < profit:
                max_profit = profit
                res = count

        while waiting > 0:
            count += 1
            profit -= runningCost
            profit = profit + waiting * boardingCost if waiting <= 4 else profit + 4 * boardingCost
            waiting = 0 if waiting <= 4 else waiting - 4
            if max_profit < profit:
                max_profit = profit
                res = count

        return res if max_profit >= 0 else -1


if __name__ == '__main__':
    s = Solution()
    customers = [8, 3]
    boardingCost = 5
    runningCost = 6
    print(s.minOperationsMaxProfit(customers, boardingCost, runningCost))