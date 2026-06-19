class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}
        if not nums or len(nums) == 0:
            return 0

        def dfs(i: int) -> int:
            # base cases
            if i == len(nums) - 1:
                return 1
            if i >= len(nums):
                return 0

            # cache check
            if i in cache:
                return cache[i]

            max_len = 1 # at least the elem itself

            # explore
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    max_len = max(max_len, 1 + dfs(j))

            # cache set
            cache[i] = max_len
            return max_len
        
        # Important: we need to check from every index
        # because the LIS can start anywhere
        lis = 0
        for i in range(len(nums)):
            lis = max(lis, dfs(i))

        return lis