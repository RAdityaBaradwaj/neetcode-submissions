class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = {}
        
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if i == len(word1) and j == len(word2):
                dp[(i,j)] = 0
                return 0
            if j >= len(word2):
                dp[(i,j)] = len(word1)-i
                return len(word1)-i
            if i >= len(word1):
                dp[(i,j)] = len(word2)-j
                return len(word2)-j
            result = 0
            if word1[i] == word2[j]:
                result = dfs(i+1,j+1)
            else:
                result = min(1+dfs(i+1,j+1), 1+ dfs(i+1,j),1+dfs(i,j+1))
            
            dp[(i,j)] = result
            return result

        return dfs(0,0)
            
            