# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = list()
        while head:
            s.append(str(head.val))
            head = head.next

        return int(''.join(s), 2)
