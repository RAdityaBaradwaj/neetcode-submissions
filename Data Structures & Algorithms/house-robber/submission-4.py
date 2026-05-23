class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums)+1)
        maxMoney = 0
        maxPrevMoney = 0
        for i,num in enumerate(nums):
            if i == 0 or i == 1:
                dp[i] = num
            else:
                if dp[i-2] > maxPrevMoney:
                    maxPrevMoney = dp[i-2]
                dp[i] = num + maxPrevMoney
            if dp[i] > maxMoney:
                maxMoney = dp[i]
        
        return maxMoney