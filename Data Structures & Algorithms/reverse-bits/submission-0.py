class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0

        for i in range(31,-1,-1):
            answer += int(math.pow(2,i))*(n%2)
            n = n//2
            if n == 0:
                break
        
        return answer

