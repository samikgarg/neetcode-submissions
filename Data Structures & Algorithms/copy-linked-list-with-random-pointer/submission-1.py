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
        found = {}
        dummy = Node(0)
        res = dummy
        prev = dummy
        curr = head

        while curr:
            if curr in found:
                currNode = found[curr]
            else:
                currNode = Node(curr.val)
                found[curr] = currNode

            prev.next = currNode
            if curr.random and curr.random in found:
                currNode.random = found[curr.random]
            elif curr.random:
                currNode.random = Node(curr.random.val)
                found[curr.random] = currNode.random
            
            prev = currNode
            curr = curr.next

        return dummy.next

