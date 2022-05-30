# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0
        stack_tree_node = [root]
        while stack_tree_node:
            node = stack_tree_node.pop()
            if not node.left and not node.right:
                ans += node.val
            if node.left:
                node.left.val = (node.val << 1) + node.left.val
                stack_tree_node.append(node.left)
            if node.right:
                node.right.val = (node.val << 1) + node.right.val
                stack_tree_node.append(node.right)
        return ans



