class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        result = []
        def dfs(arr,i,target):
            nonlocal result
            if target == 0:
                result.append(arr.copy())
                return
            
            if i >= len(candidates) or target < 0:
                return
            
            arr.append(candidates[i])
            dfs(arr,i+1,target-candidates[i])
            arr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(arr,i+1,target)
        
        dfs([],0,target)

        return result
            