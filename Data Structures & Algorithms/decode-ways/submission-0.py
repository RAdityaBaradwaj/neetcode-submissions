class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        dp[0] = 1

        n = len(s)
        dp[len(s)] = 1

        for i in range(n-1,-1,-1):
            if s[i] == "0":
                dp[i] = 0
                continue
            else:
                dp[i] = dp[i+1]
            
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]
            
        return dp[0]