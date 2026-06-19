class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # base case
        if not amount:
            return 0
        if not coins:
            return -1
        
        # cache
        cache = {}

        # dfs
        def dfs(amount_left: int) -> int:
            min_coins = float('inf')
            # base cases
            if amount_left == 0:
                return 0
            if amount_left < 0:
                return float('inf')
            
            # check cache
            if amount_left in cache:
                return cache[amount_left]
            
            # calculate sum so far
            for coin in coins:
                res = dfs(amount_left - coin)
                if res != float("inf"):
                    min_coins = min(min_coins, res + 1)

            cache[amount_left] = min_coins
            return min_coins

        result = dfs(amount)
        return -1 if result == float("inf") else result

