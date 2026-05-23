class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Counts = {}
        Top = {}
        for i in range(len(nums)):
            if Counts.get(nums[i]):
                Counts[nums[i]] +=1
            else:
                Counts[nums[i]] = 1
        
        sorted_dict = dict(sorted(Counts.items(), key=lambda item: -item[1]))

        return list(sorted_dict.keys())[:k]
                