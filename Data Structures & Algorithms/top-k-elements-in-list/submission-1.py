class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Counts = {}
        Top = {}
        for i in range(len(nums)):
            if Counts.get(nums[i]):
                Counts[nums[i]] +=1
            else:
                Counts[nums[i]] = 1
        
        Buckets = [[] for i in range(len(nums) + 1)]
        for num, count in Counts.items():
            Buckets[count].append(num)
        
        results = []

        for i in range(len(Buckets)-1,0,-1):
            for num in Buckets[i]:
                results.append(num)
                if(len(results) == k):
                    return results

        return results
                