class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasures = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    treasures.append((i,j))
        
        def bfs(t):
            INF = 2147483647
            queue = t
            level = 0
            seen = [[False]*len(grid[0]) for _ in range(len(grid))]

            while queue:
                lenQ = len(queue)
                print("hello",queue,lenQ)
                while lenQ > 0:
                    x,y = queue.pop(0)
                    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == -1 or seen[x][y] == True:
                        lenQ-=1
                        continue
                    if grid[x][y] != 0:
                        grid[x][y] = min(grid[x][y],level)
                    seen[x][y] = True
                    queue += [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
                    lenQ-=1
                level +=1
            
        bfs(treasures)
            


            

            
            


