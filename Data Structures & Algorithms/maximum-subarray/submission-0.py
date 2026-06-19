class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Basic checks
        if not nums:
            return 0

        # We iterate the array and keep track of 2 things:
        #   - the biggest sum we saw
        #   - the sum we have so far
        # If we reach a point where current sum is negative,
        # we just reset it to 0 and add the next number. This
        # way if the previous sums before a certain number is 
        # too small we disregard it.

        maxSum = nums[0]
        curSum = 0

        for n in nums:
            # This is where the magic happens, we add the sum of the
            # previous numbers to the current number, but only if
            # the sum is worth adding (> 0)
            curSum = max(curSum, 0) + n
            maxSum = max(maxSum, curSum)
        
        return maxSum