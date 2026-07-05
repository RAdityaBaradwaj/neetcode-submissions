class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False  
        dp = {}   
        def dfs(k,i,j):
            if (k,i,j) in dp:
                return dp[(k,i,j)]
            if k == len(s3):
                return True
            if (i < len(s1) and s3[k] == s1[i]) and (j < len(s2) and s3[k] == s2[j]):
                dp[(k,i,j)] = dfs(k+1,i+1,j) or dfs(k+1,i,j+1)
                return dp[(k,i,j)]
            if i < len(s1) and s3[k] == s1[i]:
                dp[(k,i,j)] = dfs(k+1,i+1,j)
                return dp[(k,i,j)]
            elif j < len(s2) and s3[k] == s2[j]:
                dp[(k,i,j)] = dfs(k+1,i,j+1)
                return dp[(k,i,j)]
            else:
                dp[(k,i,j)] = False
                return False
        
        return dfs(0,0,0)
            
            
            

            