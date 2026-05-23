class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i in range(len(nums)):
            if diff.get(nums[i]) != None:
                return [min(i,diff[nums[i]]),max(i,diff[nums[i]])]
            else:
                diff[target-nums[i]] = i
        
