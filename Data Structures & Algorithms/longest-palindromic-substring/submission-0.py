class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            next_palindrome = self.max_palindrome(s, i, i)
            if len(longest) < len(next_palindrome):
                longest = next_palindrome
            next_palindrome =  self.max_palindrome(s, i, i+1)
            if len(longest) < len(next_palindrome):
                longest = next_palindrome
        return longest
    

    def max_palindrome(self, s:str, l: int, r: int) -> str:
        longest = ""
        while l >= 0 and r < len(s) and s[l] == s[r]:
            longest = s[l:r+1]
            l -= 1
            r += 1
        return longest