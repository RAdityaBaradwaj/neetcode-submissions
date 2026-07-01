class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)


        while len(maxHeap) > 1:
            stone1 = -heapq.heappop(maxHeap)
            stone2 = -heapq.heappop(maxHeap)

            rem = stone1 - stone2
            if rem > 0:
                heapq.heappush(maxHeap, -rem)
        
        return -maxHeap[0] if maxHeap else 0
