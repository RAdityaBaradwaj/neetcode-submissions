class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        answer = 0
        edgeMap = {i: [] for i in range(n)}
        for edge in edges:
            edgeMap[edge[0]].append(edge[1])
            edgeMap[edge[1]].append(edge[0])
        
        visited = set()
        def dfs(val,prev):
            if val in visited:
                return
            visited.add(val)
            for node in edgeMap[val]:
                if node !=prev:
                    dfs(node,val)
            edgeMap[val] = []
        
        for i in range(n):
            if i not in visited:
                dfs(i,-1)
                answer +=1
        
        return answer

            