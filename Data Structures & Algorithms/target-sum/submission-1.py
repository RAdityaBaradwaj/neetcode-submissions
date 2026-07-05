class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        def dfs(i,sum):
            if i > len(nums) or (i == len(nums) and sum != target):
                return 0
            if i == len(nums) and sum == target:
                return 1
            result = 0
            result +=dfs(i+1,sum-nums[i])
            result +=dfs(i+1,sum+nums[i])
            
            return result
        
        return dfs(0,0)
