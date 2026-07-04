class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {i: [] for i in range(numCourses)}

        for x,y in prerequisites:
            preMap[x].append(y)
        visit = set()
        def dfs(x):
            if x in visit:
                return False
            if preMap[x] == []:
                return True
            
            visit.add(x)
            for y in preMap[x]:
                if not dfs(y):
                    return False
            visit.remove(x)
            preMap[x] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
