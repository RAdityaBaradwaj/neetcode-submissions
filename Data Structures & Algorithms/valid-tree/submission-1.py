class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adjMap = {i: [] for i in range(n)}
        visited = set()

        for edge in edges:
            adjMap[edge[0]].append(edge[1])
            adjMap[edge[1]].append(edge[0])
        print(adjMap)
        def dfs(num,prev):
            if num in visited:
                return False
            visited.add(num)
            for nums in adjMap[num]:
                if nums != prev:
                    if not dfs(nums,num):
                        return False
            adjMap[num] = []
            return True
        print(visited)
        answer1 = dfs(0,-1)
        answer2 = (len(visited) == n)

        return answer1 and answer2