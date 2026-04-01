class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)

        while(len(maxheap) > 1):
            first = -heapq.heappop(maxheap)
            second = -heapq.heappop(maxheap)

            if first > second:
                heapq.heappush(maxheap, -(first-second))
            elif second > first:
                heapq.heappush(maxheap, -(second-first))
            
        if len(maxheap):
            return -maxheap[0] 
        else:
            return 0