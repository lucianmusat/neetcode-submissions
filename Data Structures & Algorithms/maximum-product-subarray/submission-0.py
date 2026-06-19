class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod, max_prod = 1, 1
        current_max = max(nums)
        # For each number keep count of the current min and max
        # and calculate a maximum using both, because it ca be
        # that a negative number x a positive number is the biggest
        # product
        for num in nums:
            old_min = min_prod * num  # keep the version before recalculation
            min_prod = min(max_prod * num, min_prod * num, num)
            max_prod = max(max_prod * num, old_min, num)
            current_max = max(current_max, max_prod)
        
        return current_max