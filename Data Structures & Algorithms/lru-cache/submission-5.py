class Node:
    def __init__(self, key: int, val:int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key : node address
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next , self.tail.prev =   self.tail, self.head

    def deleteNode(self, node):

        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

        node.next = None
        node.prev = None
        return

    def insertNode(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

        return

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            self.insertNode(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists, update value
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.deleteNode(node)
            self.insertNode(node)
        else: # if key DNE, add to cache
            node = Node(key, value)
            self.cache[key] = node

            # if capacity reached, delete LRU
            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self.deleteNode(lru)
                del self.cache[lru.key]

            self.insertNode(node)

        return 
            

