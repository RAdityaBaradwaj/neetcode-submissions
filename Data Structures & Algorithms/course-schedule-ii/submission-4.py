class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hMap = {i:[] for i in range(numCourses)}
        result = []
        for p,q in prerequisites:
            hMap[p].append(q)
        seen, visited = set(), set()
        def dfs(i):
            nonlocal result
            if i in seen:
                return True
            if i in visited:
                return False
            visited.add(i)
            for j in hMap[i]:
                if not dfs(j):
                    return False
            visited.remove(i)
            result.append(i)
            seen.add(i)
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return result

        
        

