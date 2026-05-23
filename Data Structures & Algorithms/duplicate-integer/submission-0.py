class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in range(len(nums)):
            if count.get(nums[i]):
                count[nums[i]]+=1
            else:
                count[nums[i]] = 1
            if count[nums[i]] == 2:
                return True
        
        return False