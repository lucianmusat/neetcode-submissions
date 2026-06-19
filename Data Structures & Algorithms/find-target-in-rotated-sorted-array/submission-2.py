class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # Trying to find the inflexion point using binary search
            # If nums[l] <= nums[mid] that means the left side is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:  # If target is in the sorted side
                    r = mid - 1
                else:
                    l = mid + 1  # Target must be in the other side
            else:  # The right side is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1