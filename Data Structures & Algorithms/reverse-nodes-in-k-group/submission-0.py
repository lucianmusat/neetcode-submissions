# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        group = 0

        # Advance forward k positions
        while cur and group < k:
            cur = cur.next
            group += 1
        
        if group == k:
            # Recursively revert the next groups
            cur = self.reverseKGroup(cur, k)
            # Reverse the current group
            while group > 0:
                # Same as a normal reversal, just that we have head instead of cur,
                # and cur instead of prev (we try to connect an already reversed
                # group to the current one)
                next = head.next
                head.next = cur
                cur = head
                head = next
                group -= 1
            # Set head for the next iteration of the recursive
            head = cur
        # if head != k just return head
        return head
            