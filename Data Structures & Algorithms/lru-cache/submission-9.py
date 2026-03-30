class Node:
    def __init__(self, key: int, val : int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key : node address
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self. head

    def insertNode(self, node):
        node.prev = self.head
        node.next = self.head.next
        tmp = self.head.next
        tmp.prev = node
        self.head.next = node
        return

    def deleteNode(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        node.next, node.prev = None, None
        return

    def get(self, key: int) -> int:
        # if key exists
        if key in self.cache:
            node = self.cache[key]
            # delete then insert node so node becomes MRU (most recently used)
            self.deleteNode(node)
            self.insertNode(node)
            return node.val
        # else return -1
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists, update value
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.deleteNode(node)
            self.insertNode(node)
            return 
        else:
            # else insert new key, value pair
            # if cache is full, remove LRU

            node = Node(key, value)
            self.cache[key] = node

            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self.deleteNode(lru)
                del self.cache[lru.key]

            self.insertNode(node)

