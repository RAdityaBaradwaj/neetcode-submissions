class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = nums[0]

        for num in nums[1:]:
            curSum += num
            if curSum < 0:
                curSum = 0
                maxSum = max(maxSum, num)
            else:
                maxSum = max(maxSum,curSum)
        
        return maxSum
