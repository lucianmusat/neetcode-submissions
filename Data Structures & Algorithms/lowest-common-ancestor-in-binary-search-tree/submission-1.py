# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        head = root
        while head:
            if p.val < head.val and q.val < head.val:
                head = head.left
            elif p.val > head.val and q.val > head.val:
                head = head.right
            else:
                # If one is bigger and one is smaller it means there
                # is a split in the tree. The first split is the LCA.
                return head