class TrieNode:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.isWord = False

class Solution:
    def addWords(self, words) -> TrieNode:
        root = TrieNode('0')

        for word in words:
            current = root
            for s in word:
                if s not in current.children:
                    current.children[s] = TrieNode(s)
                current = current.children[s]
            current.isWord = True
        
        return root


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = self.addWords(words)
        seen = [[False]*len(board[0]) for i in range(len(board))]
        result = []

        def dfs(i,j,seen,wor,curr):
            nonlocal result
            if i < 0 or j < 0 or i > len(board)-1 or j > len(board[0])-1 or seen[i][j] or board[i][j] not in curr.children:
                return
            current = curr.children[board[i][j]]
            wor+=board[i][j]
            seen[i][j] = True
            if current.isWord:
                result.append(wor)
                current.isWord = False
            dfs(i+1,j,seen,wor,current)
            dfs(i-1,j,seen,wor,current)
            dfs(i,j+1,seen,wor,current)
            dfs(i,j-1,seen,wor,current)
            wor = wor[:-1]
            seen[i][j] = False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,seen,"",root)
        return result
