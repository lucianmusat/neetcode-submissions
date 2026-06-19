# DP algorithm
# Same as house robber one, with one added corner case
# where we are not allowed to pick the first and the last
# house at the same time.
# The solution is to calculate the max from the list without the
# last house and the list without the first house. 
# We go through the list twice, so it's O(2n), so O(n)
class Solution:

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.calculate_max(nums[:-1]), self.calculate_max(nums[1:]))
    
    def calculate_max(self, nums: List[int]) -> int:
        previous_house = two_houses_before = 0
        
        for house in nums:
            house = max(house + two_houses_before, previous_house)
            two_houses_before = previous_house
            previous_house = house
        
        return previous_house