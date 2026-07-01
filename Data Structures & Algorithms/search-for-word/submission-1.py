class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False
        seen = [[False]*len(board[0]) for i in range(len(board))]

        def dfs(i,j,seen,curr):
            nonlocal result
            n = len(curr)
            if n == len(word):
                result = True
                return
            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or board[i][j] != word[n] or seen[i][j] == True:
                return
            curr = word[:n+1]
            seen[i][j] = True
            dfs(i+1,j,seen,curr)
            dfs(i,j+1,seen,curr)
            dfs(i-1,j,seen,curr)
            dfs(i,j-1,seen,curr)
            seen[i][j] = False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,seen,"")
        
        return result
