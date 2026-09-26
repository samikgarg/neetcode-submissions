# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node, index):
        self.node = node
        self.index = index

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        curr = ListNode(0)
        heap = []
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, NodeWrapper(lst, i))

        while heap:
            minNodeWrapper = heapq.heappop(heap)
            minNode = minNodeWrapper.node
            index = minNodeWrapper.index
            if not head:
                head = minNode
            curr.next = minNode
            curr = curr.next
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(heap, NodeWrapper(lists[index], index))

        return head