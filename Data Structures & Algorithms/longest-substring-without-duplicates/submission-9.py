class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        currentlength = 0
        cmap = {}

        for i,c in enumerate(s):
            if c not in cmap:
                currentlength +=1
                maxlength = max(currentlength, maxlength)
                cmap[c] = i
            else:
                if i - cmap[c] > currentlength:
                    currentlength+=1
                    maxlength = max(currentlength, maxlength)
                else:
                    currentlength = i - cmap[c]
                cmap[c] = i
        
        return maxlength