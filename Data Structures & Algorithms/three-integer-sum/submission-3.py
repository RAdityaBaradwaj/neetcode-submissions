class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        answers = set()
        nums.sort()
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            target = -nums[k]
            i = k+1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] == target:
                    answer.append([nums[i],nums[j],nums[k]])
                    i+=1
                    while nums[i] == nums[i-1] and i < j:
                        i+=1
                elif nums[i] + nums[j] < target:
                    i+=1
                elif nums[i] + nums[j] > target:
                    j-=1   
            
        print(answer)

        return list((answer))