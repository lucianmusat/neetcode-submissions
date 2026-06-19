# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head

        while current:
            next_node = current.next # save next node
            current.next = previous # reverse pointer
            previous = current # advance the pointers
            current = next_node
        return previous
