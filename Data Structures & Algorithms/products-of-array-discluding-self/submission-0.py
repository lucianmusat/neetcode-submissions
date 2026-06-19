class Solution:
    # The key idea is the result for a number is the product of
    # all the numbers before it x the product of all numbers after
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        prod_before = 1
        prod_after = 1

        # We iterate from both ends and keep the previous product
        # for boths sides in a separate variable.
        # It's actually 2 passes into one loop, one time each number
        # is multiplied by all before it, one time by all after it.
        for i in range(length):
            result[i] = result[i] * prod_before
            prod_before = prod_before * nums[i]
            result[length - i - 1] = result[length - i - 1] * prod_after
            prod_after = prod_after * nums[length - i - 1]
        
        return result