# Key idea is, all the indexes of the array are actually
# pointers, so basically they are all a linked list.
# If a duplicate number exists, that means there is a cycle
# in the list. To find the duplicate number without modifying
# the list, we need to find the node where the cycle begins.
# There is a slow and fast pointer algorythm for that, called
# Flloyd's algorythm, and it has 2 steps. First you detect
# the node where the slow and fast pointer intersect the
# first time, and then the node where the cycle starts is half
# way between the node and the intersecting node.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # Find the intersect node
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Find the cycle start using another slow
        # pointer from the beginning
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                break
        return slow2