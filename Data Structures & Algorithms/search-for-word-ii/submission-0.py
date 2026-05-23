class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        for word in words:
            curr = self.root
            for c in word:
                if curr.children.get(c) == None:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            
            curr.endOfWord = True
        
        ROWS, COLS = len(board),len(board[0])
        res, visit = set(), set()
        
        def dfs(r,c,node,word):
            if( r >= ROWS or c >=COLS or r < 0 or c < 0 or ((r,c) in visit) or board[r][c] not in node.children):
                return
            
            node = node.children[board[r][c]]
            print(word)
            word += board[r][c]
            visit.add((r,c))
            if node.endOfWord is True:
                res.add(word)
            
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,self.root,"")

        return list(res)



        