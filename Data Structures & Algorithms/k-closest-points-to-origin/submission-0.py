class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []

        for i in range(len(points)):
            dist = (points[i][0])**2 + (points[i][1])**2
            heap.append([dist,points[i][0],points[i][1]])
        res = []
        heapq.heapify(heap)
        while k > 0:
            dist, x, y = heapq.heappop(heap)
            res.append([x,y])
            k -=1
        return res

