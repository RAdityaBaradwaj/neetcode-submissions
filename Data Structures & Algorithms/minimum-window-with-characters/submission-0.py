class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0
        cSet = {}
        sSet = {}
        for c in t:
            cSet[c] = 1 + cSet.get(c, 0)
        
        have, need = 0, len(cSet)
        answer, answerLen = [-1,-1], float("infinity")
        maxLength = 0
        for j in range(len(s)):
            c = s[j]
            sSet[s[j]] = 1 + sSet.get(s[j],0)

            if c in cSet and sSet[c] == cSet[c]:
                have +=1
            
            while have == need:
                if (j-i+1) < answerLen:
                    answer= [i,j]
                    answerLen = j-i+1

                print(cSet,sSet)
                sSet[s[i]] -=1
                if s[i] in cSet and sSet[s[i]] < cSet[s[i]]:
                    have -=1
                i+=1
        i,j = answer

        return s[i:j+1] if answerLen != float("infinity") else ""


            