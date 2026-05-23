class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mini = prices[0]
        for num in prices:
            profit = max(profit,num - mini)
            if num < mini:
                mini = num
        
        return profit