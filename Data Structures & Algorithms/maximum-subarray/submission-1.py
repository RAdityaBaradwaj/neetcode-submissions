class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        totalSum = 0
        maxSum = nums[0]
        for num in nums:
            if totalSum < 0:
                totalSum = 0
            totalSum += num
            maxSum = max(maxSum, totalSum)
        
        return maxSum