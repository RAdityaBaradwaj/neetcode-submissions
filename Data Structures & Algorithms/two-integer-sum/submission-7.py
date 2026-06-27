class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}
        for i, num in enumerate(nums):
            rem[target-num] = i
        
        for i,num in enumerate(nums):
            if num in rem and rem[num]!= i:
                return [i,rem[num]]
