class Solution:
    def numDecodings(self, s: str) -> int:
        result = 0
        hmap = {}
        def dfs(i):
            if i in hmap:
                return hmap[i]
            result = 0
            if i == len(s) -1 and s[i] != '0':
                return 1
            
            if i == len(s):
                return 1
            
            if s[i] == '0':
                return 0

            if int(s[i:i+2]) <= 26:

                result += dfs(i+2)
            
            result +=dfs(i+1)
            hmap[i] = result
            return result

        return dfs(0)
