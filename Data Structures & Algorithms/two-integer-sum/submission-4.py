class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Use hash map to keep track of number indexes
        indexes = {}
        for i, nr in enumerate(nums):
            looking_for = target - nr
            if looking_for in indexes:
                return [indexes[looking_for], i]
            indexes[nr] = i