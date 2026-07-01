class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        Count= [0]*26

        for task in tasks:
            Count[ord(task)-ord('A')] +=1
        Count.sort()
        maxf = Count[25]
        idle = (maxf-1)*n
        for i in range(len(Count)-2,-1,-1):
            idle-=min(maxf-1,Count[i])
        
        if idle <= 0:
            return len(tasks)
        else:
            return len(tasks) + idle
            
