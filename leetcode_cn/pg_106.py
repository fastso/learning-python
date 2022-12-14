# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(inorder_left, inorder_right):
            # 構築するノードがない場合は None を返す
            if inorder_left > inorder_right:
                return None

            # postorderの最後の要素は根ノード
            val = postorder.pop()
            root = TreeNode(val)

            # 根ノードで左右部分木に分割
            index = idx_map[val]

            # 右部分木を構築
            root.right = build(index + 1, inorder_right)
            # 左部分木を構築
            root.left = build(inorder_left, index - 1)
            return root

        # 値からindexを取得するためのmap
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return build(0, len(inorder) - 1)
