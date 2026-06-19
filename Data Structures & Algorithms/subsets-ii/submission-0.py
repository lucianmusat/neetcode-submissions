class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
            result.append(list(subset))
            for i in range(start, len(nums)):
                # skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        # sort the nums array to skip duplicates
        nums.sort()
        result = []
        backtrack(0, [])
        return result