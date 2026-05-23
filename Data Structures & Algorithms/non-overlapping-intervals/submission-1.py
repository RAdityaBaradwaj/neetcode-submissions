class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        result = 0
        maxi = intervals[0][1]
        mini = intervals[0][0]
        for i in range(1,len(intervals)):
            if intervals[i][0] < maxi:
                result +=1
                maxi = min(maxi,intervals[i][1])
            else:
                mini = intervals[i][0]
                maxi = intervals[i][1]
        
        return result