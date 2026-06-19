# DP algorithm
# base case: only one house, the max amount is it's value
# general case: max amount for that house it's either the max
# from the previous house, or the current value + max from two
# houses before.
# We iterate the array and compute the max for each cell using this
# algorithm and return the last house, that should contain the best
# possible max
class Solution:

    def rob(self, nums: List[int]) -> int:
        previous_house = two_houses_before = 0
        
        for house in nums:
            house = max(house + two_houses_before, previous_house)
            two_houses_before = previous_house
            previous_house = house
        
        return previous_house