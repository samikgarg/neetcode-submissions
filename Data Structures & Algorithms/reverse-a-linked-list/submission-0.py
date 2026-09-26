# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev = head
        node = head.next
        
        while node is not None:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        head.next = None
        return prev