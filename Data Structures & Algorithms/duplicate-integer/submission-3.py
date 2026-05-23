class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nummap = []
        for num in nums:
            if num in nummap:
                return True
            else:
                nummap.append(num)
        
        return False

        
