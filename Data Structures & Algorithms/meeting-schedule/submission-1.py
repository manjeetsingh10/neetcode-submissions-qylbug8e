"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.start)
        merged = []

        for interval in intervals:
            # happy case
            if not merged or interval.start >= merged[-1].end:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)
        

        return len(merged) == len(intervals)
