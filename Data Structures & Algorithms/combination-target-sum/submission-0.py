class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def backtrack(start, current_combination, current_sum):
            # base cases
            if current_sum == target:
                result.append(list(current_combination))
                return
            if current_sum > target:
                return
            # explore
            for i in range(start, len(nums)):
                # add element
                current_combination.append(nums[i])
                # backtrack
                # We do not increase i because we are allowed to reuse the current number
                backtrack(i, current_combination, current_sum + nums[i])
                # remove element
                current_combination.pop()

        result = []
        backtrack(0, [], 0)
        return result