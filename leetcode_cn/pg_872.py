# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaf_val_seq1 = []
        leaf_val_seq2 = []
        self.dfs(root1, leaf_val_seq1)
        self.dfs(root2, leaf_val_seq2)
        return leaf_val_seq1 == leaf_val_seq2

    def dfs(self, root: TreeNode, leaf_val_seq: list):
        stack = []
        p = root
        while p or stack:
            if p:
                if p.left is None and p.right is None:
                    leaf_val_seq.append(p.val)
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                p = p.right
