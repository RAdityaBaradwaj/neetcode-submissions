"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        start = [num.start for num in intervals]
        end = [num.end for num in intervals]
        start.sort()
        end.sort()
        maxi = intervals[0].end
        mini = intervals[0].start
        result = 0
        count = 0

        i = 0
        j = 0

        while i < len(start) and j < len(end):
            if start[i] < end[j]:
                count +=1
                result = max(count,result)
                i+=1
            elif end[j] <= start[i]:
                count -=1
                j+=1
        
        return result
        

            