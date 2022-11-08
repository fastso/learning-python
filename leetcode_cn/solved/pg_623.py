from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        cur_level = [root]
        for i in range(1, depth - 1):
            tmp = []
            for node in cur_level:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            cur_level = tmp
        for node in cur_level:
            node.left = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)
        return root
