class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramHash = {}
        for i in range(len(strs)):
            hashArray = [0]*26
            for s in strs[i]:
                hashArray[ord(s) - ord("a")] +=1
            
            if anagramHash.get(tuple(hashArray)):
                anagramHash[tuple(hashArray)].append(strs[i])
            else:
                anagramHash[tuple(hashArray)] = [strs[i]]
        
        return list(anagramHash.values())
            
