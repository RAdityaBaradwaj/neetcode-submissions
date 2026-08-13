class TrieNode:
    def __init__(self):
        self.isWord = False
        self.neighbors = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        tnode = self.root
        for c in word:
            if c in tnode.neighbors:
                tnode = tnode.neighbors[c]
            else:
                tnode.neighbors[c] = TrieNode()
                tnode = tnode.neighbors[c]
        
        tnode.isWord = True
        

    def search(self, word: str) -> bool:
        def dfs(i, root):
            if i == len(word):
                return root.isWord
            if word[i] == '.':
                for neighbor in root.neighbors.values():
                    if dfs(i+1,neighbor):
                        return True
            if word[i] in root.neighbors:
                if dfs(i+1,root.neighbors[word[i]]):
                    return True
            return False
        return dfs(0,self.root)



            
