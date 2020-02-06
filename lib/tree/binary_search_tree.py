# Binary Search Tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def range_sum_bst(root: TreeNode, L: int, R: int) -> int:
    """
    给定二叉搜索树的根结点root，返回L和R之间的所有结点的值的和。

    对树进行深度优先搜索，对于当前节点 node，
    如果 node.val 小于等于 L，那么只需要继续搜索它的右子树；
    如果 node.val 大于等于 R，那么只需要继续搜索它的左子树；
    如果 node.val 在区间 (L, R) 中，则需要搜索它的所有子树。
    https://leetcode-cn.com/problems/range-sum-of-bst/

    :param root:
    :param L:
    :param R:
    :return:
    """
    ans = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if L <= node.val <= R:
                ans += node.val
            if node.val > L:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
    return ans



