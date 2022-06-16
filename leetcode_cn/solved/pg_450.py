# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            # key < 当前节点 去左子树查找
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # key > 当前节点 去右子树查找
            root.right = self.deleteNode(root.right, key)
        else:
            # key = 当前节点
            if not root.left:
                # 不存在左子树，右子树顶替其位置，删除当前节点
                return root.right
            elif not root.right:
                # 不存在右子树，左子树顶替其位置，删除当前节点
                return root.left
            else:
                # 左右子树都存在
                node = root.right
                # 找到右子树中最小的节点
                while node.left:
                    node = node.left
                # 右子树中最小的节点指向左子树
                node.left = root.left
                # 右子树顶替其位置，删除当前节点
                root = root.right

        return root
