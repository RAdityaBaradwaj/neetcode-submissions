class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        Count = [0]*26
        for c in magazine:
            Count[ord(c)-ord('a')]+=1
        
        for c in ransomNote:
            Count[ord(c)-ord('a')]-=1
            if Count[ord(c)-ord('a')] < 0:
                return False
        
        return True