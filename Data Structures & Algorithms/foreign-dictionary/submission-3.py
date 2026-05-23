class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            minLen = min(len(words[i]),len(words[i+1]))
            a = words[i]
            b = words[i+1]
            if len(a) > len(b) and a[:minLen] == b[:minLen]:
                return ""
            for j in range(minLen):
                if a[j] != b[j]:
                    adj[a[j]].add(b[j])
                    break
        
        string = []
        visited = {}
        
        def dfs(num):
            if num in visited:
                return visited[num]
            
            visited[num] = True

            for nums in adj[num]:
                if dfs(nums):
                    return ""
            
            visited[num] = False
            
            string.append(num)
        
        for char in adj:
            if dfs(char):
                return ""

        string.reverse()
        
        return "".join(string)



