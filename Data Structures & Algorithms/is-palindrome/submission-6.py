class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = "".join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(stripped) - 1
        while l < r:
            if stripped[l] != stripped[r]:
                return False
            l += 1
            r -= 1
        return True