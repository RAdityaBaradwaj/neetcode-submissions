class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrings = {}
        for index, string in enumerate(strs):
            sortedStrings[index] = ''.join(sorted(string))
        
        stringSet = set()
        stringAnswer = {}
        for index, string in enumerate(sortedStrings.values()):
            if string in stringSet:
                stringAnswer[string].append(strs[index])
            else:
                stringSet.add(string)
                stringAnswer[string] = [strs[index]]
        return list(stringAnswer.values())
