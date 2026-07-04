class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp1 = [0]*(n-1)
        dp2 = [0]*(n-1)
        dp1[0], dp1[1] = nums[0], max(nums[0],nums[1])
        dp2[0], dp2[1] = nums[1], max(nums[1],nums[2])

        for i in range(2,n-1):
            dp1[i] = max(nums[i]+dp1[i-2],dp1[i-1])
            dp2[i] = max(nums[i+1]+dp2[i-2],dp2[i-1])
            print(nums[i],nums[i+1])
        
        print(dp1,dp2)
        return max(dp1[-1],dp2[-1])