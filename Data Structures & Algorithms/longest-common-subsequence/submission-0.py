class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            if text1[i] == text2[j]:
                if i == len(text1) -1 or j == len(text2) - 1:
                    dp[(i,j)] = 1
                    return 1
                else:
                    dp[(i,j)] = 1 + dfs(i+1,j+1)
                    return dp[(i,j)]
            else:
                max1 = 0
                max2 = 0
                if i < len(text1) - 1:
                    max1 = dfs(i+1,j)
                if j < len(text2) - 1:
                    max2 = dfs(i,j+1)
                dp[(i,j)] = max(max1,max2)
                return dp[(i,j)]
        
        return dfs(0,0)