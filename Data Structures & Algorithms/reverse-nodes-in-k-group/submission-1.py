# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        R = dummy
        for i in range(k):
            R = R.next
        
        start = dummy
        end = head
        prev = head
        L = head.next
        while R:
            for i in range(k - 1):
                if not L:
                    break
                temp = L.next
                L.next = prev
                prev = L
                L = temp
                if R:
                    R = R.next
            start.next = prev
            if end:
                end.next = L
            start = end
            end = L
            prev = L
            if L:
                L = L.next
            if R:
                R = R.next
        return dummy.next

            

        
