class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1
        # Two pinter strategy, left will keep track of the lowest min
        # and r of the highest high, so l = best day to buy, r = best
        # day to sell.
        while r < len(prices):
            current_profit = prices[r] - prices[l]
            if current_profit > 0:
                profit = max(profit, current_profit)
            else:
                # Move the left pointer if profit <= 0
                # That means that the best day to buy is where r is,
                # we found a new min
                l = r
            # Always move the right pointer
            r += 1

        return profit