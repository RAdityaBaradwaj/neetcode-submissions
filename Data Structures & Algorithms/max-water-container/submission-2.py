class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) -1
        maxArea = 0
        while i < j:
            maxArea = max(maxArea, (j-i)*min(heights[j],heights[i]))
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        
        return maxArea