class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        
        cars.sort(key=lambda x: x[0],reverse=True)

        carFinish = []

        for i in range(len(cars)):
            carFinish.append((target - cars[i][0])/cars[i][1])
        
        stack =[carFinish[0]]

        result = 0

        for i in range(1,len(carFinish)):
            if carFinish[i] > stack[-1]:
                stack.append(carFinish[i])
        
        return len(stack)

