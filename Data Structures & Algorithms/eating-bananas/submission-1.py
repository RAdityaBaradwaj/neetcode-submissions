class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        left, right = 1, maxPile

        while left <= right:

            mid = (left + right+1)//2
            if self.checkAnswer(piles,h,mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
    
    def checkAnswer(self,piles,h,k) -> bool:

        totalTime = 0
        for pile in piles:
            totalTime+= math.ceil(pile/k)
        
        if totalTime <= h:
            return True
        else:
            return False
            