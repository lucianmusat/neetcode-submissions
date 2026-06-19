class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i, nr in enumerate(nums):
            looking_for = target - nr
            if looking_for in indexes:
                return [indexes[looking_for], i]
            indexes[nr] = i