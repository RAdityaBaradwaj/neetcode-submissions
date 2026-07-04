class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh +=1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        if fresh == 0:
            return 0

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def bfs(queue,fresh):
            result = 0
            while queue and fresh:
                lenQ = len(queue)
                freshlast = fresh
                while lenQ > 0 and fresh:
                    x,y = queue.popleft()
                    for dr,dc in directions:
                        i,j = x+dr,y+dc
                        if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j] == 1:
                            grid[i][j] = 2
                            fresh-=1
                            queue.append((i,j))
                    lenQ-=1
                if fresh == freshlast and result > 0:
                    return -1
                result+=1
            
            if fresh > 0:
                return -1
            return result
        
        return bfs(queue,fresh)