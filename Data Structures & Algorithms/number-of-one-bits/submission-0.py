class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        print(n)
        while n > 0:
            count+= n % 2
            n = n//2
        
        return count