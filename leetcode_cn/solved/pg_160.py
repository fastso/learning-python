# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 只有当链表 headA 和 headB 都不为空时，两个链表才可能相交
        if not headA or not headB:
            return None
        # 初始化两个指针，分别指向两个链表
        pa, pb = headA, headB
        # 当两个指针相等时，说明两个链表 相交 或者是 同时指向最后的空节点
        while pa != pb:
            # 如果链表 A 的指针为空，则将链表 A 的指针指向链表 B 的头结点
            pa = pa.next if pa else headB
            # 如果链表 B 的指针为空，则将链表 B 的指针指向链表 A 的头结点
            pb = pb.next if pb else headA
        return pa
