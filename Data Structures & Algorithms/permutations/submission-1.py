class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # could be done with swapping elements in place to save space
        def backtrack(current_perm):
            # base case
            if len(current_perm) == len(nums):
                result.append(list(current_perm))
                return
            # iterate over same nums each time
            for i in range(len(nums)):
                # do not chose numbers already chosen
                if nums[i] not in current_perm:
                    # typical backtracking
                    current_perm.append(nums[i])
                    backtrack(current_perm)
                    current_perm.pop()

        result = []
        backtrack([])
        return result

