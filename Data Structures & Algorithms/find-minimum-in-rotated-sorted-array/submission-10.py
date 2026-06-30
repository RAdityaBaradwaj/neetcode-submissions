class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        answer = nums[0]
        while left < right:
            mid = (left + right + 1)//2


            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[left]:
                left = mid
            else:
                answer = min(answer,nums[right])
                break

        return answer
        

