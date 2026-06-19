# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # previous, current = None, head

        # while current:
        #     next_node = current.next # save next node
        #     current.next = previous # reverse pointer
        #     previous = current # advance the pointers
        #     current = next_node
        # return previous

        # Recursive solution
        # Base cases
        if not head: return None
        if not head.next: return head

        # Recursive call with the next node
        new_head = self.reverseList(head.next)
        # Reverse next node's pointer to point back
        head.next.next = head
        head.next = None
        
        return new_head