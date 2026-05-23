class MedianFinder:

    def __init__(self):
        self.rightHeap = []
        self.leftHeap = []

    def addNum(self, num: int) -> None:
        if self.rightHeap and self.rightHeap[0] < num:
            heapq.heappush(self.rightHeap, num)
        else:
            heapq.heappush(self.leftHeap, -1* num)

        rightLen = len(self.rightHeap)
        leftLen = len(self.leftHeap)

        if leftLen > rightLen + 1:
            val = -1*heapq.heappop(self.leftHeap)
            heapq.heappush(self.rightHeap,val)
        elif rightLen > leftLen + 1:
            val = heapq.heappop(self.rightHeap)
            heapq.heappush(self.leftHeap,-1*val)

    def findMedian(self) -> float:
        if len(self.leftHeap) > len(self.rightHeap):
            return -1*self.leftHeap[0]
        elif len(self.rightHeap) > len(self.leftHeap):
            return self.rightHeap[0]
        else:
            return (-1*self.leftHeap[0] + self.rightHeap[0])/2
        