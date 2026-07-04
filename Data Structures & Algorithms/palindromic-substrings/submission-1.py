class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            l=i
            r=i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                else:
                    l-=1
                    r+=1
                    result+=1
        
        for i in range(len(s)):
            l=i
            r=i+1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                else:
                    l-=1
                    r+=1
                    result+=1
        
        return result
        
