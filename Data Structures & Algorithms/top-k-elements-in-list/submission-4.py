class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = [[] for _ in range(len(nums)+1)]
        result = []
        freqCount = {}
        for num in nums:
            if num in freqCount:
                freqCount[num] += 1
            else:
                freqCount[num] = 1
        

        for (num, frequ) in freqCount.items():
            freq[frequ].append(num)
        
        print(freq)
        for i in range(len(freq)-1,-1,-1):
            while freq[i] and k > 0:
                result.append(freq[i].pop())
                k-=1
        
        return result
