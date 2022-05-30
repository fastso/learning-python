# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isBalanced_helper(root) != -1

    def isBalanced_helper(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.isBalanced_helper(root.left)
        right = self.isBalanced_helper(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
