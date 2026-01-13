import heapq

class MedianFinder:

    def __init__(self):
        # Store approximate equal values in 2 heap for accessing max and min in O(1)
        self.maxHeap, self.minHeap =[], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -1 * num)
        # Make sure values in heap are there then if highest val of maxHeap greater than minHeaps min then swap
        if (self.maxHeap and self.minHeap) and -1 * self.maxHeap[0] > self.minHeap[0]:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        # The length of both heaps difference can't be greater than 1 if it's then swap to equalize
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = 1 * heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * val)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        return ((-1 * self.maxHeap[0]) + self.minHeap[0])/2