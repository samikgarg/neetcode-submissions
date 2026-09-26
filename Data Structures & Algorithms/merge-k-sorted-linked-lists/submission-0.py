# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        curr = ListNode(0)
        while any(lists):
            minVal = ListNode(float('inf'))
            index = -1
            for i, lst in enumerate(lists):
                if lst and lst.val < minVal.val:
                    minVal = lst
                    index = i
            if not head:
                head = minVal
            curr.next = minVal
            curr = curr.next
            lists[index] = lists[index].next
        return head