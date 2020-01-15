from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = deque()
        q.append(root)
        q.append(root)
        while q:
            TreeNode
            t1 = q.popleft()
            TreeNode
            t2 = q.popleft()
            if t1 == None and t2 == None:
                continue
            elif t1 == None or t2 == None:
                return False
            elif t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True
