class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1)
        maxMoney = 0
        for i,num in enumerate(nums):
            if i == 0 or i == 1:
                dp[i] = num
            else:
                dp[i] = num + max(dp[:i-1])
            if dp[i] > maxMoney:
                maxMoney = dp[i]
        
        return maxMoney