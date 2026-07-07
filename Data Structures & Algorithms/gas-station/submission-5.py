class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Check if there is enough gas to last the whole trip
        if sum(gas) < sum(cost):
            return -1
        
        current_cost = 0
        start_point = 0

        for i in range(len(gas)):
            # For each gas station check if the cost covers the next trip
            # When we arrive at a point where we get stranded we can disregard all
            # the stations before and try the next from scratch.
            current_cost += gas[i] - cost[i]
            if current_cost < 0:
                current_cost = 0
                start_point = i + 1
        
        return start_point