# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result = ListNode(0)
        current = result
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry
            if sum < 10:
                carry = 0
            else:
                carry = 1
            current.next = ListNode(sum - 10 * carry)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            current.next = ListNode(1)
        return result.next
