# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
            # Calculate max diameter
            self.diameter = max(self.diameter, dfs(root.left) + dfs(root.right))
            # But return height
            return 1 + max(dfs(root.left), dfs(root.right))
        
        dfs(root)
        return self.diameter
        