class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        maxLen = 1
        result = s[0]
        for i in range(len(s)):
            c = s[i]
            l = i
            r = i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r-l+1 > maxLen:
                        maxLen = r-l+1
                        result = s[l:r+1]
                else:
                    break
                l-=1
                r+=1
        
        for i in range(len(s)):
            c = s[i]
            l = i
            r = i+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r-l+1 > maxLen:
                        maxLen = r-l+1
                        result = s[l:r+1]
                else:
                    break
                l-=1
                r+=1
        
        
        return result