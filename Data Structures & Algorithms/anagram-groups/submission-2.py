class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resMap = {}

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) -  ord('a')] +=1
            if tuple(count) in resMap:
                resMap[tuple(count)].append(s)
            else:
                resMap[tuple(count)] = [s]
            
        return list(resMap.values())