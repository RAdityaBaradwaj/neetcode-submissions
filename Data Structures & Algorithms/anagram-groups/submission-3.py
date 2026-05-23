class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strmap = {}
        for str in strs:
            count = [0]*26
            for c in str:
                count[ord(c) - ord('a')] +=1
            if tuple(count) in strmap:
                strmap[tuple(count)].append(str)
            else:
                strmap[tuple(count)] = [str]
        
        return list(strmap.values())
