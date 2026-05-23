class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if curr.children.get(c) == None:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfsSearch(root, j):
            curr = root
            for i in range(j,len(word)):
                if word[i] == '.':
                    for c, Node in curr.children.items():
                        if dfsSearch(Node,i+1):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    else:
                        curr = curr.children[word[i]]
            return curr.endOfWord
        
        return dfsSearch(self.root,0)
                    
        
