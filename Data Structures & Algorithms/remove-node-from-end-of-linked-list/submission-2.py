# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        P = None
        L = dummy
        R = dummy
        for i in range(n):
            R = R.next
        while R:
            P = L
            L = L.next
            R = R.next
        if L == head:
            return head.next
        P.next = L.next
        return head
        
        
        