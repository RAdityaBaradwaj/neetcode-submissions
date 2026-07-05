class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        mini = intervals[0][0]
        maxi = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] > maxi:
                res.append([mini,maxi])
                mini = intervals[i][0]
                maxi = intervals[i][1]
            else:
                mini = min(intervals[i][0],mini)
                maxi = max(intervals[i][1],maxi)
        res.append([mini,maxi])

        return res
                