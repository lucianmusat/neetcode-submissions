class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already_existing = set()
        for num in nums:
            if num in already_existing:
                return True
            already_existing.add(num)
        return False