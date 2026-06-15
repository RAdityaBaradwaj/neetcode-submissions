class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        totalSum = 0
        for i, num in enumerate(nums):
            totalSum = totalSum + num
            if totalSum < 0:
                maxSum = max(totalSum, maxSum)
                totalSum = 0
            else:
                maxSum = max(totalSum, maxSum)
        
        return maxSum