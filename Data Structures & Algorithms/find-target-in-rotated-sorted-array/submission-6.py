class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first find the cut point

        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r-l) // 2
            if nums[m]<nums[r]:
                r = m
            else:
                l = m + 1
        #now l is the cut point
        pivot = l
        l = 0
        r = len(nums) - 1

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1


        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m -1
            elif nums[m] < target:
                l = m+1
        
        return -1

