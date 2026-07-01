class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        arr= []
        def dfs(arr,i,target):
            if target == 0:
                result.append(arr.copy())
                return
            if i >= len(nums):
                return
            if nums[i] <= target:
                arr.append(nums[i])
                dfs(arr,i,target-nums[i])
                arr.pop()
                dfs(arr,i+1,target)
            else:
                dfs(arr,i+1,target)
        
        dfs(arr,0,target)

        return result