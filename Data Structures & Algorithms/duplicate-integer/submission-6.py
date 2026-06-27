class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hset = set(nums)

        if len(hset) != len(nums):
            return True
        
        return False