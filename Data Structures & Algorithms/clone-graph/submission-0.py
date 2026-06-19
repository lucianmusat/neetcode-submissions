"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def __init__(self):
        self.visited = {}
    # The tricky part here is to create new nodes in the visited data structure,
    # but not point the neighbors list to the old node, but fill in that info later
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None

        self.visited[node] = Node(node.val)  # leave neighbors empty for now, we haven't explored them yet
        queue = deque([node])
        while queue:
            current_node = queue.popleft() 
            for neighbor in current_node.neighbors:
                if neighbor not in self.visited:
                    self.visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # Link them while exploring
                self.visited[current_node].neighbors.append(self.visited[neighbor])

        return self.visited[node]


