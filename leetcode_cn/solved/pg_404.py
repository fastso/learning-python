# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        que = [root]
        while que:
            node = que.pop()
            if node:
                if node.left:
                    if not node.left.left and not node.left.right:
                        ans += node.left.val
                    else:
                        que.append(node.left)
                if node.right:
                    que.append(node.right)
        return ans
