class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.nodes = {}
        self.used = Node(0)
        self.used.next = self.used
        self.used.prev = self.used
        self.keys = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            currNode = self.nodes[key]
            self.moveToBack(currNode)
            return self.cache[key]
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            currNode = self.nodes[key]
            self.moveToBack(currNode)
            self.cache[key] = value
            return
        self.cache[key] = value
        currNode = Node(key, self.used, self.used.prev)
        self.used.prev = currNode
        currNode.prev.next = currNode
        self.nodes[key] = currNode
        self.keys += 1
        if self.keys > self.capacity:
            del self.cache[self.used.next.key]
            del self.nodes[self.used.next.key]
            self.used.next = self.used.next.next
            self.used.next.prev = self.used
            self.keys -= 1

    def moveToBack(self, currNode):
        prev = currNode.prev
        prev.next = currNode.next
        prev.next.prev = prev
        currNode.next = self.used
        currNode.prev = self.used.prev
        self.used.prev = currNode
        currNode.prev.next = currNode

class Node:
    def __init__(self, key = 0, next = None, prev = None):
        self.key = key
        self.next = next
        self.prev = prev
        
