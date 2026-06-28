class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        preHigh = [0]*len(height)
        postHigh = [0]*len(height)
        maxH = 0
        for i in range(1,len(height)):
            preHigh[i] = max(maxH,height[i-1])
            maxH = max(maxH,height[i-1])
        maxH = 0
        for i in range(len(height)-2,-1,-1):
            postHigh[i] = max(maxH,height[i+1])
            maxH = max(maxH,height[i+1])
        
        for i in range(len(height)):
            if min(preHigh[i],postHigh[i]) > height[i]:
            
                result += min(preHigh[i],postHigh[i]) - height[i]
        
        return result
