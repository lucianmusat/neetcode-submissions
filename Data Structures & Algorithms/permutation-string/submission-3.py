from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Keep two char Counters and keep comparing them
        permutation = Counter(s1)
        current_counter = Counter()
        l = 0

        for r in range(len(s2)):
            # Increment char count
            current_counter[s2[r]] += 1

            # If the window is too big, shrink it
            if r - l + 1 > len(s1):
                current_counter[s2[l]] -= 1
                l += 1
            
            if current_counter == permutation:
                return True
        
        return False
