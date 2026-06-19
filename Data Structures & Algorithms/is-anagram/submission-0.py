class Solution:
    def sorted_string(self, s: str) -> str:
        return "".join(sorted(s))

    def isAnagram(self, s: str, t: str) -> bool:
        return self.sorted_string(s) == self.sorted_string(t)        