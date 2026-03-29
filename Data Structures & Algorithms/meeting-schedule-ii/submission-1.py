"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals or len(intervals) == 0:
            return 0
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s, e = 0, 0
        result, count = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                # start new meeting
                s += 1
                count +=1
            else:
                e += 1
                count -=1
            result = max(result, count)
        
        return result