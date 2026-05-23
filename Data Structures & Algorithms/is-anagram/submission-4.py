class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0]*26
        for c in s:
            freq[ord(c) - ord('a')] +=1
        
        for c in t:
            freq[ord(c) - ord('a')] -=1
        
        for num in freq:
            if num != 0:
                return False
        
        return True