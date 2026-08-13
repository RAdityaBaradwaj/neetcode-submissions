class Node:
    def __init__(self, key = -1,val = -1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Node()
        self.right = Node()
        self.qMap = {}
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, newNode):

        temp = self.left.next
        self.left.next = newNode
        newNode.next = temp
        temp.prev = newNode
        newNode.prev = self.left
    
    def remove(self,delNode):
        left = delNode.prev
        right = delNode.next
        left.next = right
        right.prev = left
    
    def get(self, key: int) -> int:
        if key not in self.qMap:
            return -1
        valueNode = self.qMap[key]
        self.remove(valueNode)
        self.insert(valueNode)
        return valueNode.val

    def put(self, key: int, value: int) -> None:
        if key in self.qMap:
            valueNode = self.qMap[key]
            valueNode.val = value
            self.remove(valueNode)
            self.insert(valueNode)
        else:
            newNode = Node(key,value)
            self.qMap[key] = newNode
            self.insert(newNode)
            if len(self.qMap) > self.cap:
                removedNode = self.right.prev
                self.remove(removedNode)
                del self.qMap[removedNode.key]


        
