class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(string):
            l = 0
            r = len(string) - 1

            while l < r:
                if string[l] == string[r]:
                    l+=1
                    r-=1
                else:
                    return False
            
            return True

        def dfs(string,soFar):
            nonlocal res
            if len(string) == 0:
                res.append(soFar)
                return

            for i in range(len(string)):
                soFarCopy = soFar.copy()
                print(string,soFar,i,string[:i+1])
                if isPalindrome(string[:i+1]):
                    soFarCopy.append(string[:i+1])
                    dfs(string[i+1:],soFarCopy)
            
        
        dfs(s,[])
        return res


