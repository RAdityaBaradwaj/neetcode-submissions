class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        dp = {}
        def dfs(a,i):
            if (a,i) in dp:
                return dp[(a,i)]
            if a == 0:
                dp[(a,i)] = 1
                return 1
            if i >= len(coins):
                return 0
            result = 0
            if a >= coins[i]:
                result += dfs(a-coins[i],i)
                result += dfs(a,i+1)
            else:
                result += dfs(a,i+1)
            
            dp[(a,i)] = result
            return result
        
        return dfs(amount,0)