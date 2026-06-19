class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # A helper function to check if we can finish in a certain ammount of time
        def can_finish(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)  # we need to round up the next hour
            return hours <= h

        
        # Binary search for the smallest rate that can eat the bananas in the allowed time
        # the minimum ammout to eat is 1 banana, the maximum is the largest pile
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if can_finish(mid):
                r = mid
            else:
                l = mid + 1
        return l