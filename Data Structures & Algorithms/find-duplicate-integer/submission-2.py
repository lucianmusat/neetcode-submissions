class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Marking negative solution
        # We know each number is between 1 and n, so each
        # number has a corresponding index. We mark each index
        # as negative, and if we find an index that is already
        # negative, we return it
        for num in nums:
            indx = abs(num) - 1
            if nums[indx] < 0:
                return abs(num)
            nums[indx] = -nums[indx]
        return 0