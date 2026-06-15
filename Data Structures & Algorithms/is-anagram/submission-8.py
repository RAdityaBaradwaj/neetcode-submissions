class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        Count = [0]*26

        for c in s:
            Count[ord(c)-ord('a')]+=1
        
        for c in t:
            Count[ord(c)-ord('a')]-=1
            if Count[ord(c)-ord('a')] < 0:
                return False
        
        for co in Count:
            if co > 0:
                return False
        
        return True