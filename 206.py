# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        return self.recur(None, head)

    def recur(self, prevNode, currentNode):
        originalNextNode = currentNode.next
        if prevNode is None:
            currentNode.next = None
        else:
            currentNode.next = prevNode

        if originalNextNode == None:
            return currentNode
        else:
            return self.recur(currentNode, originalNextNode)
