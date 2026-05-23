class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxHeight = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            maxHeight = max(maxHeight, min(heights[i],heights[j])*(j-i))
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        
        return maxHeight