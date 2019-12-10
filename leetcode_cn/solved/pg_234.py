# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow = head
        fast = head.next
        pre = None
        prepre = None

        while fast is not None and fast.next is not None:
            pre = slow
            slow = slow.next
            fast = fast.next.next

            pre.next = prepre
            prepre = pre

        p1 = slow.next
        slow.next = pre
        if fast:
            p2 = slow
        else:
            p2 = slow.next

        while p1 is not None:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True