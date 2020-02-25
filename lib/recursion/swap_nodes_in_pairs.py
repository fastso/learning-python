"""
https://leetcode-cn.com/explore/orignial/card/recursion-i/256/principle-of-recursion/1201/
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node
