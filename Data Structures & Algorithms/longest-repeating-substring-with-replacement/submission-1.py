# Easier mode: from collections import Counter
# to counte the char frequency in a string
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        # Use a dictionary to count the chars
        char_frequency = {}
        max_frequency = 0
        l = 0

        for r in range(len(s)):
            window_size = r - l + 1
            char_frequency[s[r]] = char_frequency.get(s[r], 0) + 1
            max_frequency = max(max_frequency, char_frequency[s[r]])

            # if the window is invalid, shrink it
            if window_size - max_frequency > k:
                char_frequency[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, r - l + 1)
        
        return max_length