class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points or len(points) == 0:
            return []
        
        heap = []
        heapq.heapify(heap)
        for x,y in points:
            dist = x*x + y*y

            heapq.heappush(heap, (-dist, x, y))
            while len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while len(heap) > 0:
            d,x,y = heapq.heappop(heap)
            result.append([x,y])
        
        return result
        