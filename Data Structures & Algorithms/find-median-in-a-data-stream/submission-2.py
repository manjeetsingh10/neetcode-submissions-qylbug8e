class MedianFinder:

    def __init__(self):
        
        self.min, self.max = [], []
    def addNum(self, num: int) -> None:
            if len(self.min) and num > self.min[0]:
                heapq.heappush(self.min, num)
            else:
                heapq.heappush(self.max, -num)

            # rebalance if needed
            if len(self.max) > len(self.min) + 1:
                value = -1 * heapq.heappop(self.max)
                heapq.heappush(self.min, value)
            if len(self.min) > len(self.max) + 1:
                value = heapq.heappop(self.min)
                heapq.heappush(self.max, -1 * value)
    def findMedian(self) -> float:
        if len(self.max) > len(self.min):
            return -1 * self.max[0]
        elif len(self.min) > len(self.max):
            return self.min[0]
        else:
            return (-1 * self.max[0] + self.min[0]) / 2.0
        
        