class Node:
    def __init__(self, key: int, val : int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key : address of node
        self.head = Node(0 , 0)
        self.tail = Node(0 , 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        node.next = None
        node.prev = None
        return
    
    def insertNode(self, node):
        node.next = self.head.next
        node.prev = self.head
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

        # update val if key exists
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            node.val = value
            self.insertNode(node)
        else:
            node = Node(key, value)
            self.cache[key] = node

            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self.deleteNode(lru)
                del self.cache[lru.key]

            self.insertNode(node)






            

