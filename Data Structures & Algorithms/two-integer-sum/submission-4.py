class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nummap = {}

        for i,num in enumerate(nums):
            if target - num in nummap:
                return [min(i, nummap[target - num]), max(i, nummap[target - num])]
            nummap[num] = i
        

    
