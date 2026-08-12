class Solution:
    def canJump(self, nums: List[int]) -> bool:
        hmap = {}

        def dfs(i):
            if i in hmap:
                return hmap[i]
            if i == len(nums) - 1:
                hmap[i] = True
                return True
            
            for j in range(1,nums[i]+1):
                if dfs(i+j):
                    hmap[i] = True
                    return True
            
            hmap[i] = False
            return False
        
        return dfs(0)
