class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def dfs(curr,pick,result):
            if len(curr) == len(nums):
                result.append(curr.copy())
                return
            for i,p in enumerate(pick):
                if p == False:
                    pick[i] = True
                    curr.append(nums[i])
                    dfs(curr,pick,result)
                    pick[i]=False
                    curr.pop()
        
        curr = []
        pick = [False]*len(nums)

        dfs(curr,pick,result)

        return result


