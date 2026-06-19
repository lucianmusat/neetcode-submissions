class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert to set for O(1) searches
        nums_set = set(nums)
        streak = 0

        for num in nums:
            # We found a sequence start, check from here
            if num - 1 not in nums_set:
                cur_streak = 1
                cur_num = num
                while cur_num + 1 in nums_set:
                    cur_streak += 1
                    cur_num += 1
                streak = max(streak, cur_streak)
        
        return streak