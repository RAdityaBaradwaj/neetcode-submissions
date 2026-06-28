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
                if nums[i-k] == maxNum:
                    maxNum = max(nums[i-k+1:i+1])
                elif nums[i] > maxNum:
                    maxNum = nums[i]
                result.append(maxNum)
        
        return result