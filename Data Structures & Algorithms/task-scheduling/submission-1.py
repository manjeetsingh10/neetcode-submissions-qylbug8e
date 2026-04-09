class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mh = []
        heapq.heapify(mh)

        counter = Counter(tasks)

        # at this point we have key and counter

        q = deque()

        for ctr in counter.values():
            heapq.heappush(mh, -ctr)
        # we have things populated at this point

        t = 0

        while len(mh) > 0 or len(q) > 0:
            t += 1

            ele = 1
            if len(mh) > 0:
                ele = heapq.heappop(mh)
            
            # decrement value. here, since it's negative, we will add 1
            ele += 1

            # only add if more cycles exist. 0 means it's over
            if ele < 0:
                q.append([ele, t + n])
            
            # add back to queue
            while len(q) and q[0][1] == t:
                heapq.heappush(mh, q.popleft()[0])

        
        return t
            
            




