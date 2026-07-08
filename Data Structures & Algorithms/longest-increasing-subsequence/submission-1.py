class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = {}
        def dfs(i):
            if i == len(nums):
                return 0
            if i in mem:
                return mem[i]

            LIS = 1
            for j in range(i,len(nums)):
                if nums[i] < nums[j]:
                    LIS = max(LIS,1+dfs(j))
            
            mem[i] = LIS
            return LIS
        
        return max(dfs(i) for i in range(len(nums)))

