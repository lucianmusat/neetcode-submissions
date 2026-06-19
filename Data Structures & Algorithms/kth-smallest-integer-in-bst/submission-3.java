/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

    private void explore(TreeNode root) {
        if (root == null) {
            return;
        }
        maxHeap.add(root.val);
        explore(root.left);
        explore(root.right);
    }

    public int kthSmallest(TreeNode root, int k) {
        if (root == null) {
            return 0;
        }
        int ret = 0;
        explore(root);
        while (maxHeap.size() >= k) {
            ret = maxHeap.poll();
        }
        return ret;
    }
}
