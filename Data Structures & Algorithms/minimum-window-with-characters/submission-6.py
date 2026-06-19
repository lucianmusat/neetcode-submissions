from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        target_counter = Counter(t)
        current_counter = Counter()
        l = 0
        result, shortest_substring_len = [-1, -1], float("inf")
        # This is key here, we need to track the length of "UNIQUE" chars that we need
        # not the total ammount, so len(t) will not work in our case.
        # This is because we also check that current_counter[s[r]] == target_counter[s[r]]
        # in order to bump "have", which only bumps it if we have the exact number we need
        have, need = 0, len(target_counter)

        for r in range(len(s)):
            current_counter[s[r]] += 1

            if s[r] in target_counter and current_counter[s[r]] == target_counter[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < shortest_substring_len:
                    result = [l, r]
                    shortest_substring_len = r - l + 1
                
                # Contract the window from the left
                current_counter[s[l]] -= 1
                if s[l] in target_counter and current_counter[s[l]] < target_counter[s[l]]:
                    have -= 1
                l += 1

        l, r = result
        return s[l : r + 1] if shortest_substring_len != float("inf") else ""