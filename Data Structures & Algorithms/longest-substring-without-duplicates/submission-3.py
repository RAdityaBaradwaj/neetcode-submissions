class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i = 0
        j = 1
        letterSet = set()
        maxLength = 1
        if len(s) == 0:
            return 0
        letterSet.add(s[0])
        while j < len(s):
            print(i,j,letterSet)
            if s[j] in letterSet:
                letterSet.discard(s[i])
                i +=1
            else:
                letterSet.add(s[j])
                maxLength = max(maxLength, j - i + 1)
                j+=1
        
        return maxLength
