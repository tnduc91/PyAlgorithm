class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        reverseHead = None
        while head != None:
            newHead = head.next
            head.next = reverseHead
            reverseHead = head
            head = newHead

        return reverseHead
