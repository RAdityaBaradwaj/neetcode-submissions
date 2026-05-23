class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            if i == 0:
                output.append(1)
            else:
                output.append(nums[i-1]*output[i-1])
        postfixMult = 1
        for i in range(len(nums)-1,-1,-1):
            if i == (len(nums) - 1):
                continue
            else:
                postfixMult*=nums[i+1]
                output[i]*=postfixMult
        
        return output

