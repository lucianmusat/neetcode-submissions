# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def add(self, l1, l2, carry=0) -> ListNode:
        # Base case, we don't have anything to add, or to create a node
        if not l1 and not l2 and not carry:
            return None
        
        # Calculate current sum and carry
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        carry, current_sum = divmod(val1 + val2 + carry, 10)

        # Call the function for the new node and pass the carry
        next_node = self.add(l1.next if l1 else None,
                             l2.next if l2 else None,
                            carry)
        
        return ListNode(current_sum, next_node)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.add(l1, l2)
        
        


