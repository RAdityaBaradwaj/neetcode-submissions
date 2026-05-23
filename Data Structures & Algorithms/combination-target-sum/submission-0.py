class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []

        def dfs(nums, target, soFar):
            nonlocal combos
            soFarCopy = soFar.copy()

            if len(nums) == 0:
                return
            if nums[0] > target:
                print(nums,target,soFar, "more than target")
                print(soFar,soFarCopy)
                dfs(nums[1:], target, soFar)
            elif nums[0] < target:
                print("less than target",nums,target,soFar)
                soFarCopy.append(nums[0])
                print(soFar,soFarCopy)
                dfs(nums,target-nums[0],soFarCopy)
                dfs(nums[1:],target,soFar)
            elif nums[0] == target:
                soFarCopy.append(nums[0])
                combos.append(soFarCopy)
                dfs(nums[1:],target, soFar)
        
        dfs(nums,target,[])

        return combos