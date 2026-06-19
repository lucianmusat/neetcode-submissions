"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# We have to do 2 passes. First we create the node copies, then
# we re-create the links.
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_nodes_map = { None: None}

        cur = head
        while cur:
            new_nodes_map[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copy = new_nodes_map[cur]
            copy.next = new_nodes_map[cur.next]
            copy.random = new_nodes_map[cur.random]
            cur = cur.next
        
        return new_nodes_map[head]

