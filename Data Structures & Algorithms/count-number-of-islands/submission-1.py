class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        groups = 0
        self.grid = grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == "1":
                    self.dfs(i,j)
                    groups += 1
        return groups

    def dfs(self, i, j):
        if i >= len(self.grid) or j >= len(self.grid[0]) or i < 0 or j < 0 or self.grid[i][j] == "0":
            return
        self.grid[i][j] = "0"
        self.dfs(i+1,j)
        self.dfs(i-1,j)
        self.dfs(i,j+1)
        self.dfs(i,j-1)
    