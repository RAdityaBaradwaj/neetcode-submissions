class TrieNode:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.isWord = False
    
    def add_Child(self, val, node):
        self.children[val] = node


class PrefixTree:

    def __init__(self):
        self.root = TrieNode('0')

    def insert(self, word: str) -> None:
        current = self.root
        for s in word:
            if s in current.children:
                current = current.children[s]
            else:
                childNode = TrieNode(s)
                current.add_Child(s,childNode)
                current = current.children[s]
        current.isWord = True

    def search(self, word: str) -> bool:
        current = self.root
        for s in word:
            if s in current.children:
                current = current.children[s]
            else:
                return False
        return current.isWord

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for s in prefix:
            if s in current.children:
                current = current.children[s]
            else:
                return False
            
        return True
        