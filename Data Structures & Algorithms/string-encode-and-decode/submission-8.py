class Solution:

    def encode(self, strs: List[str]) -> str:
        eString = ""
        lengths = []
        for s in strs:
            lengths.append(str(len(s)))
        
        eString += "#".join(lengths)
        eString += "$"
        eString += "".join(strs)

        return eString


    def decode(self, s: str) -> List[str]:
        result = []
        stringStartIndex = 0
        for i in range(len(s)):
            if s[i] == "$":
                stringStartIndex = i+1
                break
        i=0
        j = stringStartIndex
        while i < stringStartIndex:
            if s[i] == "$":
                break
            l=0
            while s[i+l] != "#" and s[i+l] != "$":
                l+=1
            length = s[i:i+l]
            result.append(s[j:j+int(length)])
            j= j+ int(length)
            i = i+l+1
        
        return result
            

            
            