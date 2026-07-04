class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]

        rank = [1]*(len(edges)+1)

        def find(i):
            if i != par[i]:
                i = find(par[i])
            return par[i]
        
        def union(i,j):
            k, l = find(i), find(j)

            if k == l:
                return False
            
            if rank[k] > rank[l]:
                par[l] = k
                rank[l] += 1
            else:
                par[k] = l
                rank[k] += 1
            
            return True
        
        for i,j in edges:
            if not union(i,j):
                return [i,j]
