class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetMap = {}
        for i in range(len(nums)):
            targetMap[target - nums[i]] = i
        
        for i,num in enumerate(nums):
            if num in targetMap and i != targetMap[num]:
                return [min(i,targetMap[num]),max(i,targetMap[num])]