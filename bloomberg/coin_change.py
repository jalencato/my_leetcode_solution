from functools import lru_cache


def coinChange(coin, amount):

    @lru_cache(None)
    def helper(amount):
        if amount == 0:
            return [0, []]
        minRes = amount
        for i in coin:
            if amount >= i:
                minRes = min(minRes, helper(amount - i)[0] + 1)
        return minRes

    return helper(amount)


if __name__ == '__main__':
    coin, amount = [1, 2, 5], 11
    print(coinChange(coin, amount))