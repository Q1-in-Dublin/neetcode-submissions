"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #input the reservation timelien
        # output how many meeting rooms require without conflict
        # constraint time will be 0<= start<end<=1,000,000
        
        starts = sorted([iv.start for iv in intervals])
        ends = sorted([iv.end for iv in intervals])
        s,e = 0,0
        count = 0
        result = 0
        
        while s < len(starts):
            # next is start?
            if starts[s]< ends[e]:
                count +=1
                s +=1
                # next is end
            else:
                count -=1
                e+=1
            result = max(result,count)
        return result