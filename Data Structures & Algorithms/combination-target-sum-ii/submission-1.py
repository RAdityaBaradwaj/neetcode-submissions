class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def recursion(i,rem,curr):
            if i>len(candidates)-1:
                return
            curr.append(candidates[i])
            if candidates[i] == rem:
                result.append(curr.copy())
            elif candidates[i] < rem:
                recursion(i+1,rem-candidates[i],curr)
            curr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            recursion(i+1,rem,curr)


        recursion(0,target,[])
        return result



                
                
