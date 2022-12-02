# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = [(root, 0)]
        ans = []
        while queue:
            node, depth = queue.pop(0)
            if not node:
                continue
            if depth == len(ans):
                ans.append(node.val)
            else:
                ans[depth] = max(ans[depth], node.val)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        return ans