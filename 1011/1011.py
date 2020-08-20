class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        def check_capacity(ship_capacity) -> bool:
            days = 1
            ship_weight = 0
            for weight in weights:
                ship_weight += weight
                if ship_weight > ship_capacity:
                    ship_weight = weight
                    days += 1
                    if days > D:
                        return False
            return True

        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if check_capacity(mid):
                right = mid
            else:
                left = mid + 1
        return left
