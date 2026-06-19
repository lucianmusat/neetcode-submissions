# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Slow and fast pointer way to find the middle
    def find_middle(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head: ListNode) -> None:
        if not head: return None
        if not head.next: return head

        new_head = self.reverse_list(head.next)
        # reverse pointer of the next node to current
        head.next.next = head
        # break circular pointing
        head.next = None
        return new_head


    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        mid = self.find_middle(head)

        # split the list in two, and reverse the second part
        second_head = mid.next
        mid.next = None
        second_head = self.reverse_list(second_head)

        # traverse both lists, knowing that the second one is always smaller
        # and overwrite the pointers to point to each other
        first, second = head, second_head
        while second:
            # remember the next elements
            first_link, second_link = first.next, second.next
            # Update links
            first.next = second
            second.next = first_link
            # advance the pointers
            first, second = first_link, second_link
