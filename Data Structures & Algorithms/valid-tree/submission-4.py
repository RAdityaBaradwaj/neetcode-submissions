class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hMap = {i:[] for i in range(n)}
        for p,q in edges:
            hMap[p].append(q)
            hMap[q].append(p)

        visited, seen = set(),set()
        def dfs(i,par):
            nonlocal visited
            if i in visited:
                return False
            visited.add(i)
            for j in hMap[i]:
                if j == par:
                    continue
                if not dfs(j,i):
                    return False
            visited.remove(i)
            seen.add(i)
            return True
        
        return dfs(0,-1) and len(seen) == n