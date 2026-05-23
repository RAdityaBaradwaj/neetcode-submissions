class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxString = ""
        maxLen = 0
        def lp(l,r):
            nonlocal maxString, maxLen
            print("start",l,r)
            if l < 0 and r > len(s) - 1 and s[l] != s[r]:
                return
            while l >= 0 and r <= len(s) -1 and s[l] == s[r]:
                if r - l >= maxLen:
                    print(l,r)
                    maxLen = r-l
                    maxString = s[l:r+1]
                l-=1
                r+=1
        
        for i in range(len(s)):
            lp(i,i)
            lp(i,i+1)
        return maxString