class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isWord = False
    
    def add_Child(self,val,node):
        self.children[val] = node

class WordDictionary:

    def __init__(self):
        self.root = TrieNode('0')

    def addWord(self, word: str) -> None:
        current = self.root
        for s in word:
            if s not in current.children:
                childNode = TrieNode(s)
                current.add_Child(s,childNode)
            current = current.children[s]
        current.isWord = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j,len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.isWord
            
        return dfs(0,self.root)






