class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashSet = {}

        for s in strs:

            if tuple(sorted(s)) in hashSet:
                hashSet[tuple(sorted(s))].append(s)
            else:
                hashSet[tuple(sorted(s))] = [s]
        
        return list(hashSet.values())
