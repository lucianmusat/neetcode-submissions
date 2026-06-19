class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # If the mid is larger than the rightmost element, the min nr must be in the right side
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
