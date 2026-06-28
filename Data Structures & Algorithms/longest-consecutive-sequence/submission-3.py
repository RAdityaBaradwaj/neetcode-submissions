class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set()

        for num in nums:
            hset.add(num)
        
        result = 0
        for num in nums:
            if num - 1 in hset:
                continue
            else:
                seq = 1
                while num + 1 in hset:
                    seq+=1
                    num+=1
                result = max(result,seq)
        
        return result

                