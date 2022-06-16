# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val

        stack_list = [(root, targetSum - root.val)]
        while stack_list:
            node, target = stack_list.pop()
            if not node.left and not node.right:
                if target == 0:
                    return True
                else:
                    continue
            if node.left:
                stack_list.append((node.left, target - node.left.val))
            if node.right:
                stack_list.append((node.right, target - node.right.val))
        return False
