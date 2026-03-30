class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        node.next, node.prev = None, None
        return


    def addNode(self, node):
        node.prev = self.head
        node.next = self.head.next
        tmp = self.head.next
        tmp.prev = node
        self.head.next = node
        return


    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            self.addNode(node)
            return node.val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            node.val = value
            self.addNode(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.addNode(node)


            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self.deleteNode(lru)
                del self.cache[lru.key]

            


