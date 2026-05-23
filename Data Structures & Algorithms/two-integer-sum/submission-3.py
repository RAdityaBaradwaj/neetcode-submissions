class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            new_target = target - num
            for j in range(i+1,len(nums)):
                if nums[j] == new_target:
                    return [i,j]
    
