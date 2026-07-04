class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hMap ={i:[] for i in range(n)}
        for p,q in edges:
            hMap[p].append(q)
            hMap[q].append(p)
        answer = 0

        visited = set()
        def dfs(par,p):
            if p in visited:
                return
            visited.add(p)
            for j in hMap[p]:
                if j == par:
                    continue
                dfs(p,j)
            return True

        for i in range(n):
            if i not in visited:
                dfs(-1,i)
                answer +=1        
        return answer


        
