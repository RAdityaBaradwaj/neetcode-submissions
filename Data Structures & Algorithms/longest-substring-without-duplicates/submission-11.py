class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hmap = {}
        longest = 0
        start = 0
        seq = 0
        for i,c in enumerate(s):
            if c not in hmap:
                longest = max(i-start+1,longest)
            elif c in hmap:
                start = max(start,hmap[c]+1)
                longest = max(i-start+1,longest)
            hmap[c]=i
            
        return longest

