class MedianFinder:

    def __init__(self):
        self.cap = 0
        self.heap = []
        self.maxheap = []
        heapq.heapify(self.heap)
        heapq.heapify(self.maxheap)

    def addNum(self, num: int) -> None:
        maxNum = -heapq.heappop(self.maxheap) if self.maxheap else -float('inf')
        heapq.heappush(self.heap,max(num,maxNum))
        heapq.heappush(self.maxheap,-min(num,maxNum))
        self.cap +=1
        if len(self.heap) > (self.cap)//2+1:
           heapq.heappush(self.maxheap,-heapq.heappop(self.heap))

        

    def findMedian(self) -> float:
        if self.cap % 2:
            return self.heap[0]
        else:
            num1 = heapq.heappop(self.heap)
            num2 = heapq.heappop(self.heap)
            heapq.heappush(self.heap,num1)
            heapq.heappush(self.heap,num2)

            return (num1+num2)/2
        
        