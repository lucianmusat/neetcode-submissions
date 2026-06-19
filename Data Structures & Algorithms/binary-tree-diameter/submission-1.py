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
            # store heights to avoid recalculation
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            # Calculate max diameter
            self.diameter = max(self.diameter, left_height + right_height)
            # But return height
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.diameter
        