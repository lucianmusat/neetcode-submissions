class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return -1
        
        max_subarray_sum = nums[0]
        min_subarray_sum = nums[0]
        current_sum = 0
        # corner case, all are negative?
        all_negative = all(num < 0 for num in nums)
        if all_negative:
            return max(nums)
        max_sum = sum(nums)

        # calculate max subarray
        for num in nums:
            current_sum = max(current_sum, 0) + num
            max_subarray_sum = max(max_subarray_sum, current_sum)
        
        # calculate min subarray
        current_sum = 0
        for num in nums:
            current_sum = min(current_sum, 0) + num
            min_subarray_sum = min(min_subarray_sum, current_sum)
        
        # The trick is to remove the worst case minimum sub-array from
        # the middle of the array, then you re left with the maximum
        # sub-array wrapped around.
        return max(max_subarray_sum, max_sum - min_subarray_sum)