class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Ccount = [0]*26

        for c in s:
            Ccount[ord(c)-ord('a')] +=1
        
        for c in t:
            Ccount[ord(c)-ord('a')]-=1
        
        for count in Ccount:
            if count != 0:
                return False
        
        return True