class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        comp = {}

        for c in s:
            if c in comp:
                comp[c] += 1
            else:
                comp[c] = 1
        
        for c in t:
            if c not in comp:
                return False
            else:
                comp[c] -= 1

        for i in comp.values():
            if i != 0:
                return False

        return True