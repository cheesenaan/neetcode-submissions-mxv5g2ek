class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    
    def insertNode(self, node):
        tmp = self.head.next
        tmp.prev = node
        self.head.next = node
        node.next = tmp
        node.prev = self.head
        return

    def deleteNode(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        node.next, node.prev = None, None
        return
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            self.insertNode(node)
            return node.val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            node.val = value
            self.insertNode(node)
            return 
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insertNode(node)

            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self.deleteNode(lru)
                del self.cache[lru.key]



            
            


