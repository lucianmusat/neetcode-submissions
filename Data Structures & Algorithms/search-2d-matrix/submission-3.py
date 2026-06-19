class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums: List[int], target: int) -> bool:
            low, high = 0, len(nums) -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return False
        
        for nums in matrix:
            if nums[0] <= target and nums[-1] >= target:
                return binary_search(nums, target)
        return False