class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights)-1
        maxWater = 0
        while l < r:
            water = (r-l)*min(heights[l],heights[r])
            maxWater = max(water,maxWater)

            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        
        return maxWater
            