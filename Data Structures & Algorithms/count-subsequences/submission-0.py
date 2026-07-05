class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = {}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if j >= len(t):
                dp[(i,j)] = 1  
                return 1
            if i >= len(s):
                dp[(i,j)] = 0
                return 0
            result = 0

            if s[i] == t[j]:
                result += dfs(i+1,j+1)
            result += dfs(i+1,j)
            dp[(i,j)] = result
            return result
        
        return dfs(0,0)

