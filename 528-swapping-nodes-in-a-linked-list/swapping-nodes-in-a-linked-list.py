# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        first = head
        for i in range(k - 1):
            first = first.next
        second = head
        fast = first
        while fast.next:
            fast = fast.next
            second = second.next
        first.val, second.val = second.val, first.val
        return head