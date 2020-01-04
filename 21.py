# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        l3 = ListNode(0)
        start = l3

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                l3.next = ListNode(l1.val)
                l3 = l3.next
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l3 = l3.next
                l2 = l2.next

        if l1 != None:
            l3.next = l1
        else:
            l3.next = l2

        return start.next
