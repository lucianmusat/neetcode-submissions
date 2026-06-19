class Solution:
    # Backtrack solution works, but is too inefficient
    # Two pointers solution
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        # We use an index, and two other pointers, i+1 and the end of the list
        # If the sum is too small we move the left pointer
        # If the sum is too big, we move the right pointer left
        # We skip duplicates for all of them
        for i in range(len(nums) - 2):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                if threesum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    # skip duplicates
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while r < l and nums[r] == nums[r - 1]:
                        r -= 1
                    # Move the pointers after finding a valid solution
                    l += 1
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    r -= 1
        return result
