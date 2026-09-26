# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        L = head
        R = head.next
        while L and R:
            if L == R:
                return True
            L = L.next
            R = R.next
            if R:
                R = R.next
        return False
        