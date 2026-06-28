class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxNum = 0
        result = []

        for i in range(len(nums)):
            if i < k:
                maxNum = max(maxNum,nums[i])
                if i == k-1:
                    result.append(maxNum)
            else:
                result.append(max(nums[i-k+1:i+1]))
        
        return result