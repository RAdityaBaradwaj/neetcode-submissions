class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        numMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            numMap[crs].append(pre)

        answer = True
        visited = set()
        
        def dfs(num):
            if num in visited:
                return False
            
            if numMap[num] == []:
                return True
            
            visited.add(num)
            
            for number in numMap[num]:
                if not dfs(number):
                    return False
            
            visited.remove(num)
            numMap[num] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True



        