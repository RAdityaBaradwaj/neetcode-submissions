class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n+1):
            ans = 0
            while i > 0:
                ans+= i%2
                i = i // 2
            result.append(ans)
        
        return result