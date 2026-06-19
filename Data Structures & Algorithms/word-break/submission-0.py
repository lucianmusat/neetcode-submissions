class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP extra array
        dp = (len(s) + 1) * [False]
        # The one over the limit we set to True
        # "" always matches
        dp[len(s)] = True

        # Iterate the string backwards and try to match
        # with the available words 
        for i in range(len(s) -1, -1, -1):
            for word in wordDict:
                if (i + len(word) <= len(s)) and (s[i : i + len(word)] == word):
                    # Important detail: only set to True if the next word
                    # boundary was also True
                    dp[i] = dp[i + len(word)]
                if dp[i]: break
        
        return dp[0]