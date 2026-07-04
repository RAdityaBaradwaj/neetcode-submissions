class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(h,i,j,reachable):
            if i < 0 or j < 0 or i >= len(heights) or j >= len(heights[0]) or heights[i][j] < h or reachable[i][j] == True:
                return
            
            reachable[i][j] = True
            dfs(heights[i][j],i-1,j,reachable)
            dfs(heights[i][j],i+1,j,reachable)
            dfs(heights[i][j],i,j-1,reachable)
            dfs(heights[i][j],i,j+1,reachable)
        

        #pacific
        pac = [[False]*len(heights[0]) for _ in range(len(heights))]
        atl = [[False]*len(heights[0]) for _ in range(len(heights))]
        for i in range(len(heights[0])):
            dfs(0,0,i,pac)
            dfs(0,len(heights)-1,i,atl)
        
        #atlantic
        for i in range(len(heights)):
            dfs(0,i,0,pac)
            dfs(0,i,len(heights[0])-1,atl)

        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if atl[i][j] and pac[i][j]:
                    result.append([i,j])
        
        return result
