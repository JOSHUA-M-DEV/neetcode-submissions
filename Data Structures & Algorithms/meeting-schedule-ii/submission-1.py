"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        a=[]
        e=[]
        for i in intervals:
            a.append(i.start)
            e.append(i.end)
        a.sort()
        e.sort()
        print(a)
        print(e)
        i=0
        j=0
        c=0
        ans=0
        while i<len(a):
            if  a[i]<e[j]:
                i+=1
                c+=1
            else:
                j+=1
                c-=1
            ans=max(ans,c)
        return ans
        