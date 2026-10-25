# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        critical = []
        index = 1
        prev = head
        curr = head.next
        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                critical.append(index)
            prev = curr
            curr = curr.next
            index += 1
        if len(critical) < 2:
            return [-1, -1]
        minDistance = float('inf')
        for i in range(1, len(critical)):
            distance = critical[i] - critical[i - 1]
            minDistance = min(minDistance, distance)
        maxDistance = critical[-1] - critical[0]
        return [minDistance, maxDistance]
        