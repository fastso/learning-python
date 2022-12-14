# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node: Optional[TreeNode]):
            # 再帰の終了条件 (leaf node)
            if node is None:
                return
            # 節点の処理
            ans.append(node.val)
            # 左部分木の処理
            preorder(node.left)
            # 右部分木の処理
            preorder(node.right)

        ans = []
        preorder(root)
        return ans
