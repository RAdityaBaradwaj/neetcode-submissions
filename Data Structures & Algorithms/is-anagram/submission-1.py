class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCounts = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if charCounts.get(s[i]):
                    charCounts[s[i]] += 1
                else:
                    charCounts[s[i]] = 1
                
                if charCounts.get(t[i]):
                    charCounts[t[i]] -= 1
                else:
                    charCounts[t[i]] = -1

            for i in range(len(charCounts.values())):
                if list(charCounts.values())[i] != 0:
                    return False
            
        return True
