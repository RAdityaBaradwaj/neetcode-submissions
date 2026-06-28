class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            target = -num
            l = i+1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r-=1
                elif nums[l] + nums[r] < target:
                    l+=1
                elif nums[l] + nums[r] == target:
                    result.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1] :
                        l+=1
                    while l < r and nums[r] == nums[r-1]: 
                        r-=1
                    l+=1
                    r-=1
        
        return result

            

                
            