class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(current_perm):
            if len(current_perm) == len(nums):
                result.append(list(current_perm))
                return
            for i in range(len(nums)):
                if nums[i] not in current_perm:
                    current_perm.append(nums[i])
                    backtrack(current_perm)
                    current_perm.pop()

        result = []
        backtrack([])
        return result

