from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        frequency_map = Counter(s)
        solution = []
        used_letters = set()
        substring_len = 0

        for c in s:
            used_letters.add(c)
            substring_len += 1
            frequency_map[c] -= 1

            if frequency_map[c] == 0:
                used_letters.remove(c)
            
            # We reached the end of a partition
            if len(used_letters) == 0:
                solution.append(substring_len)
                substring_len = 0

        return solution

