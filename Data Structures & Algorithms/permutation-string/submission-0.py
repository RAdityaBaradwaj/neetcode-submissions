class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n = len(s1)
        if len(s1) > len(s2):
            return False
        counts1, counts2 = [0]*26, [0]*26
        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] +=1
            counts2[ord(s2[i]) - ord('a')] +=1

        
        matches = 0
        for i in range(26):
            if counts1[i] == counts2[i]:
                matches +=1
        
        for i in range(len(s1),len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[i]) - ord('a')
            counts2[index] +=1
            if counts1[index] == counts2[index]:
                matches+=1
            elif counts1[index] == counts2[index]-1:
                matches-=1
            
            index = ord(s2[i-n]) - ord('a')
            counts2[index] -=1
            if counts1[index] == counts2[index]:
                matches+=1
            elif counts1[index] == counts2[index]+1:
                matches-=1
            
        if matches == 26:
            return True
        return False

            



