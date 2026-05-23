class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        freq = [ [] for i in range(len(nums)+1)]

        answer = []
        for num in nums:
            if num in freqmap:
                freqmap[num] += 1
            else:
                freqmap[num] = 1
        
        for num, frequ in freqmap.items():
            freq[frequ].append(num)
        
        for i in range(len(freq)-1,-1,-1):
            if freq[i] != []:
                for j in range(len(freq[i])):
                    answer.append(freq[i].pop())
                    if len(answer) == k:
                        return answer
        
        return answer