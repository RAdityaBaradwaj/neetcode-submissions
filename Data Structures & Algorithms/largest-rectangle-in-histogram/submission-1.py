class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        leftMost = []

        stack = []

        for i in range(len(heights)):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            leftMost.append(stack[-1] if stack else -1)
            stack.append(i)

        rightMost =[0]*len(heights)
        stack = []
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            rightMost[i] = (stack[-1] if stack else len(heights))
            stack.append(i)
        
        maxArea = 0
        for i in range(len(heights)):
            print(leftMost[i],rightMost[i],heights[i])
            maxArea = max(heights[i]*(rightMost[i]-leftMost[i]-1),maxArea)
        
        return maxArea