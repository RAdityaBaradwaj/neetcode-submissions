class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        smap = {}
        for i,s in enumerate(strs):
            sorteds = ''.join(sorted(s))
            if tuple(sorteds) in smap:
                smap[tuple(sorteds)].append(s)
            else:
                smap[tuple(sorteds)] = [s]
        
        return list(smap.values())
        

