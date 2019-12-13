# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ans = 0
        stack = []
        if root is not None:
            stack.append((1, root))

        while stack:
            current_depth, node = stack.pop()
            if node is not None:
                ans = max(ans, current_depth)
                stack.append((current_depth + 1, node.left))
                stack.append((current_depth + 1, node.right))
        return ans
