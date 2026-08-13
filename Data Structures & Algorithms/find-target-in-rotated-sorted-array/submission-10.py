class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l < r:
            mid = (l+r)//2

            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid+1

        offset = l
        print(l)
        l,r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if nums[(mid+offset)%len(nums)] > target:
                r = mid-1
            elif nums[(mid+offset)%len(nums)] < target:
                l = mid+1
            else:
                return (mid+offset)%len(nums)
        
        return -1

