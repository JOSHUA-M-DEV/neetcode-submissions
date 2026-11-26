"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda a:a.start)
        l=[]
        for i in intervals:
            
            if len(l)==0 or l[-1].end<=i.start:
                l.append(i)
            else:
                return False
        return True
