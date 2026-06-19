# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Two pointer solution, where the right pointer is dephased from left
# by n+1. When r reaches the end then left is one node behind the one
# we are looking for, and we can modify the link to bypass it.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create extra node in front of the list to cover edge cases
        dummy = ListNode(0, head)
        l = r = dummy
        # move the r pointer n+1 positions ahead
        for _ in range(n + 1):
            r = r.next
        
        while r:
            l = l.next
            r = r.next
        
        # we reached the position, delete the node after l
        l.next = l.next.next
        return dummy.next