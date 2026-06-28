class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preFix = [1]
        prod = 1
        for num in nums[:-1]:
            prod*=num
            preFix.append(prod)
        
        postFix =[1]*len(nums)
        prod = 1
        for i in range(len(nums)-2,-1,-1):
            prod*=nums[i+1]
            postFix[i]=prod
        
        result = [0]*len(nums)

        for i in range(len(nums)):
            result[i] = postFix[i]*preFix[i]
        
        return result