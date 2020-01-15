# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        tn = TreeNode(nums[mid])
        nums1 = nums[0:mid]
        nums2 = nums[mid + 1:len(nums)]
        tn.left = self.sortedArrayToBST(nums1)
        tn.right = self.sortedArrayToBST(nums2)
        return tn
