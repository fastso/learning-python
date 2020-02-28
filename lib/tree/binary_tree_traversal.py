"""
二叉树的遍历

* 深度优先搜索 depth first search
  * 前序遍历 Preorder 根左右
  * 中序遍历 Inorder 左根右
  * 后序遍历 Postorder 左右根

* 宽度优先搜索 breadth first search
"""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 前序遍历 Preorder
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not TreeNode:
            return []

        ans = []
        stack = [root, ]
        while stack:
            root = stack.pop()
            if root:
                ans.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return ans

    # 中序遍历 Inorder


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not TreeNode:
            return []

        ans = []
        stack = []

        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            ans.append(current.val)
            current = current.right
        return ans


# 后序遍历 Postorder
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = [root, ]
        while stack:
            root = stack.pop()
            if root:
                ans.append(root.val)
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)
        return ans[::-1]
