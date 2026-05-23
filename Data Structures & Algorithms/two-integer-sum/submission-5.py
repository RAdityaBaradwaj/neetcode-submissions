class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reminder = {}

        for i,num in enumerate(nums):
            rem = target - num
            if rem in reminder:
                return [reminder[rem],i]
            else:
                reminder[num] = i
        
        return [-1,-1]