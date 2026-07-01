class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        def dfs(i,j,subset):
            if i == n and j == n:
                result.append(subset)
                return
            if i == n:
                while j < n:
                    subset+= ')'
                    j+=1
                result.append(subset)
                return
            
            if i > j:
                subset+= ')'
                dfs(i,j+1,subset)
                subset = subset[:-1]
                subset+= '('
                dfs(i+1,j,subset)
                subset = subset[:-1]
            elif i == j:
                subset += '('
                dfs(i+1,j,subset)
                subset = subset[:-1]
            elif i < j:
                return
        
        dfs(0,0,"")
        return result





