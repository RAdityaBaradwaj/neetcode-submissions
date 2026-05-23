class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0

        if len(nums) == 1:
            return nums[0]

        for num in nums[:-1]:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        max1 = rob2
        rob1, rob2 = 0,0

        for num in nums[1:]:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return max(max1,rob2)

