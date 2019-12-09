# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        ans_h = ListNode(-1)

        index = ans_h
        while l1 and l2:
            if l1.val <= l2.val:
                index.next = l1
                l1 = l1.next
            else:
                index.next = l2
                l2 = l2.next
            index = index.next

        index.next = l1 if l1 is not None else l2

        return ans_h.next
