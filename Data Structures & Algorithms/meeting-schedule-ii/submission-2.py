"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = [x.start for x in intervals]
        end = [x.end for x in intervals]

        start.sort()
        end.sort()
        maxRooms = 0
        s,e = 0,0
        Rooms = 0
        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                s+=1
                Rooms += 1
                maxRooms = max(Rooms,maxRooms)
            else:
                e+=1
                Rooms-=1
        
        return maxRooms


        