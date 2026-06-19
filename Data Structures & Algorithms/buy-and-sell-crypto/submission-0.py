class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1
        while r < len(prices):
            current_profit = prices[r] - prices[l]
            if current_profit > 0:
                profit = max(profit, current_profit)
            else:
                # Move the left pointer if profit <= 0
                l = r
            # Always move the right pointer
            r += 1

        return profit