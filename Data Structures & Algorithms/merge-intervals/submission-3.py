class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        mini = intervals[0][0]
        maxi = intervals[0][1]
        res = []
        print(intervals)
        for i in range(1,len(intervals)):
            if intervals[i][0] > maxi:
                res.append([mini,maxi])
                maxi = intervals[i][1]
                mini = intervals[i][0]
            else:
                maxi = max(intervals[i][1],maxi)
                mini = min(intervals[i][0],mini)
        res.append([mini,maxi])
        return res
