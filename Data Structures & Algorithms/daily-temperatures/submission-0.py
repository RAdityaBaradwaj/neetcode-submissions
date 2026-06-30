class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        stack.append((temperatures[0],0))
        for i,temp in enumerate(temperatures[1:]):
            while stack and stack[-1][0] < temp:
                tempe,index = stack.pop()
                result[index] = (i+1)-index
            stack.append((temp,i+1))
        
        return result

            

            