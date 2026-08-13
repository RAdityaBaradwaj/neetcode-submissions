class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        hmap = {}
        def dfs(t1,t2):
            if (t1,t2) in hmap:
                return hmap[(t1,t2)]
            if t1 >= len(text1) or t2 >= len(text2):
                hmap[(t1,t2)] = 0
                return 0
            
            result = 0
            if text1[t1] == text2[t2]:
                result = max(result, dfs(t1+1,t2+1) + 1)
            
            result = max(result,dfs(t1+1,t2),dfs(t1,t2+1))

            hmap[(t1,t2)] = result
            return result
        
        return dfs(0,0)