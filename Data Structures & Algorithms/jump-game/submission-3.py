class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False 
        winner_index = len(nums) - 1
        max_reach = 0

        for i in range(winner_index + 1):
            # We reached an unreachable index, got stuck:
            if i > max_reach: return False

            # Check furthest we can reach from here
            max_reach = max(max_reach, i + nums[i])

            # Check if we can get to the end
            if max_reach >= winner_index: return True
        
        return False

       