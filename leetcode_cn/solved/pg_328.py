# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        event = head.next
        even = event

        while event and event.next:
            odd.next = event.next
            odd = odd.next
            event.next = odd.next
            event = event.next

        odd.next = even
        return head
