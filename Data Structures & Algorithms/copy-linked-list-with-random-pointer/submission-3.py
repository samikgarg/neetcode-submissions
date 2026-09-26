"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
            
        curr = head
        while curr:
            newCurr = Node(curr.val, curr.next)
            curr.next = newCurr
            curr = curr.next.next
        
        newHead = head.next
        curr = head
        currNew = head.next
        while curr:
            currNew.random = curr.random.next if curr.random else None
            curr = curr.next.next
            currNew = curr.next if curr else None

        curr = head
        currNew = head.next
        while curr:
            nextNode = curr.next.next
            newNextNode = nextNode.next if nextNode else None
            curr.next = nextNode
            currNew.next = newNextNode
            curr = nextNode
            currNew = newNextNode

        return newHead

