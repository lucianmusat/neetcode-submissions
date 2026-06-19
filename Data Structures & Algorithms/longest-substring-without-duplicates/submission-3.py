class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        chars = set()
        l, r = 0, 0
        max_length = 0

        while r < len(s):
            # Increase the right pointer until we find a duplicate
            if not s[r] in chars:
                chars.add(s[r])
                max_length = max(max_length, len(chars))
                r += 1
            else:
                # Increase the left pointer until the duplicate is gone
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1

        return max_length