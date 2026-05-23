class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        result = 0
        maxFreq = 0
        letterMap = {}
        for j in range(len(s)):
            letterMap[s[j]] = 1 + letterMap.get(s[j],0)
            maxFreq = max(maxFreq, letterMap[s[j]])

            print(i,j,maxFreq)
            while (j-i+1) - maxFreq > k:
                letterMap[s[i]] -=1
                i +=1
            result = max(j-i+1,result)

        return result
                