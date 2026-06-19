class Solution:
    def numDecodings(self, s: str) -> int:
        # corner cases
        if not s or s[0] == '0':
            return 0
        
        # just cache all recursions for performance
        cache = {}

        def dfs(i: int) -> int:
            # Got to the end of the recursion, means
            # we found a way to split
            if i == len(s):
                return 1
            
            if i in cache:
                return cache[i]
            
            if s[i] == "0":
                return 0
            
            # Chose one char and two chars if valid
            nr_ways = dfs(i + 1)
            if i + 1 < len(s) and 10 <= int(s[i: i + 2]) <= 26:
                nr_ways += dfs(i + 2)
            
            cache[i] = nr_ways
            return nr_ways
        
        return dfs(0)
        