# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list2.val < list1.val:
            list1, list2 = list2, list1

        head = list1
        prev = list1
        list1 = list1.next

        while list1 is not None:
            if list1.val >= list2.val:
                prev.next = list2
                list1, list2 = list2, list1
            prev = list1
            list1 = list1.next
        
        prev.next = list2
        
        return head
        