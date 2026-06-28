class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        longest = 0
        curr =0
        for i,c in enumerate(s):
            if c not in chars:
                chars[c] = i
                curr+=1
                longest = max(longest,curr)
            elif c in chars:
                m = chars[c]
                if curr < i - m:
                    curr+=1
                else:
                    curr = i-m
                longest = max(longest,curr)
                chars[c]=i
        return longest
