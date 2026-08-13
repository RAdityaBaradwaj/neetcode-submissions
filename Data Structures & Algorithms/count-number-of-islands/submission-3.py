class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        def bfs(i,j):

            q = [(i,j)]

            while q:
                lenQ = len(q)
                for k in range(lenQ):
                    i,j = q.pop(0)
                    if i < len(grid) and i >= 0 and j < len(grid[0]) and j >= 0 and grid[i][j] == "1":
                        grid[i][j] = "0"
                        q.append((i+1,j))
                        q.append((i,j+1))
                        q.append((i-1,j))
                        q.append((i,j-1))
        
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    result +=1
                    bfs(i,j)
        
        return result


