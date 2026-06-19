# Iterate string indexes, use 2-pointer technique to detect
# palindromes and increase the count.
# Check i-i and i-i+1 to check for odd and even palindromes
# O(n^2) solution
class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0
        for i in range(len(s)):
            palindromes += self.nr_palindromes(s, i, i)
            palindromes += self.nr_palindromes(s, i, i + 1)
        return palindromes

    def nr_palindromes(self, s: str, l: int, r: int):
        palindromes = 0
        len_s = len(s)
        while l >= 0 and r < len_s and s[l] == s[r]:
            palindromes += 1
            l -= 1
            r += 1
        return palindromes 