# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        ret = 0
        
        def explore(root: TreeNode) -> None:
            if not root:
                return
            values.append(-root.val)
            explore(root.left)
            explore(root.right)
        
        explore(root)
        heapq.heapify(values)
        while len(values) >= k:
            ret = -heapq.heappop(values)
        
        return ret