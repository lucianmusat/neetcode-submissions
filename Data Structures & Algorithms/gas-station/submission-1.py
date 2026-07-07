class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        current_cost = 0
        start_point = 0

        for i in range(len(gas)):
            current_cost += gas[i] - cost[i]
            if current_cost < 0:
                current_cost = 0
                start_point = i + 1
        
        return start_point