
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left , self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    def insert(self, node):
        nextNode = self.left.next
        self.left.next = node
        node.prev = self.left
        node.next = nextNode
        nextNode.prev = node

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        value = node.val

        self.remove(node)
        self.insert(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.remove(node)
            self.insert(node)
        
        else:
            node = Node(key,value)
            self.cache[key] = node
            self.insert(node)
            if len(self.cache) > self.cap:
                keyOld = self.right.prev.key
                self.cache.pop(keyOld)
                self.remove(self.right.prev)
        


        
