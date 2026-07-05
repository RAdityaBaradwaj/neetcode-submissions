class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        seen = set()
        dp = {}
        def dfs(i,j,val):
            if (i,j,val) in dp:
                return dp[(i,j,val)]
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] <= val or (i,j) in seen:
                return 0
            valnew = matrix[i][j]
            seen.add((i,j))
            result = 1 + max(dfs(i+1,j,valnew),dfs(i-1,j,valnew),dfs(i,j+1,valnew),dfs(i,j-1,valnew))
            seen.remove((i,j))

            dp[(i,j,val)] = result
            return result
        
        result = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result = max(result,dfs(i,j,-1))
        
        return result
