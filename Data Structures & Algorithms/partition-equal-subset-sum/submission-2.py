class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False

        # Only works if the sum is halfable
        if sum(nums) % 2 != 0:
            return False
        
        # Integer division
        target = sum(nums) // 2
        cache = {}

        def dfs(i: int, sum_so_far: int) -> bool:
            # base cases
            if sum_so_far == target:
                return True            
            if i >= len(nums) or sum_so_far > target:
                return False

            # get cache
            key = (i, sum_so_far)
            if key in cache:
                return cache[key]

            # Got 2 choices, to include or exclude current num
            include = dfs(i + 1, sum_so_far + nums[i])
            exclude = dfs(i + 1, sum_so_far)

            # add to cache
            cache[key] = include or exclude
            return cache[key]
            
        return dfs(0, 0)

        