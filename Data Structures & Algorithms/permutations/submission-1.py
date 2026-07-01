class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        taken = [False]*len(nums)
        result = []
        def dfs(arr, taken):
            if False not in taken:
                result.append(arr.copy())
            for i in range(len(taken)):
                if taken[i] == False:
                    arr.append(nums[i])
                    taken[i] = True
                    dfs(arr,taken)
                    taken[i] = False
                    arr.pop()
        
        dfs([],taken)
        return result

