"""
Iterate through the nums (except the target cell)
For each index calculate the max reach from the location + the next
location (2 steps ahead). Jump to the optimal location.
After each jump increase the count.
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_count = 0
        current_jump_end = 0
        furthest_possible = 0

        for i in range(len(nums) - 1):
            furthest_possible = max(furthest_possible, i + nums[i])

            if i == current_jump_end:
                jump_count += 1
                current_jump_end = furthest_possible
        
        return jump_count

