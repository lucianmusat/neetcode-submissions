# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root: Optional[TreeNode], tree_min: int, tree_max: int) -> bool:
            if not root: return True
            if not tree_min < root.val < tree_max:
                return False
            return (valid(root.left, tree_min, root.val) and
                   valid(root.right, root.val, tree_max))
        
        return valid(root, float("-inf"), float("inf"))