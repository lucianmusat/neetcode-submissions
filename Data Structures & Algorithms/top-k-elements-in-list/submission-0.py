from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # This is the secret data structure, it counts the number of times 
        # an element exists, but it's not sorted.
        freq_map = Counter(nums)
        # We could use an extra heap to make it even more efficient, but this
        # is more readable. We sort the frequency map and only return the first
        # k elements
        sorted_elem = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        return [num for num, _ in sorted_elem[:k]]