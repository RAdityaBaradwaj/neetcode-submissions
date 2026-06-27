class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        end = 0
        start = len(gas)-1
        totalGas = gas[start] - cost[start]
        while start > end:
            if totalGas < 0:
                start-=1
                totalGas += gas[start] -cost[start]
            else:
                totalGas += gas[end] - cost[end]
                end+=1
        
        return start if totalGas >=0 else -1